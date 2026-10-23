---
name: mistakes
description: "Concept mistake log: what I thought, why it was wrong, the repair, the layer, spaced revisits. Main retrieval source and the experiment's repeat-rate signal."
metadata:
  type: reference
---

# Mistake log

One row per real mistake: in Practice, in Trace, in an explain-back, or a `not-today` bug. I write "What I thought" in my own words. Due rows are asked in generation form, mixed across topics, at the first natural boundary of a substantive session. **Next** holds one date (YYYY-MM-DD); after a row is asked, Claude moves it to the next step of +3d → +2w → +6w, then `done`. A row whose "What I thought" recurs gets `REPEAT` in the Status column and a new row for the new date: repeats are what the experiment (`experiment.md`) counts. **Card** links the ledger card for the same concept, if one exists: one retrieval per concept, so asking the row also counts as that card's review.

Layers: `process` · `runtime/lib` · `syscall` · `kernel` · `wire` · `remote host` · `orchestrator` · `control plane` · `data store`. See `layer-map.md`.

| Date | What I thought | Why it was wrong | Repair | Layer | Next | Status | Card |
|---|---|---|---|---|---|---|---|
| 2026-01-05 | (example) `write` returning means the bytes were delivered | `write` returning means copied into the kernel send buffer; delivery is TCP's job later | Draw the kernel buffer between process and wire | syscall vs wire | 2026-01-08 | open | |
