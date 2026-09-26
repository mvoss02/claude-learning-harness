# Learning system rework: from rules to mechanisms

Date: 2026-09-13. Status: PROPOSAL, awaiting the learner's decisions (section 5).

## 1. Why

Goal stated by the learner: stay a valuable engineer while building with AI daily. Concretely: be able to tell when the AI is wrong before users do, diagnose under ambiguity, own consequences.

Evidence from the ledger on 2026-09-13, three weeks after the last redesign:

- `independence.md`, "Choosing next evidence": both entries say "Claude chose every evidence step". Repo navigation and reading unfamiliar code: zero entries.
- `solo.md`: zero completed. One spec parked with the reason "I would just copy-paste what we have".
- `index.md`: 35 active cards, 3 retrievable, 0 transferable, 36 due. Roughly ten domains. The roadmap of 2026-09-02 rates most of those domains LOW ROI and lists seven MUST areas with zero cards.
- Git: 10 of 18 commits since 2026-08-01 touched the contract or playbooks.
- Rows that moved to L3 (HCL typed by the learner, tmux drills, Go error reading) share one property: the structure made the learner do the work. Rows that did not move depended on Claude refraining.

Diagnosis: the design is sound and already cites the right science. It fails at enforcement. Every rule with teeth asks Claude to hold back, and a prose rule loses that fight against the harness and against the pull of progress often enough that the log reads as delegation.

## 2. What the research says (verified 2026-09-13, sources in the two research reports)

LLM-specific:

- Answer-giving AI reliably hurts unassisted performance. Bastani et al., PNAS 2025, RCT n≈1000: practice +48%, exam −17%. Anthropic, Jan 2026, RCT n=52 developers: quiz 50% with AI vs 67% hand-coding (d=0.74), largest gap on debugging. Liu et al. 2026, RCT n=1222: ten minutes of AI help reduced later unassisted persistence.
- Design flips the sign. Bastani's hint-only tutor erased the harm. Kestin et al. 2025 (Harvard): a tutor that gives one step at a time and makes the student try first beat active-learning classes, 0.7 to 1.3 SD.
- Mode of use matters more than the tool. Anthropic exploratory: explanation-seekers scored 65%+, delegators below 40%.
- Self-assessment is unreliable. METR 2025: 19% slower, believed 20% faster. Prather 2024: "illusion of competence" in strugglers.
- Debugging and code reading erode first (Anthropic, Prather).

Classic:

- Retrieval beats re-reading at delays past a day, g≈0.5 (Rowland 2014, Adesope 2017).
- Attempting before instruction raises retention even when the attempt fails (Kornell 2009; Sinha and Kapur 2021, g=0.36).
- Self-explanation g=0.55 (Bisra 2018).
- Spacing: gap grows with the retention interval, 5 to 20% of it (Cepeda 2008).
- Worked examples help novices, hurt once a schema exists; fade them (Kalyuga 2007).
- Fluency is an illusion; judgments of learning made with the answer in view are inflated (Koriat and Bjork 2005; Rozenblit and Keil 2002).
- Far transfer is near zero (Sala 2019, g≈0.01); near transfer needs deep structure across varied surfaces.
- Deliberate practice explains under 1% of variance in professions (Macnamara 2014); judgment grows through varied real work with feedback.
- Tutoring effect comes from step-level interaction, d≈0.8, not 2.0 (VanLehn 2011).

Implications for this setup:

1. The variable that matters is who generates the first attempt. Not how much Claude explains.
2. Microdoses inside real work are the right vehicle (Macnamara), but the dose must be the first move (Kornell, Kapur), and a hint must cost something or the retrieval effort never happens.
3. Retrieval must actually fire, spaced, in generation form. Currently it never does.
4. Debugging is the capability to protect first (Anthropic, Prather, and the log).
5. Fewer domains. Far transfer is not coming; near transfer inside two or three areas is achievable.
6. the learner cannot feel whether it is working (METR). Evidence files, not impressions.

## 3. Design principle

**Replace rules that ask Claude to refrain with mechanisms that make the learner act.** Keep the stage ladder, calibration, and say-back rules; they are already right. Shorten the contract. Every remaining rule with teeth gets a mechanism.

## 4. Mechanisms

### M1. Gate hook on investigation commands

PreToolUse hook on Bash. If the command matches an investigation pattern and no hand-off flag is set, the hook denies it and tells Claude: "investigation command; propose it to the learner with the why". the learner runs it with `! <cmd>`.

Proposed pattern list (the learner decides): `kubectl`, `helm`, `flux`, `az`, `psql`, `pg_dump`, `ssh`, `tofu`/`terraform` (plan, apply, import, state), `curl`/`http`/`wget` to any host except localhost, `atuin` excluded.

Hand-off flag: `~/.claude/.handoff-active`. Claude sets it in one visible Bash call when the learner says SHIP, "run it", "take this"; clears it when the task ends or the learner says so. The flag is visible in the transcript, so a self-granted hand-off is auditable.

Not gated: file searches, reads, edits, tests, formatting, dependency installs, git.

Science: Kornell 2009, Kapur 2021 (attempt first), Anthropic 2026 (debugging erodes first).

### M2. Curriculum file drives the session

`memory/curriculum.md`: the roadmap's MUST areas as a topic tree, subtopics from the week pages, one status per subtopic (`not started | cards | owned`), `owned:` areas, `week:` pointer, `checkpoint:` last date.

Cards carry `curriculum: <node>` or `curriculum: off`. Off-curriculum cards are kept, never reviewed, never drilled.

Session-start hook prints: week, owned areas, up to 3 due cards from owned areas (generation-form recall question included), count of other due cards, days since last checkpoint. Retrieval rule: one of those three is asked at the first natural boundary of a substantive session, in generation form ("explain how it works underneath", "what would you reach for and why"). "Not today" still ends it for the session.

Science: Rowland 2014 (retrieval), Cepeda 2008 (spacing), Rozenblit 2002 (test explanatory depth), Sala 2019 (narrow).

### M3. Ownership decides who types

In owned areas, the roles flip: the learner writes the first draft (design, hypothesis, code, query) and Claude reviews, unblocks, supplies syntax. Full HANDS-ON is the default for debugging in owned areas. Claude's version is shown only after the learner's attempt is on the record.

Outside owned areas: current PAIR loop (Claude drafts, the learner reshapes) or SHIP. Off-curriculum work is legitimately delegated; no guilt, no cards beyond `encountered`.

Hints cost a sentence: "what I tried and where I am stuck". Ladder stays question, hint, direction, fragment; no solution on taught material.

Science: Anthropic 2026 (hand-coding condition), Kalyuga 2007 (fading), Bisra 2018 (self-explanation).

### M4. Weekly checkpoint replaces solo blocks

20 to 30 minutes, inside a session, cold. Claude gives a problem statement on a practiced concept in an owned area, different surface, then stops. the learner writes the answer (diagnosis, design, code, or reconstruction) into `memory/checkpoints/YYYY-MM-DD.md` without Claude. Claude reviews after: reconstructed / syntax only / stalled on model / wrong abstraction. Evidence lines go on cards; a clean checkpoint on a different surface is the path to `transferable`.

Hook prints days since last checkpoint. At 10+ days Claude proposes one at the next natural boundary. `solo.md` is retired into this.

Science: Koriat and Bjork 2005 (judge only after a delayed unaided attempt), METR 2025 (calibration), Sala 2019 (varied surfaces).

### M5. Cards: birth unchanged, ownership by the learner

Born `encountered` by Claude when touched and the tool-swap test passes ("would this still be true if I switched tools or vendors?"). Tool-bound material goes to `notes/<domain>.md`, one line each, never reviewed. Promotion above `introduced` requires a "My model" line written by the learner from memory. Recall questions are generation-form.

### M6. Contract shrinks

CLAUDE.md keeps the modes, the build loop, the voice, and the rules. The science rationale moves to this spec. Each rule with teeth points at its mechanism (M1 to M4). Target: about half the current length.

## 5. Decisions for the learner

1. M1 gate hook: yes or no; edit the pattern list.
2. Owned areas. Recommendation: the debugging loop (a capability, any domain) plus two knowledge areas, databases and networking-to-distributed-systems (timeouts, retries, delivery semantics, backpressure). The roadmap week rotates a third focus automatically.
3. M4 checkpoint: weekly, 20 to 30 minutes. Yes or adjust.
4. Card retag: retire tmux (2), providers, aks-node-pools, naming-scopes, dependency-pinning to notes; trim cosign, azure-policy, managed-identity, workload-identity to their transferable core; keep the rest with a `curriculum:` line.

## 6. Build order once decided

1. `memory/curriculum.md` from the roadmap.
2. Hook: session-start additions (week, owned, 3 due, checkpoint days). Tests updated.
3. Hook: PreToolUse gate script plus settings.json entry. Tests.
4. Convention edits (tool-swap test, `curriculum:` field, My-model promotion rule, checkpoint section replacing solo).
5. CLAUDE.md rewrite to about half length, rules pointing at mechanisms.
6. Card retag and notes files.
7. `scripts/check.sh`, commit.

## 7. How we will know in four weeks

- `independence.md` "Choosing next evidence" and "First debugging hypothesis" carry entries at L3 with the note "the learner chose the evidence".
- At least three checkpoints completed and reviewed.
- Three cards in owned areas reach `retrievable` on cold review.
- The gate hook denied at least a handful of commands; none were self-granted hand-offs.
If none of these move, the mechanisms are ceremony too, and the next step is a different design, not a longer one.
