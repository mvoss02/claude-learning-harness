# Lesson style contract

The HTML lesson is a VISUAL TEACHING AID the learner inspects and revisits. Chat is the interactive tutor: orientation happens in chat before the page, questions and exercises happen in chat after it. Reading the page is not evidence of learning.

One self-contained HTML file per lesson. `STATE_DIR/lessons/NNNN-<slug>.html`.

## Content rules

- Three layers in order: (a) concept, (b) this repo, (c) do-it-yourself. See `phases/lesson.md`.
- Layer (a) opens with the problem the concept solves, then the model, then ONE worked example (toy domain or the repo's shape), then the seam. Diagrams, flows, and progressions wherever they beat prose. Worked examples are welcome; they are how a novice gets a model.
- Short: 15-20 minutes of reading. One tangible win. Depth comes from the build phase, not lesson length.
- Layer (b) MUST quote real paths, resource names, and short excerpts from the learner's repo. Test: could this lesson have been written without reading the repo? If yes, rewrite (b).
- Layer (c) contains no solution code for the deliverable. Constraints, definition of done, prediction prompts, doc links.
- Cite one primary source (official docs preferred), verified current via web search, linked prominently.
- End with: "Ask your mentor when anything is unclear" and links to prior lessons for interleaving.

## No questions in the page

The page explains; the chat asks. No multiple-choice blocks, no quizzes, no predict-then-reveal widgets, no answer keys in the HTML. Reasons: a quiz in a document is recognition with the answer one click away, nobody can diagnose a wrong pick, and the page gets revisited as a cheat sheet, so embedded answers poison later retrieval.

What the page may contain instead: the worked example with its reasoning visible, diagrams, and in layer (c) the DIY spec with "before you run X, commit a prediction in chat" pointers (the question is named, the answer is not on the page).

Questions happen in chat, after the page, per `phases/lesson.md` step 5. Open questions first. Multiple choice is allowed THERE as a second-choice format (when the open answer was vague, or to discuss distractors after a correct answer): 3 to 4 options, learner picks one and says why, then the distractors get discussed (each wrong option encodes a specific misconception; name it). Never a bare "correct!". Print-only value of the page stays intact: it must read well on paper with no scripts.

## Visual rules

- Clean readable typography, generous whitespace, print-friendly. Think Tufte.
- Inline CSS only, no external assets; must render offline forever.
- Code excerpts in monospace blocks with the repo path as caption.
