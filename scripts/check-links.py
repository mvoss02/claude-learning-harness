#!/usr/bin/env python3
"""Check wikilinks and alias collisions in the learning ledger. Stdlib only.

Usage: scripts/check-links.py [--strict]

Checks (under ~/.claude/memory, or $LEDGER_DIR):
  1. Every basename is unique across active + history + archived notes.
  2. No archived file basename equals an active card's alias (aliases must win).
  3. Every [[wikilink]] in active cards resolves to a basename or alias.
     Unresolved links are reported as warnings (the convention allows links to
     not-yet-written notes); --strict turns them into errors.
  4. index.md lists exactly the active cards (files with a `stage:` key outside archive/).
Exit 1 on any error.
"""
from __future__ import annotations

import os
import re
import sys

LEDGER = os.environ.get("LEDGER_DIR", os.path.expanduser("~/.claude/memory"))
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")


def frontmatter(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_]+):\s*(.*?)\s*$", line)
        if m:
            fm[m.group(1)] = m.group(2)
    return fm


def aliases(fm: dict) -> list[str]:
    raw = fm.get("aliases", "")
    raw = raw.strip().strip("[]")
    return [a.strip().strip("'\"") for a in raw.split(",") if a.strip()]


def main() -> int:
    strict = "--strict" in sys.argv
    errors, warnings = [], []
    basenames: dict[str, str] = {}
    alias_owner: dict[str, str] = {}
    active: dict[str, str] = {}  # slug -> relpath
    archived: set[str] = set()
    links: list[tuple[str, str]] = []

    for root, dirs, files in os.walk(LEDGER):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, LEDGER)
            base = f[:-3]
            if base in basenames:
                errors.append(f"duplicate basename '{base}': {rel} and {basenames[base]}")
            basenames[base] = rel
            fm = frontmatter(path)
            is_archived = rel.startswith("archive" + os.sep)
            if is_archived:
                archived.add(base)
                if "stage" in fm or "review" in fm:
                    errors.append(f"archived note still carries stage/review: {rel}")
                continue
            for a in aliases(fm):
                if a in alias_owner and alias_owner[a] != rel:
                    errors.append(f"alias '{a}' claimed by {rel} and {alias_owner[a]}")
                alias_owner[a] = rel
            if "stage" in fm and rel not in ("index.md",):
                active[base] = rel
            with open(path, encoding="utf-8") as fh:
                for m in LINK_RE.finditer(fh.read()):
                    links.append((rel, m.group(1).strip()))

    for a, owner in alias_owner.items():
        if a in archived:
            errors.append(f"alias '{a}' on {owner} collides with archived basename '{a}' (rename the archive file)")
        if a in basenames and basenames[a] != owner:
            errors.append(f"alias '{a}' on {owner} collides with existing file {basenames[a]}")

    resolvable = set(basenames) | set(alias_owner)
    placeholders = {"slug", "concept", "not-yet-written"}
    for src, target in links:
        if target in placeholders or "<" in target:
            continue
        if target not in resolvable:
            (errors if strict else warnings).append(f"unresolved link [[{target}]] in {src}")

    index = os.path.join(LEDGER, "index.md")
    if os.path.exists(index):
        with open(index, encoding="utf-8") as fh:
            listed = set(re.findall(r"^- \[([^\]]+)\]\(", fh.read(), re.M))
        for slug in sorted(active):
            if slug not in listed:
                errors.append(f"index.md missing active card '{slug}' ({active[slug]})")
        for slug in sorted(listed - set(active)):
            errors.append(f"index.md lists '{slug}' but no active card has that basename")

    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("error:", e)
    print(f"links: {len(active)} active cards, {len(archived)} archived, {len(links)} links, "
          f"{len(errors)} error(s), {len(warnings)} warning(s)", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
