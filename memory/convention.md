---
name: convention
description: "How the learning ledger works: concept stages, evidence, card shape, review placement, archive rules, independence and solo tracking"
metadata:
  type: reference
---

# Learning ledger convention

Global, topic-organized, git-tracked in `~/.claude` (private repo), plain markdown with `[[basename]]` wikilinks. **One directory per topic, one file per concept, one central causal model per card.** A card records a learning journey; it is not proof of mastery.

```
~/.claude/memory/
  convention.md                 ← this file
  curriculum.md                 ← the direction: owned areas, topic tree, week pointer (hook reads it)
  index.md                      ← one line per active concept, read each session
  independence.md               ← scaffolding-fading evidence per capability
  checkpoints/YYYY-MM-DD-*.md   ← weekly cold attempts by the learner, reviewed after (hook counts days)
  notes/<domain>.md             ← field notes: tool-bound facts, one line each, never reviewed
  solo.md                       ← retired 2026-09-13 (history)
  kubernetes/requests-limits.md ← active card
  kubernetes/requests-limits.history.md   ← optional long evidence log for that card
  archive/merged/<slug>.archived.md       ← originals of merged cards (history only)
  archive/retired/<slug>.archived.md      ← retired one-offs (history only)
```

## Sacred rule

**`encountered` is the default stage. Teaching and demonstrated evidence change the stage, never the act of writing the card.** A card may exist purely so we remember the concept exists.

## Stages (frontmatter `stage:`)

| Stage | Meaning | What promotes into it |
|---|---|---|
| `encountered` | We ran into it. I may know nothing. | Default on creation. |
| `introduced` | Claude taught the minimum useful model; I can roughly say what it is and why it matters. | A real orient + model moment AND a short say-back in my words (see "Say-back"). Not a one-line flag, not "makes sense". |
| `practiced` | I used it with guidance: predictions, debugging, implementation decisions, reasoning through examples. | Guided use in real work or an exercise. |
| `retrievable` | After a delay, without seeing the answer, I reconstructed the core model reasonably well. | A cold recall in a LATER session, unaided, core model right. |
| `transferable` | I applied the idea to a meaningfully different or unfamiliar problem without Claude framing it. | Independent generation in a different context: a solo block, independent production work, an interview-style exercise, an unaided incident investigation, or a different implementation done with minimal AI framing. The requirement is the independence and the different surface, not a particular ceremony. |

Rules:
- Promotion needs evidence AND spacing. Correct answers moments after discussion never promote. Immediate ≠ retained, recognition ≠ generation, same-context generation ≠ transfer.
- **Promotion above `introduced` requires a "My model" line written by the learner from memory.** Claude writes cards at birth; the card becomes the learner's when his own reconstruction is on it. A card whose "My model" still reads "(Claude's teaching explanation, not yet the learner's)" stays at `introduced` regardless of other evidence.
- Every promotion is said out loud ("promoting X to practiced because Y"); I can veto a promotion. I cannot veto the recording of a miss.
- **Eligibility: only test what the learner actually held.** Unseen (never taught, `encountered`, or anything Claude built or decided while he watched, including all `/ship` work) is explained, never tested. Participated or newly learned (this session, `introduced`) may be reconstructed right after the build. Previously understood (`practiced` or above) is fair for cold retrieval. Questions test ownership of the system (end-to-end flow, source of truth, failure, rejected alternatives), not trivia, and never frontend mechanics.
- Never quiz `encountered` concepts. Never ask above the stage: `introduced` gets the model reactivated in one line, then an application; `practiced` gets cold prediction, familiar case, basic failure mode; `retrievable` gets alternatives, seams, transfer attempts. Ladder and stage-aware prediction: `~/.claude/docs/pedagogy/teaching.md`.
- Before any question, check I hold a minimum viable model; if not, teach it first (3 to 8 sentences), then ask. "I don't really remember this" → short reorientation, then one application; log the miss honestly.
- Questions may ask "what would you reach for?" (tool or evidence category) as well as "explain X". Exact flags or syntax only when the capability needs them.

## Misses and demotion (evidence-based, not automatic)

- Record every meaningful miss as a dated Evidence line, as it happened.
- **Demote** when the miss concerns the central causal model of the card, or when repeated evidence shows the capability is no longer retrievable.
- **Do not demote** for one peripheral miss (a badly calibrated question, ambiguous wording, fatigue, a side detail, one weak submodel). Mark `status: shaky`, shorten the interval, keep the stage.
- I may challenge the stage interpretation; a challenge can change the stage decision. It never edits or deletes the evidence lines.
- Demotions are said plainly, no drama.

## Frontmatter

```yaml
---
name: <slug>                    # unique basename across memory/ (wikilinks are basename-only)
description: "<one line>"       # QUOTE it: descriptions with ': ' are invalid YAML otherwise
metadata:
  type: reference
topic: <dir name>
aliases: [old-slug, other-old-slug]   # optional; old wikilinks resolve here
stage: encountered | introduced | practiced | retrievable | transferable
curriculum: <area>/<node> | off  # node in curriculum.md; `off` = kept, never reviewed or drilled
status: shaky | solid            # optional confidence within a stage; NOT the stage
review: YYYY-MM-DD               # next cold check; omit for `encountered`
independence: 0-4                # optional, latest level for concepts tied to a capability I'm building
---
```

Frontmatter is the single source of truth for stage/status/review. Basename wikilinks only (`[[wal]]`). Validate with `scripts/validate-frontmatter.py` (real YAML parser; the hook's parser is lenient and proves nothing).

## Card body: current model, not a chronicle

One screen. One central causal model. If a recall question would be a multi-part oral exam, or a miss could not be attributed to one model, split the card.

```markdown
# <Concept name>

**Why it matters:** the task, incident, or question that exposed it (one or two lines).

**My model:** my own explanation, in my words, when I have given one. Claude's version is labeled "(Claude's teaching explanation, not yet the learner's)".

**Core model:** canonical explanation: anchor, mechanism, the seam where it leaks. Optionally `Reach for this when: ...` / `Tool family: ...`.

**Current misconception:** open, dated, specific. Remove when repaired and re-demonstrated.

**Recent evidence:** the last ~5 dated lines (predicted correctly / explained unaided / debugged / implemented with guidance / transferred / missed X). Older lines move to `<slug>.history.md`.

**Next useful step:** ONE activity.

**Recall question:** one question testing one coherent capability, matched to the stage.

History: [[<slug>.history]] (only when a history note exists)
Related: [[concept]], [[not-yet-written]]
```

History notes (`<slug>.history.md`, same topic dir) carry the full evidence log and old incident detail. They have no `stage:` and are never reviewed.

## Archive

Merged or retired cards move to `archive/merged/` or `archive/retired/` as `<slug>.archived.md` (git mv, history preserved). Their frontmatter renames `stage:`/`review:` to `archived_stage:`/`archived_review:` and adds `archived: merged | retired`, `archived_on:`, and `archived_into:` (merged only). The suffix keeps the old basename free so `aliases:` on the active card win; the renamed keys keep them out of every review query, and the session-start hook skips the folder. Revive by moving the file back, restoring the keys, and setting a review date.

## Card threshold

**Tool-swap test first:** would this still be true if I switched tools or vendors? "A Service is a stable number in front of churning pods" survives moving to GKE or Nomad: card. `tmux switch-client`, `features {}`, an Azure error body: fails the test, goes to `notes/<domain>.md` as one line (what it is, when it bit us, what to search). A tool can hold both: Terraform's plan model is a card, its provider quirks are notes.

Then a card only when at least one holds: foundational to an area I want to own; encountered repeatedly; caused a real misconception; broad transfer value; explicitly chosen by me; important for a system I work with regularly. Every card carries `curriculum: <area>/<node>` from `curriculum.md`, or `curriculum: off` when nothing fits (kept as a record, never reviewed).

## Retrieval placement

Spacing: first review ~3 days out, then ~1 week, ~3 weeks, ~2 months. Shaky or missed recall shortens it. `retrievable`/`transferable` still decay and still get reviews. `encountered` cards have no review date. Retention target: correct unaided retrieval in about three separate sessions on different days (successive relearning) is the working target, not a law; one strong transfer outweighs several recall checks. A miss is classified before it counts (central model / minor detail / terminology / syntax / ambiguous question / separate sub-concept); only a central-model miss or repeated misses reset the count, per "Misses and demotion". A confident wrong prediction gets a retest within a week. Reviews mix confusable neighbours so the first step is deciding which case applies.

- **Contextual (preferred):** when today's work touches a due concept and its stage makes recall fair, the real task is the review ("this plan touches the three boxes again; before I interpret it, what are they?").
- **Owned-due (the one that must fire):** the hook lists up to three due cards from owned areas with their recall question. In a substantive session Claude asks ONE of them at the first natural boundary, in generation form (explain the mechanism, or what would you reach for and why), not as recognition. "Not today" ends it for the session. This is the retrieval that never happened under the old rules; it is not optional for Claude.
- **Other due cards:** contextual only, never interrupt the start of work, at most one offer at a natural boundary, "not today" is a complete answer. "review" from the learner runs several.
- **Dedicated review:** when I ask for review, cover several cards.
- **Backlog:** a growing backlog triggers pruning, suspension (remove the review date, note it in the index), merging, or a dedicated review plan. Never compulsory catch-up during ordinary work.
- The session-start hook reports due-card state to Claude; that report is information, not a demand.

## Say-back (selective)

"Makes sense" is zero evidence. A short say-back in my words is asked for when the concept is card-worthy, the model is load-bearing for the next decision, promotion to `introduced` is being considered, Claude suspects recognition without generation, or I want to learn the concept. Not for minor details, lookup-worthy facts, syntax, or every toolbox note. **Only on curriculum material:** a concept in an owned area or on a node in `curriculum.md`. Never on the learning system, the contract, tooling setup, or the design rationale; those sessions end with a one-line summary and no question.

## Independence (capabilities I chose to own)

Levels, evidence not judgment; `/ship` tasks are legitimately 0 to 1:
- 0 Claude framed and solved nearly everything
- 1 I understood and modified Claude's solution
- 2 I proposed meaningful parts of the reasoning/design; Claude did most execution
- 3 I owned design and major implementation; Claude unblocked/reviewed
- 4 I solved it independently; Claude reviewed afterward

`independence.md`: at most one entry per capability per substantive session, and only when scaffolding changed or meaningful evidence appeared. The file shows progression, not activity volume.

## Checkpoints (`checkpoints/`)

Roughly weekly, 20 to 30 minutes, inside a session, cold. Claude gives a blank-page problem on a `practiced`-or-above concept in an owned area, or on the current roadmap week's nodes and design work (the week table in `curriculum.md`: design minis, project deep dives, incident narratives), different surface, then stops; the learner writes the attempt into `checkpoints/YYYY-MM-DD-<slug>.md` without Claude; Claude reviews after and classifies each part (reconstructed unaided / syntax only / stalled on model / wrong abstraction). The hook reports days since the newest dated file; at 10+ days Claude proposes one at a natural boundary, once. Checkpoint files carry no `stage:`. Format and rationale: `checkpoints/checkpoints.md`. Solo blocks (`solo.md`) are the retired predecessor.

## Owned areas (`curriculum.md`, `owned:`)

In an owned area the learner's move comes first, every time: the hypothesis, the design, the approach, the query. Claude reviews, spars, supplies syntax, shows its own version only after his is on the record, and may then type the implementation; he types it himself only when the coding mechanic is the skill being learned. Full HANDS-ON is the default for debugging there. A hint costs a sentence ("what I tried, where I am stuck"); the ladder is question, hint, direction, fragment; no solution on taught material. Outside owned areas: normal PAIR, or `/ship` for a bounded task; delegation is legitimate.

## Session flow

- **Start:** the hook reports the curriculum week, owned areas, owned-due cards with recall questions, the count of other due cards, days since the last checkpoint, and whether the hand-off flag was left set. Retrieval follows "Retrieval placement" above.
- **Concept appears in work:** flag in one line, place it in its family if useful, no lecture unless relevant or asked. Card only if it meets the threshold; born `encountered`; `introduced` only after a real teaching moment plus say-back.
- **Concept used with guidance:** add an Evidence line; `introduced → practiced` if real guided use happened.
- **Wrap-up (substantive sessions, brief):** one important model, one tool/solution-space addition, one misconception or open question, one independence shift if present. Cards updated by evidence; index line updated. When the previous conversation clearly lacked a wrap-up and the context is available, offer one at the next natural boundary. No wrap-up for trivial sessions.

## Index line format

`- [slug](topic/slug.md) — **stage** — hook`

## Scope

This ledger holds cross-project concepts. Project-specific facts stay in that project's `~/.claude/projects/<slug>/memory/`. Cross-project decisions (decision / alternatives / why / tradeoffs) may live here in the relevant topic dir.

## Privacy

Cards and mentor state contain company-specific identifiers and incident details. The repo is private; keep it that way. Reusable vs private split and the packaging script: `~/.claude/docs/private-state.md`.

## Validation

`scripts/check.sh` runs JSON, Python, frontmatter, hook-fixture, and link checks. Before committing: `git pull --rebase`, `scripts/check.sh`, commit, push.
