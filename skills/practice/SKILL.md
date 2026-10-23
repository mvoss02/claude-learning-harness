---
name: practice
description: "Practice block: retrieval and application of material the learner was already taught, first move without AI, Claude reviews after. Logs the block in memory/experiment.md. New material belongs to /mentor or a lesson. Only the learner can invoke it."
disable-model-invocation: true
argument-hint: "[what to work on] | skip"
---

# /practice

Request: $ARGUMENTS

The retrieval half of the Practice track in `~/.claude/CLAUDE.md`: the learner's own first move on something he was already taught, AI closed until it exists. New material is `/mentor` (a project) or a lesson in PAIR, never this. 45 to 60 minutes is the intended size; nothing enforces it.

**`skip`** as the argument: append `- YYYY-MM-DD skipped <reason if given>` under "Practice log" in `~/.claude/memory/experiment.md`, say "Logged. Back in PAIR.", stop. No comment, no persuasion.

1. **Pick the work, in five lines at most.** Read the "Practice repo" line in `memory/experiment.md`, this week's line in `memory/curriculum.md`, and the due rows in `memory/mistakes.md`. Offer two or three options, all on taught material: a due mistake row rebuilt from a blank editor, this week's DSA pattern, a design mini or checkpoint on a concept at `introduced` or above, a cold rebuild of something built earlier. An argument names the work directly. the learner picks.
2. **Untaught material is redirected, not taught.** If the picked work rests on a mechanism the learner has not been taught (no card above `encountered`, not taught in an earlier session), say so in one line and offer `/mentor` or a lesson in PAIR, then pick another item. Generating from nothing is guessing, not practice.
3. **Close.** Say exactly: "AI closed. Post your attempt and the point where you got stuck." Until the attempt arrives, answer logistics only (broken environment, missing tool, wrong doc version: fix it and say so in one line). A content question before the attempt gets "Write down what you have and where it stops; that is the attempt." A stuck note is a valid attempt.
4. **Review the attempt.** Respond to the learner's reasoning first: what holds and why, what breaks, at which layer. Gaps go up the ladder one rung per reply (question → hint → direction → fragment), unless he asks to jump. Show your own version only after his is on the record. A gap that turns out to be a missing model is a teaching failure, not his: name it and log it for `/mentor` or a lesson.
5. **Log mistakes.** For each real mistake, ask the learner for one line of what he thought, then add the row to `memory/mistakes.md` (Next = today + 3 days). A rebuilt row that now holds moves to its next step (+2w, +6w, then `done`).
6. **Close the block.** Append `- YYYY-MM-DD done <what, one line>` to the practice log in `memory/experiment.md`. Then "Back in PAIR."

`quick` inside a block skips nothing before the attempt exists; after it, it skips the learner's next move for that one message. "Not today" ends the block and logs it as skipped. The word "practice" in a sentence is not the command.
