# mentor

A Claude Code skill: a principal-engineer mentor that teaches you a technology
by having you build it into your own real repo, milestone by milestone.

Not a tutorial generator, and not an examiner guarding the answer key. The
mentor audits your repo, spars with you to build a learning plan, teaches each
milestone's concepts properly (orientation, mental model, worked example, with
a project-grounded HTML page as the visual aid), coaches while YOU write the
code that teaches (it may run investigations and tests for you once you have
chosen what evidence to gather), and gates each milestone behind an
evidence-based review: working behaviour, unaided explanation, and a "what
breaks first" answer. Transfer is checked later, spaced. You own the code
that teaches; it never lands code you cannot explain.

## Install

```bash
git clone <this-repo>
cp -r mentor ~/.claude/skills/mentor
```

Then in any project: `/mentor` (it is slash-command only by design; a teaching
session should be deliberate).

Arguments: `/mentor status` shows plan progress, `/mentor drill` asks for
strict typing this session (you type every line), any other text becomes
context for the session.

## First run

`/mentor` in your repo with a goal in mind, e.g. "I want to learn
OpenTofu by putting this cluster under IaC". The intake interview builds
`PLAN.md` with you; nothing is taught until you approve the plan. Missions are
sized (small / medium / large) and researched proportionally: a one-session
mission gets a repo audit and the official docs, not a research fan-out.

## State

Everything lives in `~/.claude/mentor/<repo-name>/`:

- `PLAN.md` — mission, milestones, decisions
- `JOURNAL.md` — session log, verdicts, gap lists
- `lessons/` — self-contained HTML lessons (offline, printable), plus a
  private `NNNN-<slug>.reference.md` per milestone the mentor writes for
  itself: required behaviour, invariants, acceptable design families,
  trade-offs, failure modes, misconceptions, evaluation criteria. Never an
  intended architecture, never shown to you.
- `concepts/` — concept cards with an explicit learning stage
  (encountered → introduced → practiced → retrievable → transferable)

If `~/.claude` is a dotfiles repo, your learning state syncs across machines
for free.

## Integrations (all optional, all auto-detected)

- **Learning ledger**: if `~/.claude/memory/convention.md` exists (a global,
  topic-organized concept ledger), concept cards are written there instead of
  `concepts/`, so one spaced-repetition system covers everything you learn.
- **caveman plugin**: composes; caveman compresses chrome (pleasantries,
  filler), and the mentor's explanations are already short units. Compression
  must never remove a model, a worked example, or a re-explanation.
- **SessionStart hook** (opt-in): surface due reviews when you open a shell.
  Add to `~/.claude/settings.json` hooks:

  ```json
  {
    "hooks": {
      "SessionStart": [{
        "hooks": [{
          "type": "command",
          "command": "grep -rlE 'stage: (introduced|practiced|retrievable)' ~/.claude/mentor/*/concepts/ 2>/dev/null | head -3 | xargs -I{} echo 'Mentor: concept to review {}'"
        }]
      }]
    }
  }
  ```

## Philosophy

- Orient → teach → model → practice together → fade scaffolding → retrieve
  (spaced) → transfer. Teach first when background is missing; struggle is a
  tool, not the teaching.
- Learn by building something real; the repo improves as you do.
- Predictions before runs whose outcome teaches something; wrong predictions
  are the best teachers. No prediction ceremony before mechanical commands.
- Teach before testing. Questions calibrated to what was taught and
  demonstrated; a card existing never means the concept is known. A resumed
  session starts with "where were we, what did we establish?", not a quiz.
- Help is adaptive, per concept, never by seniority: prerequisites are
  checked before every lesson, a stall is diagnosed before it is helped
  (productive difficulty, missing prerequisite, unclear explanation, too
  many unknowns, slip, fatigue), and a re-explanation changes representation
  instead of repeating words. One coherent chunk at a time, as long as the
  causal model needs and no longer. You can change the format at any moment
  ("explain directly", "worked example", "let me try", "harder").
- Slow, fine-grained beginnings: a new technology starts as small units (one
  model, one piece of syntax or tooling, one guided and one independent
  application), each carrying one or two unknowns, before features combine
  them. Three formats: project sessions, focused labs, transfer sessions.
- Gates judge behaviour, invariants, and trade-offs, not a hidden
  architecture. A valid different design is "valid; optimises for X,
  introduces Y". A demonstration that did not happen yet is `gate-pending`,
  not a failure.
- Sessions end on a retrieval, never on reading.
- Evidence-based gates, honest journal, no social passes. States:
  `gate-pending`, `passed`, `needs-revisit`.
- Escalation ladder when stuck on something already taught: question → hint →
  direction → fragment. Rescue on the deliverable kills retention.
- Ownership: you write the code that teaches the milestone's concepts; the
  mentor may write scaffolding and boilerplate once you have said what it
  should do, and nothing it wrote lands until you can explain it and predict
  an edge case. `drill` (opt-in) means you type every line. The mentor may
  run commands once you chose the evidence, unless a milestone names the
  execution loop as yours or you say `HANDS-ON`. You steer the teaching
  format turn by turn ("explain this directly", "let me try", "harder").
