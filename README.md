# A Claude Code harness for getting better while building with AI

The goal is to grow into a Principal Engineer while building with AI every day. The benchmark is Mitchell Hashimoto's whiteboard defense: pulled aside at any moment, you can walk any system you built end to end. Why X instead of Y, where the source of truth is, what happens when a dependency fails or an actor is malicious.

This repo is the reusable part of my `~/.claude`: a behavioral contract, hooks that enforce it, a mistake log and a spaced-repetition ledger, and a mentor skill. The private part (my cards, mistakes, journals, project notes) is not here.

**The one principle: AI for speed on what you already own, your own hands for what you are trying to own.**

## Why it looks like this

The first version of this harness tried to make every AI-assisted work session also a learning session. After two months the evidence from my own journals said it did not work:
- AI-free practice was scheduled twice and never happened.
- The model asked cold, expert-level questions about material taught the day before.
- Explanations stacked analogies instead of showing the mechanism.
- The same wrong-layer mistakes kept coming back.

The research points the same way:
- **Anthropic, 2026.** Engineers learning a new library with AI scored 50% on a follow-up quiz, against 67% for those coding by hand. The gap was largest on debugging. People who used the AI only for conceptual questions and fixed their own errors scored about as well as the hand coders. ([Anthropic 2026](https://www.anthropic.com/research/AI-assistance-coding-skills))
- **Bastani et al., PNAS 2025.** Unrestricted AI answers during practice cost students 17% on the exam taken without AI. Hints did not.
- **Kalyuga et al. 2003, and Chen, Kalyuga & Sweller 2015.** New material with many interacting parts needs a worked example before any question. This is the expertise-reversal effect.
- **Metcalfe 2017.** A mistake stops repeating only when the wrong reasoning itself is worked through.

So version two splits the day in two:

| Track | How | What it is for |
|---|---|---|
| **Work** | PAIR: the AI implements heavily, you take every consequential decision, a 5-minute written explain-back closes each substantial session | speed, without losing the model of what you built |
| **Practice** | a 45 to 60 minute block: `/mentor` for new material, `/practice` for what you were taught, AI closed until your first attempt is written | getting better |

## Four modes, one dial

Every mode answers one question: who makes the first move, and for how long. Only PAIR starts without a typed command; the others are skills the model cannot invoke, so they never start from an inferred mood ("he seems in a hurry").

| Mode | First move | Scope |
|---|---|---|
| PAIR | shared | default: work |
| `/mentor` | you | learn new material: the AI teaches, you build, written gate |
| `/practice` | you | retrieve and apply what you were taught; AI closed until your attempt, no teaching |
| `/ship` | the AI | one task or problem; gate closed unless you write "gate open" |

Inside PAIR there are three words, never modes: go-ahead words build the agreed slice, `quick` skips your move for one message, "not today" declines a due card or the practice block. Words cover one message only: they never switch the mode, widen the scope, skip a consequential decision, or open the gate.

## What is in here

| Path | Role |
|---|---|
| `CLAUDE.md` | the contract: invariants, the five modes, the work loop, teaching rules, investigation, voice |
| `docs/pedagogy/teaching.md` | the teaching playbook: mechanism first on real artifacts, worked example → completion → independent, questions by the age of the material, stall diagnosis, debugging loop |
| `memory/mistakes.md` | template: one row per mistake, in your words: what you thought, why it was wrong, the repair, the layer, the next revisit date |
| `memory/layer-map.md` | template: process → runtime → syscall → kernel → wire → remote, plus orchestrator, control plane and data store, with who owns which state. Every new concept is placed here first |
| `memory/experiment.md` | template: a six-week experiment with metrics (practice blocks, repeat rate, a timed cold build, explain-back grades, work speed) and a decision rule. The rules stay frozen while it runs |
| `memory/convention.md` | the card ledger: five stages from encountered to transferable, promotion only on a model written from memory |
| `hooks/session-start.py` | prints the current week, due mistake rows and cards, practice blocks in the last 7 days, days since the last checkpoint |
| `hooks/gate-investigation.py` | denies the AI's own kubectl, helm, flux, az, psql, ssh, terraform and remote curl unless a hand-off flag exists. The AI proposes the command; you run it and read the output first |
| `settings.json` | wires the hooks. Its UserPromptSubmit hook re-injects the contract on every message so it survives context compaction |
| `skills/practice/`, `skills/ship/` | the typed modes besides `/mentor`: a retrieval block that logs itself; one bounded task or problem at full speed, gate closed by default, a fixed bug logged as a record. The model cannot invoke any of them |
| `skills/mentor/` | project-tier learning: plans, chat-first lessons, written gates, journals |
| `scripts/` | validators, link checker, secret scan, the packaging script that built this repo |

## How a day runs

1. **Session start.** The hook prints what is due. One item, a mistake row or a card, is asked at the first natural pause, as a generation question.
2. **Work.** Small units, bottom-up. On a consequential decision the AI asks what you lean toward, or gives at most two options with a recommendation. Then it builds fast. Routine choices it makes silently.
3. **Investigation.** You choose the evidence, the AI supplies the exact command, you run it with `! <cmd>` and say what the raw output means before the AI weighs in.
4. **`/ship`.** When you need speed on one task or problem, the AI takes it, with no questions and no teaching detours. The gate stays closed unless you wrote "gate open", so you approve commands with "run it". A fixed bug is logged as a record, symptom → cause → fix, that counts for repeats but is never quizzed. Then it is PAIR again.
5. **Teaching.** The mechanism is shown on a real artifact (an `strace` line, a packet, a plan header), not an analogy. Then a worked example, then a half-finished problem, then one you do alone. Anything taught less than three days ago only gets a "say it back", never a cold question.
6. **End of session.** You write a five-minute explain-back without looking; the AI reviews it.
7. **Practice block.** `/mentor` when the material is new (the AI teaches, you build); `/practice` when it was taught (a DSA pattern, a design mini, a rebuild of a due mistake). The AI stays closed until your first attempt is down, then reviews it, and the block logs itself.

## Adopting it

- Copy everything into `~/.claude`.
- Replace "the learner" with your name in `settings.json` and the hooks. It only appears in prose the hooks print.
- Fill in `memory/experiment.md` (dates, practice repo) and delete the example row in `memory/mistakes.md`.
- Create `memory/curriculum.md` (owned areas, topic tree, current week) and `memory/index.md`. The hook degrades gracefully without them; `scripts/check.sh` reports them missing until they exist.
- Run `python3 hooks/test_session_start.py` and `python3 hooks/test_gate_investigation.py`. Both use synthetic fixtures.
- Edit the gate's command list at the top of `hooks/gate-investigation.py` to match your stack.

## What it costs

About an hour a day of slower, AI-free first attempts, plus five minutes of writing at the end of a work session. Everything else runs at full AI speed. Whether that trade pays off is what `experiment.md` is for: measure it, do not trust the feeling. Experienced developers in [METR's 2025 study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) were 19% slower with AI while believing they were 20% faster.
