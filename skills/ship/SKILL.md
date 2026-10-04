---
name: ship
description: "Bounded SHIP mode: execute one clearly scoped task at full speed, summarize, return to PAIR. The only way into SHIP; only the learner can invoke it."
disable-model-invocation: true
argument-hint: "<the bounded task to ship>"
---

# /ship

Scope requested: $ARGUMENTS

SHIP is the exception to PAIR (`~/.claude/CLAUDE.md`). For this one bounded task, optimize for execution speed and make the routine decisions yourself. It does not mean "take over the rest of the project", and it ends with this task.

1. **State the scope** in one to three lines before the first edit: what you will ship, what counts as done, what you are leaving out. No argument given means the scope is the task currently under discussion; state it the same way. If it cannot be bounded in three lines (several features, an open design question, "the rest of the project"), do not start: say what is unbounded and propose the smallest shippable piece.
2. **Execute.** No reps, no Decide or Trace stops, routine decisions are yours. Normal voice, kept terse. Open the investigation gate only if the scope needs gated commands, in one visible call: `touch ~/.claude/.handoff-active`. Commit, push, apply, deploy, or delete only when the scope names it.
3. **Scope guard.** Stop and hand the decision back when the work grows past the stated scope: a new capability or system boundary, a new dependency or piece of infrastructure, an irreversible change the scope did not name (schema, public API, protocol, data migration), or roughly twice the expected surface. Report what is done, what you found, and the decision that is now the learner's. Never widen silently.
4. **Summarize** on one screen: what changed with `file:line`, the decisions that matter with the alternative each rejected, where it fails, what was verified and how, what is left open. This is a brief, not a quiz. Nothing shipped here is asked back; it counts as unseen until the learner picks it up in PAIR.
5. **Exit.** `rm -f ~/.claude/.handoff-active`, then say "Back in PAIR." SHIP never carries into the next message, the next task, or the next session. Another SHIP needs another `/ship`.
