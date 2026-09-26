# Milestone review rubric

Pass requires ALL THREE, demonstrated with evidence:

1. **Works.** The deliverable exhibits the required behaviour and preserves
   the invariants in the milestone's reference (or, for an early unit, its
   definition of done), verified against the real repo: run it, test it.
2. **Understood.** Unaided explain-back, without notes or file-peeking,
   ideally reconstructing from the original problem rather than reciting
   the lesson; plus at least one correct prediction.
3. **Failure-aware.** "What breaks first?" answered with a real failure mode
   and its consequence.

Grade each axis: strong | adequate | gap.

**Fourth axis, checked later: Transferred.** Same concept, different surface,
little framing, spaced. Not part of the gate; scheduled via the ledger and
the plan's transfer sessions. Passing it moves the concept to `transferable`.

## Design evaluation

Judge against the reference's **behaviour, invariants, and trade-offs**, not
against any shape the mentor had in mind. A design that satisfies them is
valid even if the mentor would have built it differently: "valid; it
optimises for X and introduces Y", then discuss the trade-off. Reject only
for a violated invariant, requirement, safety property, or an agreed
learning constraint, and say which. Never "not the intended structure".

## Gate states

| State | Meaning |
|---|---|
| `gate-pending` | Deliverable done or nearly done; the demonstration has not happened yet (session ended, learner deferred). Not a failure; a spaced demonstration is often stronger evidence. |
| `passed` | All three axes held. If reactivation or hints were needed, note "with guidance" in the journal; concepts then stay at `practiced` until an unaided demonstration. |
| `needs-revisit` | A demonstration showed a gap in the central model or the behaviour. Recorded as what it was, with a concrete list: what is missing, what demonstrating it looks like. The list is the next agenda. |

Rules: questions calibrated to what the milestone taught and the learner
demonstrated; no trivia, no concepts merely encountered, no escalation
because early answers were good. Answers without notes or file-peeking.
Effort, confidence, and time pressure are not axes. A wrong answer is
diagnosed before it is graded; if the missing piece was never taught, that
is a plan gap: journal, teach, re-ask. No failure language because a
session ended.
