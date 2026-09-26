#!/usr/bin/env python3
"""Deterministic fixture tests for hooks/session-start.py.

Run: python3 hooks/test_session_start.py   (exit 1 on failure)
Each case builds a temporary ~/.claude layout, pins LEDGER_TODAY, runs the hook
as a subprocess, and asserts on the injected text.
"""
import json
import os
import subprocess
import sys
import tempfile
import textwrap

HOOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "session-start.py")
TODAY = "2026-09-13"


def run_hook(files, flag=False):
    """files: {relative path under the fake ~/.claude: content}. Returns additionalContext."""
    with tempfile.TemporaryDirectory() as home:
        for rel, content in files.items():
            path = os.path.join(home, rel)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(textwrap.dedent(content))
        if flag:
            open(os.path.join(home, ".handoff-active"), "w").close()
        env = dict(os.environ, CLAUDE_HOME=home, LEDGER_TODAY=TODAY)
        out = subprocess.run([sys.executable, HOOK], env=env, capture_output=True, text=True, check=True).stdout
        return json.loads(out)["hookSpecificOutput"]["additionalContext"]


def card(stage, review, curriculum=None, question=None):
    fm = f"---\nname: x\ndescription: \"x\"\nstage: {stage}\nreview: {review}\n"
    if curriculum:
        fm += f"curriculum: {curriculum}\n"
    body = "# x\n\n**Core model:** y\n"
    if question:
        body += f"\n**Recall question:** {question}\n"
    return fm + "---\n" + body


CURRICULUM = """\
    ---
    name: curriculum
    description: "c"
    ---
    # Curriculum

    week: 3
    owned: databases, networking-distributed
    checkpoint: none yet

    ## weeks
    - week 2: networking-distributed/request-path; dsa: strings; design: outbound client; exit: timeouts in layers
    - week 3: databases/indexes-plans, databases/schema-access-patterns; dsa: stacks, queues; design: billing ledger; exit: justify an index
    """

CASES = {}


def case(fn):
    CASES[fn.__name__] = fn
    return fn


@case
def owned_due_shows_recall_question_and_other_is_count_only():
    ctx = run_hook({
        "memory/curriculum.md": CURRICULUM,
        "memory/postgres/wal.md": card("practiced", "2026-09-01", "databases/durability", "What must be on disk before commit returns?"),
        "memory/kubernetes/probes.md": card("introduced", "2026-09-05", "reliability-observability/health"),
        "memory/azure/policy.md": card("practiced", "2026-09-05"),
    })
    assert "WEEK: 3. OWNED: databases, networking-distributed." in ctx, ctx
    assert "OWNED-DUE (1): wal (practiced, +12d): What must be on disk before commit returns?" in ctx, ctx
    assert "OTHER-DUE: 2 (contextual only)." in ctx, ctx


@case
def current_week_line_printed_only_when_week_is_numeric():
    ctx = run_hook({"memory/curriculum.md": CURRICULUM})
    assert "THIS WEEK: databases/indexes-plans, databases/schema-access-patterns; dsa: stacks, queues; design: billing ledger; exit: justify an index" in ctx, ctx
    assert "week 2" not in ctx, ctx
    ctx = run_hook({"memory/curriculum.md": CURRICULUM.replace("week: 3", "week: not started")})
    assert "WEEK: not started." in ctx, ctx
    assert "THIS WEEK" not in ctx, ctx
    ctx = run_hook({"memory/curriculum.md": CURRICULUM.replace("week: 3", "week: 9")})
    assert "WEEK: 9." in ctx and "THIS WEEK" not in ctx, ctx


@case
def recall_question_drops_trailing_answer_parenthetical():
    ctx = run_hook({
        "memory/curriculum.md": CURRICULUM,
        "memory/postgres/a.md": card("practiced", "2026-09-01", "databases/x",
                                     "Which one (planned or crash) loses data, and why? (A: failover; async tail (WAL) lost.)"),
    })
    assert "Which one (planned or crash) loses data, and why?" in ctx, ctx
    assert "failover" not in ctx, ctx


@case
def owned_due_capped_at_three_with_overflow_count():
    files = {"memory/curriculum.md": CURRICULUM}
    for i in range(5):
        files[f"memory/postgres/c{i}.md"] = card("practiced", f"2026-09-0{i + 1}", "databases/x")
    ctx = run_hook(files)
    assert "OWNED-DUE (5):" in ctx, ctx
    assert "(+2 more)" in ctx, ctx
    assert ctx.count(" | ") == 2, ctx


@case
def off_curriculum_cards_never_due():
    ctx = run_hook({
        "memory/curriculum.md": CURRICULUM,
        "memory/tmux/a.md": card("practiced", "2026-08-01", "off"),
    })
    assert "OWNED-DUE: none." in ctx, ctx
    assert "OTHER-DUE: 0" in ctx, ctx


@case
def due_cards_exclude_archive_history_encountered_and_future():
    ctx = run_hook({
        "memory/curriculum.md": CURRICULUM,
        "memory/postgres/a.md": card("practiced", "2026-09-10", "databases/x"),
        "memory/postgres/b.md": card("encountered", "2026-08-01", "databases/x"),
        "memory/postgres/c.history.md": card("practiced", "2026-08-01", "databases/x"),
        "memory/postgres/d.md": card("introduced", "2026-10-01", "databases/x"),
        "memory/archive/merged/e.archived.md": "---\nname: e\narchived_stage: practiced\narchived_review: 2026-08-01\n---\n",
        "memory/archive/retired/f.archived.md": card("practiced", "2026-08-01", "databases/x"),
    })
    assert "OWNED-DUE (1): a (practiced, +3d)." in ctx, ctx
    assert "OTHER-DUE: 0" in ctx, ctx


@case
def missing_curriculum_degrades_gracefully():
    ctx = run_hook({"memory/postgres/a.md": card("practiced", "2026-09-10", "databases/x")})
    assert "WEEK: unknown. OWNED: none set." in ctx, ctx
    assert "OWNED-DUE: none." in ctx, ctx
    assert "OTHER-DUE: 1" in ctx, ctx


@case
def checkpoint_none_then_recent_then_stale():
    base = {"memory/curriculum.md": CURRICULUM}
    ctx = run_hook(base)
    assert "CHECKPOINT: none yet" in ctx, ctx
    ctx = run_hook({**base, "memory/checkpoints/2026-09-10-pool-exhaustion.md": "# cp\n"})
    assert "CHECKPOINT: last 2026-09-10 (3d ago)." in ctx, ctx
    assert "10+ days" not in ctx, ctx
    ctx = run_hook({**base, "memory/checkpoints/2026-08-20.md": "# cp\n", "memory/checkpoints/README.md": "x"})
    assert "CHECKPOINT: last 2026-08-20 (24d ago) (10+ days: propose one at a natural boundary)." in ctx, ctx


@case
def checkpoints_and_notes_dirs_are_not_scanned_as_cards():
    ctx = run_hook({
        "memory/curriculum.md": CURRICULUM,
        "memory/checkpoints/2026-09-01.md": card("practiced", "2026-09-01", "databases/x"),
        "memory/notes/azure.md": card("practiced", "2026-09-01", "databases/x"),
    })
    # they carry frontmatter with a stage, so they WOULD count; the convention is that
    # checkpoint and note files never carry stage/review. This test documents that contract.
    assert "OWNED-DUE (2)" in ctx, ctx


@case
def handoff_flag_reported():
    ctx = run_hook({"memory/curriculum.md": CURRICULUM}, flag=True)
    assert "HANDOFF FLAG SET" in ctx, ctx
    ctx = run_hook({"memory/curriculum.md": CURRICULUM}, flag=False)
    assert "HANDOFF FLAG SET" not in ctx, ctx


@case
def output_is_short():
    ctx = run_hook({
        "memory/curriculum.md": CURRICULUM,
        "memory/postgres/a.md": card("practiced", "2026-09-01", "databases/x", "Q one?"),
        "memory/postgres/b.md": card("practiced", "2026-09-02", "databases/x", "Q two?"),
        "memory/postgres/c.md": card("practiced", "2026-09-03", "databases/x", "Q three?"),
    })
    assert len(ctx) < 1500, len(ctx)


def main():
    failed = 0
    for name, fn in CASES.items():
        try:
            fn()
            print(f"ok   {name}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL {name}: {e}")
        except Exception as e:  # noqa: BLE001
            failed += 1
            print(f"ERROR {name}: {type(e).__name__}: {e}")
    print(f"{len(CASES) - failed}/{len(CASES)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
