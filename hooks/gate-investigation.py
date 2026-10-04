#!/usr/bin/env python3
"""PreToolUse hook (Bash): deny investigation commands unless the hand-off flag is set.

Why: commands whose output is evidence (cluster, cloud, database, ssh, requests to
real services, infrastructure plans) are the learner's to run and read first. A prose
rule loses to the pull of progress; this gate does not. Claude proposes the exact
command with the why, the learner runs it with `! <cmd>`.

Gate opens when ~/.claude/.handoff-active exists. Claude creates it in one
visible Bash call inside a /ship task, or when the learner says "run it" for the
commands just proposed; removes it as soon as that step or task ends. Neither
changes the mode outside /ship. The session-start hook reports a leftover flag.

Input: hook JSON on stdin ({"tool_name": "Bash", "tool_input": {"command": ...}}).
Output: permissionDecision deny with a reason, or nothing (allow).
Env overrides for tests: CLAUDE_HOME.
"""
import json
import os
import re
import sys

HOME = os.environ.get("CLAUDE_HOME") or os.path.expanduser("~/.claude")
FLAG = os.path.join(HOME, ".handoff-active")

GATED = {
    "kubectl", "k9s", "helm", "flux", "kustomize", "stern",
    "az", "aws", "gcloud",
    "psql", "pg_dump", "pg_restore", "pgcli", "mysql", "redis-cli",
    "ssh", "scp", "sftp",
    "tofu", "terraform", "terragrunt",
}
# request tools: gated only when they target a non-local host
REQUEST = {"curl", "wget", "http", "https", "xh", "httpie"}
LOCAL_HOSTS = re.compile(r"^(localhost|127(\.\d{1,3}){3}|\[?::1\]?|0\.0\.0\.0)(:\d+)?$", re.I)
WRAPPERS = {"sudo", "time", "env", "nohup", "command", "exec", "xargs", "nice", "watch", "timeout",
            "do", "then", "else", "elif", "if", "while", "until", "{"}
def segments(cmd):
    """Split a shell command line into simple commands at |, ||, &&, ;, newline, $( and backtick,
    ignoring those characters inside single or double quotes (a grep pattern like "a|kubectl|b"
    is data, not a pipeline)."""
    out, cur, quote, i, n = [], [], None, 0, len(cmd)
    while i < n:
        c = cmd[i]
        if quote:
            cur.append(c)
            if c == quote and (quote == "'" or cmd[i - 1] != "\\"):
                quote = None
            i += 1
            continue
        if c in ("'", '"'):
            quote = c
            cur.append(c)
            i += 1
            continue
        if c == "\\" and i + 1 < n:
            cur.append(cmd[i:i + 2])
            i += 2
            continue
        two = cmd[i:i + 2]
        if two in ("||", "&&", "$("):
            out.append("".join(cur)); cur = []
            i += 2
            continue
        if c in "|;\n`":
            out.append("".join(cur)); cur = []
            i += 1
            continue
        cur.append(c)
        i += 1
    out.append("".join(cur))
    for seg in out:
        seg = seg.strip().lstrip("(").strip()
        if seg:
            yield seg


def head(seg):
    """First real executable of a segment, skipping env assignments and wrappers (and their flags)."""
    toks = seg.split()
    i = 0
    while i < len(toks):
        t = toks[i]
        if re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", t) or (t in WRAPPERS) or (i > 0 and toks[i - 1] in WRAPPERS and t.startswith("-")):
            i += 1
            continue
        return os.path.basename(t), toks[i + 1:]
    return "", []


def targets_remote(args):
    for a in args:
        m = re.match(r"^(?:https?://)?([^/\s]+)", a)
        if not m or a.startswith("-"):
            continue
        host = m.group(1)
        if "." in host or ":" in host or host in ("localhost",):
            if not LOCAL_HOSTS.match(host):
                return True
    return False


def gated_reason(cmd):
    for seg in segments(cmd):
        exe, args = head(seg)
        if exe in GATED:
            return f"`{exe}` is an investigation command"
        if exe in REQUEST and targets_remote(args):
            return f"`{exe}` against a non-local host is an investigation command"
    return ""


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        return
    if data.get("tool_name") != "Bash":
        return
    cmd = (data.get("tool_input") or {}).get("command") or ""
    if os.path.exists(FLAG):
        return
    reason = gated_reason(cmd)
    if not reason:
        return
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                f"GATE: {reason}. Its output is evidence the learner reads first. Propose the exact command and the why; "
                "he runs it with `! <cmd>`. Only inside /ship, or after he said 'run it' for this command, open the "
                "gate in one visible call: `touch ~/.claude/.handoff-active` (remove it right after)."
            ),
        }
    }))


if __name__ == "__main__":
    try:
        main()
    except Exception:  # noqa: BLE001
        sys.exit(0)
