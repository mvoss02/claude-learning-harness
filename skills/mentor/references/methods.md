# Method selection

Per concept, choose the teaching method deliberately and record the choice
plus one-line reason in the journal. The selector is the learner's prior
knowledge (ledger/concept cards), not habit.

## Menu

- **Struggle-first task** (productive failure): the learner attempts a scoped
  problem BEFORE the concept is explained; the consolidating explanation then
  contrasts their attempt with the canonical approach. Use when the learner
  actually holds adjacent prior knowledge (stage `practiced` or above on the
  neighbouring concepts, or demonstrated in the repo) and the target is
  conceptual understanding. A card merely existing is not prior knowledge.
  [Sinha & Kapur 2021, Rev. Ed. Research: meta-analysis, g = 0.36 for
  concept/transfer when problem-solving precedes instruction]
- **Worked walkthrough**: study an annotated example first (toy domain, never
  the milestone deliverable), then fade support toward independent work. Use
  for true novices or procedural mechanics. Fade it as expertise grows;
  guidance that helps novices hurts advanced learners.
  [Sweller & Cooper 1985; Kalyuga et al. 2003, "expertise reversal effect"]
- **Visual aid** (HTML lesson): diagrams, flows, one worked example, repo
  mapping, the DIY spec. Supports the chat teaching, never replaces it: chat
  owns orientation, teaching, questions, diagnosis, and exercises. The page
  carries no quiz, multiple-choice, or reveal blocks; questions are asked in
  chat where a wrong pick can be diagnosed (`references/lesson-style.md`).
- **Multiple choice in chat, second choice only**: open question first,
  always. Reach for MC when the open answer was vague and you need to find
  WHICH wrong model the learner holds, or as a distractor discussion after a
  correct open answer. 3 to 4 options, each distractor encoding one specific
  misconception; the learner picks AND justifies, then the distractors are
  discussed. Weak as evidence on its own (recognition); never the default
  because it is the easiest question to generate. Follow a correct pick with
  "why is option B wrong?" to turn it into generation.
- **Prediction drill**: commit a prediction before a command whose outcome
  teaches something about a concept in play (a plan header, a first apply, a
  test expected to fail, a breakage). Selective, not every run: the boost
  lands on the pretested content, and predictions on mechanical or repeated
  commands are ceremony. One prediction per meaningful moment; skip when the
  learner is in flow or the outcome is already obvious to them.
  [Kornell, Hays & Bjork 2009; Pan & Carpenter 2023 review]
- **Breakage lab**: break the system on purpose, predict, observe, explain.
  Use for failure-mode and reliability concepts.
- **Focused lab**: one mechanism isolated from the project for 20 to 40
  minutes when the project has too many moving parts around it; predict →
  run → break → explain, then back to the project (`references/progression.md`).
- **Test as model statement**: write the table-driven test that states what
  must hold, predict which rows pass, run. Legitimate from the first unit on,
  once the model is taught.
- **Explain-back / rebuild**: unaided retrieval at gates, wrapups, and
  retrospectives. The single most robust effect in the literature.
  [Roediger & Karpicke 2006; Adesope et al. 2017 meta-analysis, g ≈ 0.5-0.6]

Programming-specific formats (pick when the concept is code, not infra):

- **Runtime picture first** (notional machine): before syntax, show what the
  machine does at each line: what is copied, what is shared, what is on the
  stack, what blocks. Most novice bugs are wrong runtime models, not wrong
  syntax. Then ask "what does the machine do at this line?" [Sorva 2013]
- **Trace → explain → write**: before the learner modifies code, ask for a
  one-sentence relational purpose ("what does this function do?"). If they
  narrate line by line, drop to a trace of one concrete input. Writing
  ability sits on top of these two. [Lister / Whalley 2008, 2009]
- **Subgoal-labelled worked example**: every worked example carries 3 to 5
  purpose labels ("open resource", "guard error", "release"). After two
  labelled examples, the learner labels the third. Benefit concentrated in
  weaker learners, no extra time. [Margulieux et al. 2012, 2020]
- **Interference flag** (expert in a neighbouring language): name the places
  where the old model gives the wrong answer ("Python's `a = b` shares; Go's
  struct assignment copies"). Ask the learner to predict from the old model,
  run, and let the wrong analogy surface as evidence. [Shrestha et al. 2020]
- **Parsons problem**: hand the learner a correct toy solution as shuffled
  lines (optionally one distractor) to reorder before they write their own
  variant. Equal learning to writing from scratch in less time; good when
  the idiom is new and the deliverable would otherwise be copied.
  [Ericson et al. 2017, 2018; Haynes & Ericson 2021]
- **Predict, run, investigate, modify, make** (PRIMM): the ladder for any
  unfamiliar snippet: predict its output, run it, change one thing and
  trace, modify toward the requirement, then make the next piece from
  scratch. [Sentance et al. 2019]

## Two dials (the assistance dilemma)

Learning is an inverted U in the amount of help: too little and the learner
flounders on extraneous load, too much and they never construct the model.
The optimum moves with prior knowledge and with task complexity, so the
mentor sets help per concept from two dials, never from the learner's overall
seniority. [Koedinger & Aleven 2007; Kalyuga et al. 2003]

| Dial | Reading | Help level |
|---|---|---|
| Stage on THIS concept | `encountered` or missing | full model, worked toy example with subgoal labels, runtime picture; scaffolded questions only |
| | `introduced` | one-line reactivation, then apply; hints available |
| | `practiced` and above | cold questions, struggle-first on the table, fade |
| Task complexity | many interacting pieces at once | raise help one level temporarily; shrink the step |

Contingent shift: after a failed reply, more help; after a success, less.
Usually one rung at a time, but the learner's request or the stall diagnosis
below can jump rungs. Fade from the end of a task backwards (the learner owns
the finish first, then the middle, then the start). Fading without a
diagnosis is withdrawal, not fading. [Wood, Bruner & Ross 1976; van de Pol et
al. 2010; Renkl & Atkinson; the one-rung default is a design choice, not a
finding]

## Stall diagnosis

A stuck learner is in one of six states; only the first is answered with a
hint. Name the state (to yourself, and to the learner when it helps) before
responding.

| State | Signs | Response |
|---|---|---|
| Productive difficulty | holds the model, is making moves, errors are near the target | ladder; hold the line |
| Missing prerequisite | the question needs a model that was never taught or has faded | stop, teach or reactivate, resume |
| Unclear explanation | "I still don't get it", says it back wrong in the same way twice | re-explain with a new representation (below) |
| Too many unknowns | copied toy names, "I don't know what we want", same question twice, three fresh terms in one step | reframe the goal in a sentence; shrink or split the step; move one dimension to a lab (`references/progression.md`) |
| Implementation slip | model is fine, a typo or a wrong identifier | point at it; syntax as the only blocker is just given |
| Fatigue | short answers, guesses, time | stop, or switch to a lower-load format; journal, no grade |

[Hermans 2021 for the knowledge / information / processing split; the six-state
table is this mentor's practical inference]

## Explanation size and re-explanation

Explanation volume does not drive learning; contingency does. An explanation
works when it meets the learner's current model at an impasse and does not
replace their own processing. [Chi et al. 2001; VanLehn 2011; Wittwer & Renkl 2008]

- **Chunk, not sentence count.** Explain one coherent model or task chunk at
  a time, at the shortest length that makes the causal model understandable.
  A chunk usually carries: the problem, the core mechanism, one concrete
  example, one boundary or limitation, one learner action. Three sentences
  for a small idea; a diagram, several examples, or a comparison of
  alternatives for a large one. Avoid lectures that span unrelated concepts,
  and avoid splitting one causal chain across many messages. [Kestin 2025
  used brief responses; "one coherent chunk" is the inference, not a rule
  from the paper]
- On "I don't get it", a vague answer, or a wrong answer: first find the
  missing piece (ask "which part?", or diagnose: terminology / mechanism /
  prerequisite / boundary / order / layer).
- Then re-explain with a NEW representation: diagram, runnable toy, trace of
  one input, analogy to something the learner holds. Pair the new one with
  a familiar one; three representations at most. [Ainsworth 2006]
- Then one small application. Never "does that make sense?"; content prompts
  ("why must this come first?") beat confidence prompts. [Bisra et al. 2018]
- The learner can change the format at any moment ("explain directly", "a
  worked example", "another analogy", "let me try", "harder", "stop asking
  and teach this"). Honour it in the same turn.

## Selection heuristic

1. Prior-knowledge check, stage-aware. Ask: does the learner hold a model
   the attempt can lean on, and is the problem surmountable with it?
   - Concept `encountered` or missing, or a prerequisite model absent →
     direct teaching / worked walkthrough first.
   - `introduced` → guided attempt (hints available) only if adjacent
     knowledge makes it surmountable; otherwise walkthrough.
   - `practiced` or above on the neighbours → struggle-first is on the table.
   Stage is evidence about prior knowledge; prior knowledge and difficulty
   are what actually decide, not the stage label and never card existence.
2. Target check: conceptual "why" → lean struggle-first (within rule 1).
   Procedural "how" → walkthrough, then fade.
3. Difficulty stays surmountable: two failed attempts in a row → drop one
   level of difficulty. A difficulty is only desirable if the learner can
   get through it. [Bjork 1994, desirable difficulties]
4. Teaching before practice is not "giving the answer". The harm in the
   literature comes from unrestricted answer access DURING practice on the
   deliverable (+48% practice, -17% unassisted exam); scaffolded hints erase
   it. [Bastani et al. 2025, PNAS; Kestin et al. 2025, Sci. Reports]. So:
   explain fully, show worked toy examples, then keep the deliverable's
   answers behind the ladder while the learner builds.
5. Calibrate questions to stage (see `~/.claude/docs/pedagogy/teaching.md`):
   prediction from intuition → core model → familiar case → basic failure
   mode → alternatives → nuance. Wrong answers are diagnosed (terminology /
   mechanism / prerequisite / boundary / order / layer / trivial detail) and
   the specific piece repaired, then one more small application.
