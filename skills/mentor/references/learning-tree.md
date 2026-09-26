# Learning tree: research sized to the mission

Planning is logistics, so it gets zero learner struggle and proportional mentor effort. At intake the mentor sizes the mission, researches accordingly, merges the results into a plan, and walks the learner through what is ahead before anything is taught.

## Mission sizing

| Size | Expected duration | Research | Milestones | Approval |
|---|---|---|---|---|
| **small** | one or two sessions | repo/context audit; official docs for the one or two concepts; one-breath solution-space orientation | one milestone or exercise | one-screen walkthrough, explicit yes |
| **medium** | several sessions or weeks | official path, repo audit, solution-space map, prerequisite check | about three to five | walkthrough below, compressed where nothing is at stake |
| **large** | broad, multi-month capability | full parallel fan-out (below), prerequisite graph, cuts | about four to seven | full seven-point walkthrough |

Numbers are guidance, not quotas. Size by horizon and breadth from the interview; say the size out loud; the learner can override; re-size at a session boundary if the mission grows or shrinks, and journal it.

**Fallback.** When subagents are unavailable, web access is down, or the mission already carries enough context (a known repo, a topic the ledger already covers, a learner who brought the curriculum), do the reduced research in your own context and say so in the journal. Never block intake on tooling.

## Fan-out (large missions; medium missions pick the rows they need)

Spawn with the Agent tool, in one message, all read-only. Each agent gets the topic sentence agreed with the learner, the mission text, and the output schema below. None of them writes files.

| Agent | Type | Job |
|---|---|---|
| **official-path** | general-purpose (web) | Official docs' own learning sequence for the topic; current stable version; deprecations and recommended practice; one primary-source link per concept. |
| **community-curricula** | general-purpose (web) | 2 to 3 respected roadmaps, courses, or books for the same topic; how experienced people order it; concepts they insist on early; common pitfalls and misconceptions. |
| **repo-audit** | Explore (read-only) | The learner's repo: structure, tooling already present, what is manual today, 3 to 5 concrete artifacts (paths, resource names) the curriculum can anchor to, anything already done that the plan can build on or must not break. |
| **solution-space** | general-purpose (web) | The neighbourhood: which tool families sit next to this technology, what each replaces or competes with, when an engineer would choose differently. Feeds toolbox awareness and the "cut" list. |
| **prerequisites** (large only) | general-purpose | What must already be known before concept X makes sense; mapped against the learner's baseline from the interview. |

## Output schema (every agent returns this, nothing else)

```markdown
## Concepts
- <concept slug> | why it matters for this mission | prerequisites: <slugs or none> | source: <one link> | hook: <one sentence a learner remembers>
## Ordering notes
- <how this source orders things and why>
## Pitfalls
- <misconception or trap, one line each>
## Cuts suggested
- <concept> | why the mission does not need it
```

Repo-audit replaces "Concepts" with "Anchors" (path | what it is | which concept it can ground) and "Already present" (tooling, state, things to preserve).

## Synthesis (mentor, in its own context)

1. Merge and dedupe concepts across sources. Keep the prerequisite edges; they become the tree's structure (a small mission may end up with a flat list; that is fine).
2. Check the ledger (`~/.claude/memory/index.md`) for each concept: `retrievable`/`transferable` → compress or skip; `introduced`/`practiced` → short refresh; `encountered` or missing → new ground.
3. Cross with the mission and the repo anchors. Everything that does not serve the mission goes to the cut list with a reason; cuts are decisions, not oversights.
4. Build the milestones: deliverables cut along the tree, count per the sizing table, granularity by stage (`references/progression.md`): when the technology itself is new to the learner, the first milestones are small explicit units (one model, one piece of syntax or tooling, a guided and an independent application each), then features that combine them, then ambiguous work, then transfer. Count the unknowns of every unit and feature (`Unknowns:` in PLAN.md); an early unit over one or two is split, or one dimension goes to a lab or gets a worked example. Primitive-first where the primitive is cheap; a primitive that stacks unknowns (crypto plumbing in a new language) goes to a lab while the project uses the library.
   - **Ownership, in the deliverable line.** Setup, access, and tooling are normally cleared by the mentor at zero friction; when one of them is itself a capability the learner chose to own, or when the run → observe → fix loop is the thing being trained, or when the learner wants to type every line (`drill`), say so in that milestone's deliverable line. Name the reasoning move the learner owns when one is singled out.
5. Record the tree or list in PLAN.md (`references/plan-format.md`) and the sources in the journal.

## Learner's map before the plan (one rep)

Before showing anything, ask once: "In 3 or 4 chunks, what do you think this topic consists of, and what would you learn first?" No hints, no correction yet. Approving a plan someone else built is recognition; producing a map first is the framing rep the whole system exists to protect. Their answer is journaled verbatim and becomes baseline evidence (stronger than the interview's self-report). For a small mission one sentence is enough.

## Walkthrough for approval (required before any teaching; compress for small missions)

Present in chat, in this order, detailed enough that the learner can object to specifics:

0. **Comparison** with their map: what they had right, what they missed, why the order differs. Respond to their reasoning first.
1. **The tree** (or list), area by area: which concepts, in which order, and why that order.
2. **Milestones**: stage and format, deliverable, the concepts it teaches, its unknowns count, what the repo looks like after it. Say why the early units are small and where the first combined feature sits.
2b. **Finish line**: the one-sentence outcome and its evidence list.
3. **Cuts** and the reason for each. Ask: "anything here you actually want back in?"
4. **Capabilities owned at the end** (from the interview) and which milestone grows each.
5. **Neighbourhood** in three sentences: what sits next to this technology and when one would choose differently.
6. **Sources**: the primary source plus the best curriculum found, with links.
7. **First transfer opportunity**: the earliest point at which the learner could do something alone (a checkpoint, `~/.claude/memory/checkpoints/checkpoints.md`, or a piece of real work done with minimal framing).

Then ask for approval explicitly. Pushback edits the plan; no milestone starts until the learner says the plan is theirs. Record the approval date and any changes in the journal.

## Guardrails

- Research feeds; the mentor decides. Never paste agent output raw into the plan.
- Claims about versions, defaults, and deprecations are verified once more by the mentor when they become load-bearing in a lesson (fact-check rule in SKILL.md).
- The tree is a plan, not a syllabus to recite. Lessons still start from the problem each concept solves.
- Re-run a single research step (not the whole fan-out) when a milestone later reveals a gap; journal it as a plan gap.
