# Milestone reference format (mentor-private)

`STATE_DIR/lessons/NNNN-<slug>.reference.md`, one per feature milestone
(`Stage: middle | later`), written at lesson time, read in build and review,
never shown, pasted, or quoted to the learner. Early units get at most five
lines (definition of done, two or three misconceptions) or none: a full
reference for a one-session unit is ceremony.

Purpose: a fixed target for hints and a catalogue of known mistakes
(embedded-solution and mistake-catalogue guardrails, Bastani 2025, Kestin
2025). The target is a set of **evaluation boundaries**, not an intended
implementation. The mentor evaluates "does the learner's design satisfy the
behaviour, invariants, and trade-offs?", never "did they rediscover my
architecture?".

## Do not write

- an intended package layout, exact function signatures, an expected
  interface or type structure, an implementation sequence, or one preferred
  architecture presented as the answer

unless the task genuinely has one correct implementation (rare: a protocol
byte layout, a spec-mandated algorithm). Even then, mark it as the spec's
constraint, not the mentor's preference.

## Sections

```markdown
# <Milestone> reference (mentor-private)

## Required behaviour
What the deliverable must do, observable from outside. Inputs, outputs,
failure behaviour, definition of done in behavioural terms.

## Invariants
What must remain true regardless of design: security properties, data
integrity, idempotency, "the key never leaves the process", "no goroutine
outlives its request".

## Acceptable design families
At least two when they genuinely exist (concrete dependency vs interface
boundary; sync vs async; repository package vs direct persistence; library
vs hand-rolled mechanism; channels vs mutex). For each: what it optimises
for, what it introduces, when it fits the current learning goal. The mentor
may prefer one for this milestone; the preference is stated with its
trade-off, never as the answer.

## Trade-offs the learner should be able to discuss
The two or three decisions where a reasonable engineer could go either way.

## Failure modes to test or break on purpose
What a good implementation guards against; the breakage experiments.

## Common misconceptions
Symptom → which weak mental model it reveals → direction of repair (not
the fix). Mistakes already made by this learner, dated, with the repair.

## Evaluation criteria
How correctness and understanding are judged without requiring one
architecture. Gate questions with the *properties* a good answer contains,
not a model answer to match.

## Optional reference implementation
Only when a worked example is pedagogically useful, in a toy domain or
clearly marked "one example, not the canonical answer". Never the
deliverable itself.

## Reference gaps
Appended as the build reveals traps or design families that were missing.
```

## Review language

- "This is a valid design. It optimises for X and introduces Y." Then the
  trade-off discussion.
- Reject only for a violated invariant, requirement, safety property, or an
  explicit learning constraint the learner agreed to (e.g. "stdlib only in
  this lab"). Say which one.
- Never "that is not the intended structure".
