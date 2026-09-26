# Phase: Review (hard gate)

Goal: decide the milestone's gate state against the rubric. SKILL.md "Gates" applies in full.

## Steps (in order)

1. **Read `references/rubric.md` and the milestone's `*.reference.md` now**, before looking at the work. Restate the three pass conditions so the bar is visible before the verdict; the reference supplies the required behaviour, invariants, and design families to review against, and the properties a good gate answer contains.
2. **Read the actual work.** Real diff/files in the learner's repo. Never review from their description.
3. **Code review.** Findings ranked by consequence: correctness, security, reliability, maintainability. What is wrong, why, consequence, better alternative. No style trivia. Design is judged against the reference's behaviour, invariants, and trade-offs: a different but valid design gets "valid; optimises for X, introduces Y" and a trade-off discussion, never "not the intended structure". Reject a design only for a violated invariant, requirement, safety property, or an agreed learning constraint, and name it.
4. **Oral exam**, minimum three questions, unaided, in this session, calibrated to what was taught and demonstrated in this milestone (no questions about concepts merely encountered, no trivia about flags or API names):
   - Explain-back: walk me through what you built and why it works. Prefer reconstruction from the original problem over recitation of the lesson.
   - One prediction question ("what does X print if we do Y?").
   - "What breaks first?" and its consequence.
   A wrong answer is diagnosed (which piece is missing) before it is graded; a wrong answer caused by something never taught is a gap in the plan, not the learner, and is journaled as such.
5. **Verdict**, one of the gate states in `references/rubric.md`: `passed` when all three axes hold (note "with guidance" in the journal if reactivation was needed; concepts then stay `practiced`); `needs-revisit` when a demonstration showed a real gap, with a concrete list: what is missing, what demonstrating it looks like; `gate-pending` when the demonstration did not happen (session ended, learner deferred), which is not a failure. Say the state plainly.
6. **Ledger and journal.** Concepts demonstrated unaided here become `practiced` (same-session, so not `retrievable`; that needs a later cold recall). Set review dates. Record independence level for the milestone (0 to 4) in the journal and, if the milestone belongs to a chosen capability and the scaffolding actually changed, one line in `~/.claude/memory/independence.md` (at most one per capability per session). Note a transfer scenario per major concept as its "Next useful step" so a later session can run it. On `passed`: mark it in PLAN.md, route to `phases/wrapup.md`. On `needs-revisit` or `gate-pending`: record the state (and the list); next session opens with the demonstration or the gap list.

## Guardrails

- "Can we do the questions next time?" → `gate-pending`; the milestone is not passed and not failed; the demonstration opens the next session, and a spaced demonstration is often better evidence.
- Exam answers come without notes or file-peeking. Peeking converts the question into a new one.
- Do not escalate difficulty because the first answers were good; the gate tests the milestone's model, not the learner's ceiling.
