# Phase: Intake

Goal: co-author PLAN.md. No teaching, no lessons yet. Sizing, research, synthesis and the approval walkthrough are specified in `references/learning-tree.md`; this file is the order of steps.

## Steps (in order)

1. **Sparring interview.** One question at a time, wait for each answer:
   - Why this technology? What should exist at the end that doesn't today?
   - Current level: what have they already used or read? Probe one answer with a follow-up to calibrate depth honestly.
   - Prerequisite probe, not self-report: 3 to 5 concrete questions on the fundamentals every milestone will lean on (for a language: its runtime model, its memory/value semantics, its error handling, its module layout; for infra: the primitive under the abstraction). Intuition-level questions only; nothing is graded, the answers set the starting stage. "Tutorial done" is a self-report, not evidence.
   - Interference map, when the learner is expert in a neighbouring technology: the 4 to 6 places where the old model gives the wrong answer in the new one ("Python says X, Go says Y"). Goes into the baseline; each becomes a predict-from-the-old-model moment later.
   - Time budget per week, target horizon.
   - Which capabilities they want to OWN at the end (framing, navigation, design, debugging, implementation, and whether the execution loop itself is one of them) vs merely operate. These become the independence-tracked areas.
   - Ownership: by default the learner writes the code that teaches and the mentor may write scaffolding on request; ask whether any concepts should be `drill` (learner types every line) and note them per milestone.
2. **Name the topic** explicitly with the learner in one sentence ("Learn Terraform deployments on Azure by putting this cluster under IaC").
3. **Size the mission** (`references/learning-tree.md`, "Mission sizing") from horizon and breadth. Say the size and what research it buys in one line; the learner can override.
4. **Research proportionally** per the sizing table; fan-out and fallback in `references/learning-tree.md`.
5. **Ledger and curriculum check.** If `~/.claude/memory/convention.md` exists, read the ledger index for this topic. `retrievable`/`transferable` → skip or compress; `introduced`/`practiced` → plan a short refresh, not a re-teach; `encountered` → treat as new ground. Then map the mission's concepts to nodes in `~/.claude/memory/curriculum.md`: a mission on an owned area or a curriculum node gets reviewed cards and may supply checkpoint problems; a mission off the curriculum (tooling, a language the roadmap excludes) is legitimate but says so in the plan, and its new concepts become field notes (`memory/notes/`) or `curriculum: off` cards that are never reviewed. Say which in one line; the learner can override.
6. **Synthesize** per `references/learning-tree.md`, "Synthesis": merge, keep prerequisite edges, cross with mission and repo anchors, cut with reasons, build milestones as real deliverables in the learner's repo with small explicit units first when the technology is new, count unknowns, state the finish line with its evidence list. Numbers bend to the work, not the other way round.
7. **Draft PLAN.md** per `references/plan-format.md`.
8. **Learner's own map first (one rep, before the plan is shown).** "You've named the mission. In 3 or 4 chunks, what do you think this topic consists of, and what would you learn first?" Take the answer as is; no hints, no correction yet. Approving a plan someone else built is recognition; producing a map first is the framing rep the whole system exists to protect, and the most honest baseline intake produces (stronger than the interview's self-report). Journal it verbatim; it goes into the plan's baseline. For a small mission this can be one sentence.
9. **Walk the learner through what is ahead** per `references/learning-tree.md`, "Walkthrough for approval": comparison with their map first, then the rest of the list, compressed for a small mission. Invite pushback, revise, then ask for explicit approval. No milestone starts until they approve; record the approval and changes in the journal.
10. **Journal** the session per `references/journal-format.md`, including the learner's own map, the mission size, which research ran, and the sources surfaced.

## Guardrails

- Interview before audit conclusions: do not prescribe a curriculum the mission doesn't need (YAGNI applies to learning plans too).
- The first unit must be completable in one session and carry one unknown. Early wins compound; early overload compounds faster.
- Never start teaching on an unapproved plan.
- A small mission never triggers the large-mission process. If it grows, re-size at a session boundary and journal it.
