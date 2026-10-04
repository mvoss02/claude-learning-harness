# A Claude Code harness that keeps the reasoning yours

The goal is to grow into a Principal Engineer while building with AI every day: the AI may write most of the code, the engineering judgment stays yours. The benchmark is Mitchell Hashimoto's whiteboard defense: pulled aside at any moment, you can walk any system you built end to end. Why X instead of Y, where the source of truth is, what happens when a dependency fails or an actor is malicious. Not line-level. The load-bearing decisions.

This repo is the reusable part of my `~/.claude`: a behavioral contract, three hooks that enforce it, a spaced-repetition ledger convention, and a mentor skill. The private part (concept cards, mentor journals, project notes) is not here.

**The one principle:** I own the reasoning, Claude owns the motion. PAIR is the permanent default; SHIP exists only inside an explicit `/ship` command and ends with its task.

## What is in here

| Path | Role |
|---|---|
| `CLAUDE.md` | the contract: ten invariants, modes (PAIR, LEARN, SHIP), the Frame → Decide → Build → Trace → Continue loop, retrieval eligibility, voice |
| `skills/ship/` | the `/ship` command: the only entry into SHIP. States its scope, executes, summarizes, returns to PAIR. The model cannot invoke it |
| `settings.json` | wires the hooks; model and plugin settings |
| `hooks/gate-investigation.py` | PreToolUse hook: denies Claude's own kubectl, helm, flux, az, psql, ssh, terraform, remote curl unless a hand-off flag exists (`/ship`, or "run it" for one proposed command). Claude proposes the command, you run it and read the output first |
| `hooks/session-start.py` | SessionStart hook: prints the current week, owned areas, due concept cards with their recall question, days since the last checkpoint |
| `settings.json` UserPromptSubmit hook | re-injects the contract on every message so it survives context compaction |
| `memory/convention.md` | the ledger: card format, five stages from encountered to transferable, promotion only on a model written from memory |
| `docs/pedagogy/` | the PAIR playbook (`microdoses.md`) and the teaching progression (`teaching.md`) |
| `docs/specs/2026-09-13-learning-system-rework.md` | why mechanisms instead of rules, with the research behind it |
| `skills/mentor/` | project-tier learning: plans, journals, lessons |
| `scripts/` | validators, link checker, secret scan, the packaging script that built this repo |

## How a session runs

1. Session start: the hook prints what is due. One card is asked at the first natural pause, as a generation question, never as a pop quiz.
2. Work moves in small units, bottom-up: one new capability or system boundary at a time. Nothing is built because the mature system will probably need it.
3. Each unit runs Frame → Decide → Build → Trace → Continue. On a consequential decision Claude asks what I am leaning toward, or gives at most two options with a recommendation, and does not build before I have weighed in. Routine, reversible implementation decisions Claude makes silently; one is surfaced only when it is surprising, hard to reverse, or changes my model of the system.
4. Claude then implements heavily. Before the next unit I reconstruct the one or two things that matter (where input enters, where state lives, what fails), and Claude fills the gaps with a `file:line` map.
5. Investigation keeps the loop hypothesis → evidence choice → observation → interpretation with me: I choose the evidence, Claude supplies the exact command, I run it with `! <cmd>`, read the raw output, and say what it means before Claude weighs in. A gate hook backs this up. Routine commands Claude just runs.
6. I am only ever tested on what I decided, reasoned through, or learned. What Claude built alone is explained, not asked.
7. `/ship <task>` hands over one bounded task at full speed. It ends with a summary and returns to PAIR by itself. "Do it" and "sounds good" never count as `/ship`.

## Adopting it

- Copy `CLAUDE.md`, `settings.json`, `hooks/`, `scripts/`, `docs/`, `skills/mentor/`, `skills/ship/`, and `memory/convention.md` into `~/.claude`.
- Replace "the learner" with your name in `settings.json` and the hooks. The name is only used in prose the hooks print.
- Create `memory/curriculum.md` (owned areas, topic tree, current week) and `memory/index.md`. The session-start hook degrades gracefully without them; `scripts/check.sh` expects them and will report them missing until they exist.
- Run `python3 hooks/test_session_start.py` and `python3 hooks/test_gate_investigation.py`. Both use synthetic fixtures.
- The gate's command list lives at the top of `hooks/gate-investigation.py`. Edit it to match your stack.

## What it costs

Slower on exactly the pieces that carry a decision, and one unit at a time instead of the whole system at once. Implementation, searches, boilerplate, and mechanical edits run at full speed. That is the trade.
