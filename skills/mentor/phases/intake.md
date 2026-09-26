# Phase: Intake

Goal: co-author PLAN.md. No teaching, no lessons yet.

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
3. **Size the mission** (`references/learning-tree.md`, "Mission sizing") from horizon and breadth: small (one or two sessions), medium (several sessions or weeks), large (broad, multi-month). Say the size and what research it buys in one line; the learner can override.
4. **Research proportionally.** Small: repo/context audit, official docs, a one-breath solution-space orientation. Medium: official path, repo audit, solution-space map, prerequisite check. Large: the full parallel fan-out plus a prerequisite graph. Use subagents when available; when they are not, when web access is down, or when the mission already carries enough context, do the reduced version in your own context and say so.
5. **Ledger and curriculum check.** If `~/.claude/memory/convention.md` exists, read the ledger index for this topic. `retrievable`/`transferable` → skip or compress; `introduced`/`practiced` → plan a short refresh, not a re-teach; `encountered` → treat as new ground. Then map the mission's concepts to nodes in `~/.claude/memory/curriculum.md`: a mission on an owned area or a curriculum node gets reviewed cards and may supply checkpoint problems; a mission off the curriculum (tooling, a language the roadmap excludes) is legitimate but says so in the plan, and its new concepts become field notes (`memory/notes/`) or `curriculum: off` cards that are never reviewed. Say which in one line; the learner can override.
6. **Synthesize.** Merge results, keep prerequisite edges, cross with mission and repo anchors, cut what the mission does not need (each cut with a reason). Milestones are real deliverables in the learner's repo: roughly one for small, three to five features for medium, four to seven for large, preceded by small explicit units when the technology is new to the learner (`references/progression.md`). Count each unit's unknowns; early units carry one or two. State the finish line in one sentence with its evidence list. Numbers bend to the work, not the other way round. Where setup, access, or tooling is itself a capability the learner chose to own, or the run → observe → fix loop is the thing being trained, say so in that milestone's deliverable line.
7. **Draft PLAN.md** per `references/plan-format.md`.
8. **Learner's own map first (one rep, before the plan is shown).** "You've named the mission. In 3 or 4 chunks, what do you think this topic consists of, and what would you learn first?" Take the answer as is; no hints. Blank-page framing, the most honest baseline intake produces. Journal it verbatim. For a small mission this can be one sentence.
9. **Walk the learner through what is ahead.** Open with the comparison: what their map had right, what it missed, why the order differs. Then tree (or the short list, for small missions), milestones, cuts, capabilities, neighbourhood, sources, first transfer opportunity. Detailed enough to object to specifics; for a small mission, one screen. Invite pushback, revise, then ask for explicit approval. No milestone starts until they approve; record the approval and changes in the journal.
10. **Journal** the session per `references/journal-format.md`, including the learner's own map, the mission size, which research ran, and the sources surfaced.

## Guardrails

- Interview before audit conclusions: do not prescribe a curriculum the mission doesn't need (YAGNI applies to learning plans too).
- The first unit must be completable in one session and carry one unknown. Early wins compound; early overload compounds faster.
- Research feeds; the mentor decides; the learner approves. Never paste agent output raw into the plan; never start teaching on an unapproved plan.
- A small mission never triggers the large-mission process. If it grows, re-size at a session boundary and journal it.
