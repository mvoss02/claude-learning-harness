# Progression: granularity, unknowns budget, formats, finish line

The plan is a progression, not a syllabus. Its shape changes as the learner
grows: fine-grained and explicit at the start, combined in the middle,
ambiguous and independent at the end.

## Adaptive milestone granularity

| Stage | Unit shape | What the learner is doing |
|---|---|---|
| **Early** (new language, stack, or domain) | Small, focused units: one central mental model, one small piece of syntax or tooling, one guided application, one short independent application. A unit is one or two sessions. | Acquiring vocabulary, syntax, runtime model, tooling, code-reading and debugging habits at the same time. Each unit isolates one of them. |
| **Middle** | Guided features that combine previously introduced ideas into something the project needs. | Integrating: the concepts are known, the composition is new. |
| **Later** | Larger, ambiguous tasks: independent framing, decomposition, design, debugging. | Owning the work; the mentor reviews and unblocks. |
| **Transfer** | A different small problem, minimal framing. | Proving the concept, not the repository, was learned. |

`small explicit units → combined guided features → larger independent features → transfer`

Smaller early units are not a lower standard. Their purpose is to remove
extraneous load so the learner struggles with the concept that matters. An
early unit that takes forty minutes and ends with the learner able to explain
one runtime model is a full unit. Do not merge early units to "get to the real
work"; they are the real work. Do not let a unit become trivial either: each
one ends with an independent application the learner could not have done
before it.

## Unknowns budget

Before defining a milestone, unit, or exercise, count the major unfamiliar
dimensions it combines. Major dimensions (each counts as one when the learner
has no evidence on it):

- language syntax or semantics · an unfamiliar standard-library area · a
  protocol (HTTP, OAuth, a bank API) · cryptography · concurrency ·
  persistence · package architecture and dependency direction · a testing
  style · unfamiliar tooling · unfamiliar domain logic

Budget: early units carry **one**, at most **two** if the second was taught
first. Middle-stage features may combine several *known* dimensions and one
new one. Later-stage tasks are allowed to be ambiguous on purpose.

Over budget → do one of: split the exercise; teach a prerequisite first;
give a worked example for one dimension so only the other is struggled with;
move one dimension into a focused lab. The diagnostic question in every
stall: *is the learner struggling with the intended concept, or drowning in
several unrelated unknowns?* The second is not productive struggle; it is a
planning error, journaled as such.

Record the count in PLAN.md (`Unknowns:` per unit) so the plan shows its own
load, and re-count when the learner's stage changes.

## Three formats

The project is the spine. Not every concept is best met inside
production-shaped code.

| Format | When | Shape |
|---|---|---|
| **Project session** | Default. Concepts are known enough to be composed. | Advance the real application: authentic architecture, integration, debugging, design decisions. |
| **Focused lab** | The project has too many moving parts around one mechanism, or a mechanism deserves isolation (slice aliasing, pointer vs value receivers, interface satisfaction, context cancellation, channel closure, mutex vs channels, JSON decoding failures, HTTP timeouts, the race detector, profiling). | 20 to 40 minutes, a throwaway directory or `_lab/`, predict → run → break → explain. Returns to the project with a sentence on where the mechanism lives there. |
| **Transfer session** | Later, spaced, for concepts at `practiced` or above. | Same concept, different small problem (a concurrent URL checker, a webhook delivery worker, a small inventory API, a rate-limited job processor, a log aggregation pipeline), minimal framing, docs allowed. Evidence for `transferable`. |

The project proves integration. The lab clarifies mechanism. Transfer tests
whether the concept was learned rather than one repository memorised.

## Momentum versus depth

When project progress and learning depth conflict, say so and offer the
choice: "we can ship this with the library now and study its internals in a
lab, or slow down here and implement the mechanism ourselves." The learner
chooses; the decision is recorded (decision / alternatives / why /
tradeoffs). The mentor never optimises for finishing milestones fastest, and
never manufactures difficulty to prolong the journey. The project has to stay
interesting and useful.

## Finish line

Every plan states a first-stage outcome in one sentence and the evidence
that would show it, so the learner and mentor can tell when the mission is
done rather than merely when the milestone list is empty. Shape:

> I can independently design, implement, test, debug, and explain a
> <medium-sized thing in this technology> using documentation, without an LLM
> framing the problem for me.

Evidence is a list of demonstrable acts (start from a blank repo, choose a
structure, model data and errors, write useful tests, read unfamiliar code,
use tooling productively, explain trade-offs, complete a transfer project
with little scaffolding). Framed as "independently capable at a meaningful
project scale", never as mastery of the whole technology.

## Early testing

Tests appear in the earliest units, not as a late correctness gate: pure
functions and table-driven tests first, then JSON round trips, expected
error cases, `httptest`-style boundaries, the race detector later, fuzzing
where it teaches something. A test is a way to state the model ("this input
must produce this"), and predicting what will pass or fail is a legitimate
prediction drill once the model is taught.
