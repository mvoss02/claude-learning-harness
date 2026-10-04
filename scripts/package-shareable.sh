#!/usr/bin/env bash
# Build a ZIP of the REUSABLE part of ~/.claude only. Private learning state
# (memory/ cards, mentor/ plans, journals, lessons, projects/) is never included.
#   scripts/package-shareable.sh [out.zip]
# Refuses to run if the secret scan or the private-path check fails.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="${1:-$ROOT/claude-config-shareable.zip}"
cd "$ROOT"

SHARE=(
  CLAUDE.md
  settings.json
  statusline.sh
  .gitignore
  hooks/session-start.py
  hooks/test_session_start.py
  hooks/gate-investigation.py
  hooks/test_gate_investigation.py
  scripts/
  docs/pedagogy/
  docs/private-state.md
  docs/specs/2026-09-13-learning-system-rework.md
  skills/mentor/
  skills/ship/
  memory/convention.md
)
# The public README differs from the private one (no review views, no private places).
PUBLIC_README=docs/README.public.md

scripts/scan-secrets.sh >/dev/null || { echo "secret scan failed; not packaging"; exit 1; }

STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT
for p in "${SHARE[@]}"; do
  [ -e "$p" ] || { echo "skip (missing) $p"; continue; }
  mkdir -p "$STAGE/$(dirname "$p")"
  cp -R "$p" "$STAGE/$p"
done
cp "$PUBLIC_README" "$STAGE/README.md"
rm -f "$STAGE/docs/README.public.md"
find "$STAGE" -name __pycache__ -type d -prune -exec rm -rf {} +

# Name placeholder: the hooks and docs print the learner's name in prose only.
find "$STAGE" -type f \( -name '*.md' -o -name '*.py' -o -name '*.json' -o -name '*.sh' \) -print0 \
  | xargs -0 sed -i '' -e "s/the learner's/the learner's/g" -e 's/the learner/the learner/g'

# Hard check: nothing private may have slipped in.
if find "$STAGE" -type f | grep -E '/memory/(archive|[a-z]+)/|/mentor/[^/]+/(PLAN|JOURNAL)\.md|/lessons/|/projects/|\.history\.md$|settings\.local\.json|\.DS_Store'; then
  echo "private path inside package; aborting"; exit 1
fi

rm -f "$OUT"
(cd "$STAGE" && zip -qr "$OUT" .)
echo "wrote $OUT ($(find "$STAGE" -type f | wc -l | tr -d ' ') files)"
unzip -l "$OUT" | tail -n +4 | awk '{print $4}' | grep -v '^$' | sed 's/^/  /' | head -60
