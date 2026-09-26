# Private state vs reusable configuration

`~/.claude` is one git repo. It mixes reusable configuration (safe to share) with private learning state (not safe to share). This file says which is which, what protects the private part today, and how a full split would look if it is ever wanted.

## Status (2026-08-23)

- The remote of this repo is **private** (verified with the GitHub API at the time of writing). Keep it that way; re-check with `gh repo view <owner>/<repo> --json isPrivate` before any visibility change.
- The standalone mentor skill repo is **public**. It contains only the generic skill, tests with synthetic fixtures, and design docs. Nothing from `memory/` or `mentor/` is copied there.
- `scripts/scan-secrets.sh` scans tracked files for credential patterns without printing values; `scripts/check.sh` runs it. Last run: no hits.
- A full split into two repos was judged too invasive for this pass (the wikilinks and the hook assume one root). The measures below are the low-disruption alternative.

## Reusable (shareable)

| Path | What |
|---|---|
| `CLAUDE.md` | the behavioral contract |
| `settings.json` | hooks, permissions, model (no secrets; `settings.local.json` is machine-local and untracked) |
| `hooks/` | SessionStart hook and its fixture tests |
| `scripts/` | validators, secret scan, packaging |
| `docs/pedagogy/` | PAIR playbook, teaching progression |
| `docs/private-state.md` | this file |
| `skills/mentor/` | the mentor skill (generic; identical to the public repo) |
| `memory/convention.md` | ledger rules, no content |
| `README.md` | map of the repo and the review views |

`scripts/package-shareable.sh` zips exactly this list and refuses to run if a private path or a secret-pattern hit slips in.

## Private (never share)

| Path | Why |
|---|---|
| `memory/<topic>/*.md`, `*.history.md`, `memory/archive/` | concept cards carry incident narratives, cluster and resource names, internal architecture, security observations, access-control details |
| `memory/index.md`, `memory/independence.md`, `memory/solo.md` | derived from the above |
| `mentor/<project>/PLAN.md`, `JOURNAL.md`, `lessons/*.html` | company repos, app registration ids, hostnames, IP ranges, team names, access sequences |
| `projects/` | per-project working memory and transcripts (already untracked) |
| `docs/specs/` | design notes that reference real systems |

Rule for new files: anything that names a real customer, cluster, resource, host, address, account, or person goes under one of the private paths above. The `.gitignore` already ignores everything at the repo root by default and opts directories in deliberately; new private directories need no extra rule unless they are created inside an opted-in directory.

## Migration plan (when a split is wanted)

1. Create `claude-state-private/` (private repo) with `memory/`, `mentor/`, `docs/specs/`.
2. Keep `~/.claude` as the root; symlink `~/.claude/memory -> ../claude-state-private/memory` and `~/.claude/mentor -> ../claude-state-private/mentor`. Wikilinks stay basename-only so nothing breaks.
3. The hook and scripts already honour `CLAUDE_HOME` (hook) and `LEDGER_DIR` (link check); add the same override to any new tool so the state root is one variable.
4. Remove `memory/`, `mentor/`, `docs/specs/` from this repo's `.gitignore` opt-ins, commit, and let git history keep the old copies (no history rewrite).
5. Run `scripts/check.sh` and `scripts/package-shareable.sh`; the package must be byte-for-byte the same before and after.
