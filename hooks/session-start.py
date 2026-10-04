#!/usr/bin/env python3
"""SessionStart hook: inject live learning-ledger state (short, dynamic).

Reports: curriculum week and owned areas (memory/curriculum.md), due cards in
owned areas (up to 3, with their recall question), count of other due cards,
days since the last checkpoint (memory/checkpoints/YYYY-MM-DD*.md), and whether
the hand-off flag that opens the investigation gate is still set.
The behavioral contract lives in CLAUDE.md, not here.

Pure stdlib. Never raises: parse problems degrade to "unknown".
Env overrides for tests: CLAUDE_HOME (default ~/.claude), LEDGER_TODAY (YYYY-MM-DD).
"""
import datetime as dt
import json
import os
import re
import sys

HOME = os.environ.get("CLAUDE_HOME") or os.path.expanduser("~/.claude")
MEM = os.path.join(HOME, "memory")
FLAG = os.path.join(HOME, ".handoff-active")
ACTIVE = {"introduced", "practiced", "retrievable", "transferable"}
MAX_OWNED = 3

HEADER = (
    "Learning ledger: PAIR default, SHIP only via /ship (contract ~/.claude/CLAUDE.md, rules "
    "~/.claude/memory/convention.md, direction ~/.claude/memory/curriculum.md). In owned areas the learner's hypothesis "
    "or approach comes first and Claude reviews. One OWNED-DUE card is asked at the first natural boundary of a "
    "substantive session, in generation form; 'not today' ends it for the session. Other due cards: contextual only."
)


def today():
    raw = os.environ.get("LEDGER_TODAY")
    if raw:
        return dt.date.fromisoformat(raw)
    return dt.date.today()


def read(path, limit=None):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read(limit) if limit else f.read()
    except OSError:
        return ""


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_]+):\s*(.*?)\s*$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip('"').strip("'")
    return fm


def recall_question(text):
    """The card's recall question without its answer: cards write the answer as a trailing
    parenthetical, which must not reach the session (it would turn retrieval into recognition)."""
    m = re.search(r"\*\*Recall question:\*\*\s*(.+)", text)
    if not m:
        return ""
    q = m.group(1).strip()
    if q.endswith(")"):
        depth, i = 0, len(q) - 1
        while i >= 0:
            depth += 1 if q[i] == ")" else -1 if q[i] == "(" else 0
            if depth == 0:
                q = q[:i].rstrip()
                break
            i -= 1
    return q[:220] + ("..." if len(q) > 220 else "")


def curriculum():
    """Return {week, owned: [areas], week_line} from memory/curriculum.md; empty values when absent.
    week_line is the `- week N: ...` entry matching the current week (nodes, dsa pattern, design work)."""
    text = read(os.path.join(MEM, "curriculum.md"))
    out = {"week": "", "owned": [], "week_line": ""}
    m = re.search(r"^week:\s*(.+?)\s*$", text, re.M)
    if m:
        out["week"] = m.group(1)
    m = re.search(r"^owned:\s*(.+?)\s*$", text, re.M)
    if m:
        out["owned"] = [a.strip() for a in m.group(1).split(",") if a.strip()]
    if re.match(r"^\d+$", out["week"]):
        m = re.search(r"^- week " + out["week"] + r":\s*(.+?)\s*$", text, re.M)
        if m:
            out["week_line"] = m.group(1)
    return out


def due_cards(now, owned):
    """Active cards whose review date has passed, split into owned-area cards and the rest.
    Scans memory/<topic>/*.md only (archive/ is two levels deep, history notes carry no stage,
    checkpoints/ and notes/ carry no stage either, so all are skipped)."""
    owned_due, other_due = [], []
    if not os.path.isdir(MEM):
        return owned_due, other_due
    for topic in sorted(os.listdir(MEM)):
        tdir = os.path.join(MEM, topic)
        if not os.path.isdir(tdir) or topic.startswith(".") or topic == "archive":
            continue
        for name in sorted(os.listdir(tdir)):
            if not name.endswith(".md") or name.endswith(".history.md"):
                continue
            text = read(os.path.join(tdir, name), 6000)
            fm = parse_frontmatter(text)
            stage = fm.get("stage", "")
            review = fm.get("review", "")
            if stage not in ACTIVE or not re.match(r"^\d{4}-\d{2}-\d{2}$", review):
                continue
            try:
                rdate = dt.date.fromisoformat(review)
            except ValueError:
                continue
            overdue = (now - rdate).days
            if overdue < 0:
                continue
            node = fm.get("curriculum", "")
            area = node.split("/", 1)[0] if node else ""
            if node == "off":
                continue
            slug = name[:-3]
            if area and area in owned:
                q = recall_question(text)
                owned_due.append((overdue, f"{slug} ({stage}, +{overdue}d)" + (f": {q}" if q else "")))
            else:
                other_due.append((overdue, slug))
    owned_due.sort(reverse=True)
    other_due.sort(reverse=True)
    return [s for _, s in owned_due], [s for _, s in other_due]


def checkpoint_state(now):
    cdir = os.path.join(MEM, "checkpoints")
    if not os.path.isdir(cdir):
        return "CHECKPOINT: none yet (propose a 20 to 30 minute one at a natural boundary)."
    dates = []
    for name in os.listdir(cdir):
        m = re.match(r"^(\d{4}-\d{2}-\d{2})", name)
        if m and name.endswith(".md"):
            try:
                dates.append(dt.date.fromisoformat(m.group(1)))
            except ValueError:
                pass
    if not dates:
        return "CHECKPOINT: none yet (propose a 20 to 30 minute one at a natural boundary)."
    last = max(dates)
    days = (now - last).days
    tail = " (10+ days: propose one at a natural boundary)" if days >= 10 else ""
    return f"CHECKPOINT: last {last.isoformat()} ({days}d ago){tail}."


def build(now):
    parts = [HEADER]
    try:
        cur = curriculum()
        week = cur["week"] or "unknown"
        owned = cur["owned"]
        parts.append(f"WEEK: {week}. OWNED: {', '.join(owned) if owned else 'none set'}.")
        if cur["week_line"]:
            parts.append(f"THIS WEEK: {cur['week_line']} (work touching these nodes is the rep; checkpoints may target them).")
        owned_due, other_due = due_cards(now, set(owned))
        if owned_due:
            shown = owned_due[:MAX_OWNED]
            more = f" (+{len(owned_due) - MAX_OWNED} more)" if len(owned_due) > MAX_OWNED else ""
            parts.append(f"OWNED-DUE ({len(owned_due)}): " + " | ".join(shown) + more + ".")
        else:
            parts.append("OWNED-DUE: none.")
        parts.append(f"OTHER-DUE: {len(other_due)} (contextual only).")
    except Exception as e:  # noqa: BLE001
        parts.append(f"DUE: unknown ({type(e).__name__}).")
    try:
        parts.append(checkpoint_state(now))
    except Exception as e:  # noqa: BLE001
        parts.append(f"CHECKPOINT: unknown ({type(e).__name__}).")
    if os.path.exists(FLAG):
        parts.append("HANDOFF FLAG SET: the investigation gate is open, left over from an earlier /ship or 'run it'. "
                     "Say so and clear it (rm ~/.claude/.handoff-active).")
    return " ".join(parts)


def main():
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": build(today())}}))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart",
                                                 "additionalContext": HEADER + f" (hook state error: {type(e).__name__})"}}))
        sys.exit(0)
