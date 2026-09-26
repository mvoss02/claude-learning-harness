# A Claude Code harness that keeps the reasoning yours

The benchmark is Mitchell Hashimoto's whiteboard defense: pulled aside at any moment, you can explain any system you shipped. Why X instead of Y, what a malicious actor gets, which data structure and why, where it fails. Not line-level. The load-bearing decisions.

This repo is the reusable part of my `~/.claude`: a behavioral contract, three hooks that enforce it, a spaced-repetition ledger convention, and a mentor skill. The private part (concept cards, mentor journals, project notes) is not here.

**The one principle:** I own the reasoning, Claude owns the motion. Anything that asks Claude to hold back is enforced by a mechanism, not by a paragraph of good intentions.

## What is in here

| Path | Role |
|---|---|
| `CLAUDE.md` | the contract: modes (PAIR, LEARN, SHIP), the build loop, the whiteboard defense, voice |
| `settings.json` | wires the hooks; model and plugin settings |
| `hooks/gate-investigation.py` | PreToolUse hook: denies Claude's own kubectl, helm, flux, az, psql, ssh, terraform, remote curl unless a hand-off flag exists. Claude proposes the command, you run it and read the output first |
| `hooks/session-start.py` | SessionStart hook: prints the current week, owned areas, due concept cards with their recall question, days since the last checkpoint |
| `settings.json` UserPromptSubmit hook | re-injects the contract on every message so it survives context compaction |
| `memory/convention.md` | the ledger: card format, five stages from encountered to transferable, promotion only on a model written from memory |
| `docs/pedagogy/` | the PAIR playbook (`microdoses.md`) and the teaching progression (`teaching.md`) |
| `docs/specs/2026-09-13-learning-system-rework.md` | why mechanisms instead of rules, with the research behind it |
| `skills/mentor/` | project-tier learning: plans, journals, lessons |
| `scripts/` | validators, link checker, secret scan, the packaging script that built this repo |

## How a session runs

1. Session start: the hook prints what is due. One card is asked at the first natural pause, as a generation question, never as a pop quiz.
2. A feature starts with a decision ledger. Claude lists the decisions, tags each load-bearing or incidental, and stops.
3. I call each load-bearing decision with one line of why. Claude argues where it disagrees, then builds that slice. Incidental decisions are Claude's, listed afterwards.
4. Investigation commands go through the gate: Claude proposes, I run with `! <cmd>`, I read the output before Claude interprets it.
5. Done means I answer the four whiteboard questions cold in chat. A blank answer means not done, however green the tests.
6. "SHIP this" in my words, and only mine, releases all of it. One stop survives: a one-screen brief of the load-bearing decisions before commit, and one of them asked back.

## Adopting it

- Copy `CLAUDE.md`, `settings.json`, `hooks/`, `scripts/`, `docs/`, `skills/mentor/`, and `memory/convention.md` into `~/.claude`.
- Replace "the learner" with your name in `settings.json` and the hooks. The name is only used in prose the hooks print.
- Create `memory/curriculum.md` (owned areas, topic tree, current week) and `memory/index.md`. The session-start hook degrades gracefully without them; `scripts/check.sh` expects them and will report them missing until they exist.
- Run `python3 hooks/test_session_start.py` and `python3 hooks/test_gate_investigation.py`. Both use synthetic fixtures.
- The gate's command list lives at the top of `hooks/gate-investigation.py`. Edit it to match your stack.

## What it costs

Slower on exactly the pieces that carry a decision. Searches, boilerplate, call-site updates, mechanical edits run at full speed. That is the trade.
