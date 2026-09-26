#!/usr/bin/env python3
"""Fixture tests for hooks/gate-investigation.py. Run: python3 hooks/test_gate_investigation.py"""
import json
import os
import subprocess
import sys
import tempfile

HOOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gate-investigation.py")


def run(cmd, flag=False, tool="Bash"):
    with tempfile.TemporaryDirectory() as home:
        if flag:
            open(os.path.join(home, ".handoff-active"), "w").close()
        env = dict(os.environ, CLAUDE_HOME=home)
        payload = json.dumps({"tool_name": tool, "tool_input": {"command": cmd}})
        out = subprocess.run([sys.executable, HOOK], input=payload, env=env, capture_output=True, text=True, check=True).stdout
        if not out.strip():
            return None
        return json.loads(out)["hookSpecificOutput"]["permissionDecision"]


DENY = [
    "kubectl get pods -n prod",
    "kubectl logs deploy/api | grep ERROR",
    "az aks show -g rg -n aks",
    "psql -h db.internal -U app -c 'select 1'",
    "ssh redmine@10.0.0.4 'journalctl -u sshd'",
    "tofu plan -out=tf.plan",
    "cd infra && terraform apply",
    "flux get kustomizations",
    "helm list -A",
    "curl -s https://api.example.com/health",
    "curl http://10.0.0.5:8080/metrics",
    "sudo kubectl get nodes",
    "KUBECONFIG=/tmp/k kubectl get ns",
    "for p in a b; do kubectl delete pod $p; done",
    "echo x | xargs kubectl get pod",
    "time psql -c 'select 1'",
    "grep -c foo 'file.txt' | kubectl apply -f -",
    "echo \"done\"; ssh host 'uptime'",
]

ALLOW = [
    "grep -rn kubectl memory/",
    "rg 'az aks' docs/",
    "python3 hooks/test_session_start.py",
    "pytest -q",
    "go test ./...",
    "curl -s http://localhost:8000/health",
    "curl http://127.0.0.1:9090/-/ready",
    "git status",
    "ls -la ~/.kube",
    "cat infra/main.tf",
    "uv pip install pyyaml",
    "echo 'kubectl get pods' > runbook.md",
    "touch ~/.claude/.handoff-active",
    "man kubectl",
    'grep -nE "command|solo|kubectl|run " skills/mentor/SKILL.md',
    "grep -E 'az|psql|ssh' notes.md",
    'echo "a; kubectl get pods" > runbook.sh',
    "python3 -c \"print('helm|flux')\"",
]


def main():
    failed = 0
    for c in DENY:
        r = run(c)
        ok = r == "deny"
        failed += not ok
        print(("ok   " if ok else "FAIL ") + f"deny  {c!r} -> {r}")
    for c in ALLOW:
        r = run(c)
        ok = r is None
        failed += not ok
        print(("ok   " if ok else "FAIL ") + f"allow {c!r} -> {r}")
    r = run("kubectl get pods", flag=True)
    ok = r is None
    failed += not ok
    print(("ok   " if ok else "FAIL ") + f"flag opens gate -> {r}")
    r = run("kubectl get pods", tool="Read")
    ok = r is None
    failed += not ok
    print(("ok   " if ok else "FAIL ") + f"non-Bash tool ignored -> {r}")
    total = len(DENY) + len(ALLOW) + 2
    print(f"{total - failed}/{total} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
