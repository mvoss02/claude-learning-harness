# PLAN.md format

Milestones are deliverables, not topics ("remote state configured and verified", not "learn state"). Counts per size, early-unit counting and the primitive-first rule: `references/learning-tree.md`, "Mission sizing" and "Synthesis". Progression, unknowns budget and the finish line: `references/progression.md`.

```markdown
# Learning plan: <technology> via <repo>

Status: active | completed
Size: small | medium | large   (references/learning-tree.md, "Mission sizing")
Repo: <absolute path>
Started: <YYYY-MM-DD>

## Mission
<Why the learner wants this, in their words. What exists at the end that
doesn't today. Ground every lesson and milestone in this.>

## Learner baseline
<From intake: prior knowledge, strong areas to move fast through, gaps.>
<Learner's own map of the topic, verbatim, given before the tree was shown (3 to 4 chunks + what they would learn first). Compared against the tree at approval; the gap is the baseline.>
<Prerequisite probe results: 3 to 5 fundamentals questions and how each went (held / partial / missing). These set the starting stage; "tutorial done" is not evidence.>
<Interference map, when the learner is expert in a neighbouring technology: 4 to 6 "old says X, new says Y" points. Each becomes a predict-from-the-old-model moment in the milestone that touches it.>

## Finish line
<One sentence in the shape given in references/progression.md, "Finish line",
then the evidence list of demonstrable acts.>

## Capabilities to own
<From intake: which skills the learner wants as their own competence at the end (e.g. "design the module layout myself", "debug plan diffs unaided") vs merely operate. Independence levels are tracked for these. This section is the retention filter for the whole plan: progress notes, incident details, and decisions below are project history and evidence, not material the learner must retain or be quizzed on. Sparring, exams, and transfer target these capabilities and the milestone's ledger concepts only.>

Curriculum: <`<area>/<node>` from `~/.claude/memory/curriculum.md` (cards reviewed, checkpoints may draw on this mission) | `off` (legitimate; new concepts go to field notes or `curriculum: off` cards, never reviewed)>

## Learning tree
<Root = mission. Branches = areas. Leaves = concepts with prerequisite edges,
ledger stage today, and the milestone that teaches them. A small mission may
hold a flat list here instead of a tree. Approved by the learner on <YYYY-MM-DD>.>
- <Area A>: <why it matters for the mission>
  - <concept-slug> (stage: encountered | introduced | ... ; prereq: <slug> | none) → M1
  - <concept-slug> (...) → M2
- <Area B>: ...

Neighbourhood: <three sentences: what sits next to this technology, what each
alternative is for, when one would choose differently>

Sources: <primary source link> · <best curriculum found>

## Cuts
- <concept> | why the mission does not need it (revisit if: <condition>)

## Milestones
<Ordered by stage: early units → middle features → later features → transfer
sessions (references/progression.md). Units may be numbered separately from
features (G0..Gn, then M1..Mn); numbering is free, the progression is not.>

### <id>: <deliverable name>
- Stage: early | middle | later | transfer  · Format: project | lab | transfer
- Status: open | lesson-done | in-build | gate-pending | passed | needs-revisit
- Deliverable: <concrete artifact in the repo, or the lab's observable result. Append the reasoning move the learner owns here when one is singled out ("learner decomposes the redirect flow first", "execution loop", "drill: learner types every line", "setup is the lesson")>
- Concepts: <1 for an early unit, 2-4 later; slugs from the tree>
- Prerequisites: <what those concepts presuppose and the evidence held for each; anything without evidence is taught first>
- Unknowns: <count and names of major unfamiliar dimensions; early units 1, at most 2 if the second was taught first>
- Lesson: lessons/NNNN-<slug>.html (once written; features also get a private .reference.md)

### M2: ...

## Decisions
<Meaningful choices made along the way.>
- <date> <decision> | alternatives: <...> | why: <...> | tradeoffs: <...>
```
