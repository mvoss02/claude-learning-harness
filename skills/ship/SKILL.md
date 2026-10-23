---
name: ship
description: "Claude moves first on one bounded task or problem at full speed: state the scope, execute, summarize, return to PAIR. Gate closed unless the invocation says 'gate open'. The only Claude-first mode; only the learner can invoke it."
disable-model-invocation: true
argument-hint: "<one task or problem> [gate open]"
---

# /ship

Scope requested: $ARGUMENTS

The one Claude-first mode of `~/.claude/CLAUDE.md`. For this one task or problem, optimize for speed and make the routine decisions yourself. It never means "take over the rest of the project", and it ends with this scope.

1. **State the scope** in one to three lines before the first action: the task or problem, what counts as done, what you are leaving out. No argument means the task or problem currently under discussion; state it the same way. If it cannot be bounded in three lines (several features, several bugs, an open design question, "the rest of the project"), do not start: say what is unbounded and propose the smallest piece that ships.
2. **Execute.** No reps, no Decide or Trace stops, no teaching detours, routine decisions are yours. Questions to the learner only for what only he can answer (access, intent, a missing fact). Normal voice, terse. Commit, push, apply, deploy, or delete only when the scope names it.
3. **Gate closed by default.** Gated commands (kubectl, helm, flux, az, psql, ssh, tofu/terraform, remote curl) are proposed in a batch with one line of why; the learner approves with "run it", which opens the gate for that batch only (one visible `touch ~/.claude/.handoff-active`, removed right after). Only the words "gate open" in the invocation open it for the whole scope; then `rm -f ~/.claude/.handoff-active` at exit.
4. **Scope guard.** Stop and hand the decision back when the work grows past the stated scope: a new capability or system boundary, a new dependency or piece of infrastructure, a consequential choice (data shape, boundary, failure handling, security), an irreversible change the scope did not name (schema, public API, protocol, data migration), or roughly twice the expected surface. A fix stays minimal: no refactor, no extra feature. Report what is done, what you found, and the decision that is now the learner's. Never widen silently.
5. **Summarize** on one screen: what changed with `file:line`, the decisions that matter with the alternative each rejected, where it fails, what was verified and how, what is left open. For a bug, what broke and why in three lines at most, on the real artifact. This is a brief, not a quiz: everything shipped here stays unseen until the learner picks it up in PAIR.
6. **Record a fixed bug** as one row in `~/.claude/memory/mistakes.md`: What I thought = `(ship) <symptom>`, Why it was wrong = the cause, Repair = the fix, Layer, Next = `-`, Status = `ship`. A record, never asked later; it still counts when the same cause comes back.
7. **Exit.** Remove the hand-off flag if it is set, then say "Back in PAIR." SHIP never carries into the next message, the next task, or the next session. Another one needs another `/ship`.
