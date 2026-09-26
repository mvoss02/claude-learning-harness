# Phase: Wrapup

Goal: persist what was actually learned (not what was written); prime the next session. Brief.

## Steps (in order)

1. **Wrap questions, then teach-back.** What did you learn, what is still unclear, what would you struggle to rebuild tomorrow, what surprised you. Then the last substantive act of the session is the learner generating something: they teach the session's one important model back with files and lesson closed, and answer two naive follow-ups ("why does it have to be that way?", "what would go wrong if not?"). Periodically, for concepts at `practiced` or above with some spacing, make this a written summary in their words; it becomes "My model" on the card. Never end a session on reading.
2. **Concept cards.** For each concept touched: ledger present → create/update per `~/.claude/memory/convention.md`; else `STATE_DIR/concepts/` per `references/concept-card-format.md`. Stage by evidence only: taught today → `introduced` (after a say-back); used with guidance → `practiced`; cold-recalled unaided in a LATER session → `retrievable`; transferred → `transferable`. A miss is classified (central / peripheral) before it counts. Claude's explanation is labeled as Claude's. Never promote because the notes are good.
3. **Independence.** One journal line: which parts of today's work the learner did that the mentor used to do, level 0 to 4 for the milestone. `~/.claude/memory/independence.md` gets at most one line per capability, only when scaffolding changed or meaningful evidence appeared. Say what scaffolding fades next time.
4. **Journal** per `references/journal-format.md`; set the milestone state in PLAN.md (`gate-pending` if the deliverable is done but not demonstrated).
5. **Next step**, one line: milestone, phase, format (project / lab / transfer), whether a `gate-pending` demonstration opens the next session, and what the learner could attempt cold before then (a checkpoint problem for the next session, per `~/.claude/memory/checkpoints/checkpoints.md`, only when it fits).

## All milestones passed?

Run the retrospective instead of step 5:
- Rebuild exercise: learner re-derives the architecture from scratch, verbally: components, data flow, trade-offs, what they would change.
- Transfer: one meaningfully different scenario using the plan's core concepts, minimal framing. Feeds the ledger (`transferable` only if passed).
- Review the mission against the finish line: achieved? Natural next mission?
- Close the plan (status: completed) and name soberly the two or three hardest things they now own.
