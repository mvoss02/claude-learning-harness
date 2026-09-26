#!/usr/bin/env bash
# Secret scan over git-tracked files. Prints file:line and the PATTERN NAME only,
# never the matched value. Exit 1 on any hit.
#   scripts/scan-secrets.sh            scan ~/.claude tracked files
#   scripts/scan-secrets.sh <repo>     scan another repo
set -uo pipefail
REPO="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
cd "$REPO"

# name|regex  (ERE). Keep patterns specific; prose words like "secret" alone are not hits.
PATTERNS=(
  'aws-access-key|AKIA[0-9A-Z]{16}'
  'private-key-block|-----BEGIN [A-Z ]*PRIVATE KEY-----'
  'github-token|gh[pousr]_[A-Za-z0-9]{20,}'
  'slack-token|xox[abprs]-[A-Za-z0-9-]{10,}'
  'openai-style-key|sk-[A-Za-z0-9]{32,}'
  'sendgrid-key|SG\.[A-Za-z0-9_-]{16,}\.[A-Za-z0-9_-]{16,}'
  'azure-storage-key|AccountKey=[A-Za-z0-9+/=]{40,}'
  'azure-sas|sig=[A-Za-z0-9%]{30,}'
  'jwt-literal|eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}'
  'password-assignment|(password|passwd|pwd)[[:space:]]*[:=][[:space:]]*["'"'"']?[^[:space:]"'"'"']{8,}'
  'bearer-header|Authorization:[[:space:]]*Bearer[[:space:]]+[A-Za-z0-9._-]{20,}'
  'kubeconfig-token|token:[[:space:]]+[A-Za-z0-9._-]{40,}'
)

hits=0
files=$(git ls-files | grep -vE '\.(png|jpg|jpeg|gif|pdf|zip)$' || true)
for entry in "${PATTERNS[@]}"; do
  name="${entry%%|*}"
  regex="${entry#*|}"
  while IFS= read -r line; do
    [ -z "$line" ] && continue
    echo "HIT $name -> $line"
    hits=$((hits + 1))
  done < <(echo "$files" | xargs grep -nIE "$regex" 2>/dev/null | cut -d: -f1,2 || true)
done

if [ "$hits" -eq 0 ]; then
  echo "ok  no secret-pattern hits in $(echo "$files" | wc -l | tr -d ' ') tracked files"
  exit 0
fi
echo "$hits hit(s); inspect the lines above (values not printed)"
exit 1
