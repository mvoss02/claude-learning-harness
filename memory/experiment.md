---
name: experiment
description: "Six-week learning experiment: Work/Practice split, mechanism-first teaching, mistake log, layer map. Metrics, baselines, weekly check, decision rule. Rules are frozen until it ends."
metadata:
  type: project
---

# Learning experiment, <start> → <start + 6 weeks>

**Question.** Does the Work/Practice split plus mechanism-first teaching make me retain concepts and stop repeating mistakes, without costing the speed I get from AI?

**Changes under test.**
- The daily practice block, AI closed until my first attempt is written.
- Mechanism-first teaching with worked example → completion → independent.
- `mistakes.md` as the main retrieval source.
- `layer-map.md`.
- A written explain-back at the end of substantial sessions.
- "Not today" for speed.

**Practice repo.** `<path to the repo where practice blocks happen>`

**Frozen.** No changes to CLAUDE.md, `docs/pedagogy/teaching.md` or the mentor skill until <end date>, except bug fixes. Ideas go in "Parked" below.

## Metrics

| Metric | How | Baseline | Wk 3 | Wk 6 |
|---|---|---|---|---|
| Practice blocks done / skipped | the practice log below | n/a | | |
| Repeat rate | REPEAT rows ÷ new rows in `mistakes.md` that period | | | |
| Cold build | one small build from a blank editor, no AI, docs allowed, timed; note every stall | | | |
| Explain-backs | grade each: unaided / nudged / wrong layer | n/a | | |
| Work speed | rough count of shipped work items per week, my judgment | | | |

**Decision rule at week 6.**
- If the repeat rate and cold build time haven't improved: raise the share of hand coding.
- If work speed dropped noticeably: shrink the practice block.
- If both improved: keep it, and unfreeze the rules for targeted changes only.

## Weekly check (5 minutes)

Blocks done/skipped, new and repeat rows, one sentence on how it felt.

## Practice log

Format: `- YYYY-MM-DD done|skipped <what, 1 line>` (the session-start hook counts the last 7 days)

## Parked ideas
