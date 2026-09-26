#!/usr/bin/env bash
# Validation suite for ~/.claude (config + learning ledger). Run from anywhere.
#   scripts/check.sh            all checks
#   scripts/check.sh --quick    skip the behavioral-scenario reminder
# Exit non-zero on the first failing check.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
fail=0
step() { printf '\n== %s\n' "$1"; }

step "JSON: settings.json, settings.local.json"
for f in settings.json settings.local.json; do
  [ -f "$f" ] || continue
  python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$f" && echo "ok  $f" || { echo "BAD $f"; fail=1; }
done

step "Python: compile hooks and scripts"
python3 -m py_compile hooks/*.py scripts/*.py && echo "ok  py_compile" || fail=1

step "Hook: UserPromptSubmit command emits valid JSON"
python3 - <<'EOF' || fail=1
import json, subprocess
cmd = json.load(open("settings.json"))["hooks"]["UserPromptSubmit"][0]["hooks"][0]["command"]
out = subprocess.run(["bash", "-c", cmd], capture_output=True, text=True, check=True).stdout
ctx = json.loads(out)["hookSpecificOutput"]["additionalContext"]
print(f"ok  UserPromptSubmit ({len(ctx)} chars)")
EOF

step "Hook: SessionStart fixtures"
python3 hooks/test_session_start.py || fail=1

step "Hook: PreToolUse investigation gate fixtures"
python3 hooks/test_gate_investigation.py | tail -1 || fail=1
python3 hooks/test_gate_investigation.py >/dev/null 2>&1 || { echo "gate fixtures FAILED"; fail=1; }

step "Hook: SessionStart live run"
python3 hooks/session-start.py | python3 -c "import json,sys; s=json.load(sys.stdin)['hookSpecificOutput']['additionalContext']; print(f'ok  live output ({len(s)} chars)')" || fail=1

step "YAML frontmatter (real parser via uv + pyyaml; offline first)"
if uv run --quiet --offline --script scripts/validate-frontmatter.py --require-keys name,description memory 2>/dev/null \
   || uv run --quiet --script scripts/validate-frontmatter.py --require-keys name,description memory; then
  echo "ok  memory/ frontmatter"
else
  fail=1
fi
uv run --quiet --offline --script scripts/validate-frontmatter.py skills docs mentor README.md 2>/dev/null \
  || uv run --quiet --script scripts/validate-frontmatter.py skills docs mentor README.md || fail=1

step "Ledger links, aliases, archive, index"
python3 scripts/check-links.py || fail=1

step "Referenced paths exist"
for p in docs/pedagogy/microdoses.md docs/pedagogy/teaching.md memory/convention.md memory/index.md \
         memory/independence.md memory/curriculum.md memory/checkpoints/checkpoints.md memory/notes/notes.md \
         hooks/gate-investigation.py hooks/test_gate_investigation.py hooks/test_session_start.py \
         docs/specs/2026-09-13-learning-system-rework.md \
         skills/mentor/SKILL.md skills/mentor/phases/intake.md \
         skills/mentor/phases/build.md skills/mentor/phases/lesson.md skills/mentor/phases/review.md \
         skills/mentor/phases/wrapup.md skills/mentor/references/learning-tree.md \
         skills/mentor/references/plan-format.md skills/mentor/references/rubric.md \
         skills/mentor/references/methods.md hooks/session-start.py README.md docs/private-state.md; do
  [ -e "$p" ] && echo "ok  $p" || { echo "MISSING $p"; fail=1; }
done

step "Stale wording sweep (should print nothing)"
if grep -rnE 'not skippable|cannot be deferred|no deferral|once per area|exactly once per plan|Three or more new terms|1 to 3 recall questions|Predictions before commands|only measurement|main path to .transferable|runs at the next session start|two-sentence say-back before use' \
     CLAUDE.md docs/pedagogy memory/convention.md memory/solo.md memory/independence.md hooks skills/mentor README.md settings.json; then
  echo "stale wording found"; fail=1
else
  echo "ok  no stale wording"
fi

step "Secret scan (tracked files)"
scripts/scan-secrets.sh || fail=1

if [ "${1:-}" != "--quick" ]; then
  step "Behavioral scenarios"
  echo "manual: run the scenarios in ~/Developer/mentor-skill/tests/scenarios via subagents (see tests/README.md there)"
fi

echo
[ "$fail" -eq 0 ] && echo "ALL CHECKS PASSED" || { echo "CHECKS FAILED"; exit 1; }
