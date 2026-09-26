#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Validate YAML frontmatter in Markdown files with a real YAML parser.

Usage:
    scripts/validate-frontmatter.py [PATH ...]      # default: memory/ skills/ docs/ mentor/ README.md
    scripts/validate-frontmatter.py --require-keys name,description PATH

Exit 1 on any parse error (or missing required key). Prints file + error.
Files without a leading '---' are skipped (no frontmatter is not an error).
Run from anywhere; paths are relative to cwd or absolute.
"""
from __future__ import annotations

import argparse
import os
import sys

import yaml

DEFAULT_ROOTS = ["memory", "skills", "docs", "mentor", "README.md"]


def iter_markdown(paths: list[str]):
    for p in paths:
        if os.path.isfile(p):
            if p.endswith(".md"):
                yield p
            continue
        for root, dirs, files in os.walk(p):
            dirs[:] = [d for d in dirs if not d.startswith(".")]
            for f in sorted(files):
                if f.endswith(".md"):
                    yield os.path.join(root, f)


def split_frontmatter(text: str):
    """Return (yaml_text, found). Frontmatter = '---\\n' ... '\\n---' at file start."""
    if not text.startswith("---"):
        return None, False
    first_nl = text.find("\n")
    if first_nl == -1 or text[:first_nl].strip() != "---":
        return None, False
    rest = text[first_nl + 1 :]
    lines = rest.split("\n")
    for i, line in enumerate(lines):
        if line.strip() == "---":
            return "\n".join(lines[:i]), True
    return None, True  # opened, never closed


def check(path: str, required: list[str]) -> list[str]:
    errors = []
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as e:
        return [f"{path}: cannot read ({e})"]
    body, found = split_frontmatter(text)
    if not found:
        return []
    if body is None:
        return [f"{path}: frontmatter opened with '---' but never closed"]
    try:
        data = yaml.safe_load(body)
    except yaml.YAMLError as e:
        msg = str(e).replace("\n", " | ")
        return [f"{path}: YAML error: {msg}"]
    if data is None:
        data = {}
    if not isinstance(data, dict):
        return [f"{path}: frontmatter is not a mapping (got {type(data).__name__})"]
    for key in required:
        if key not in data or data[key] in (None, ""):
            errors.append(f"{path}: missing required key '{key}'")
    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--require-keys", default="", help="comma-separated keys every frontmatter must define")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    paths = args.paths or [p for p in DEFAULT_ROOTS if os.path.exists(p)]
    required = [k for k in args.require_keys.split(",") if k]
    checked = 0
    errors: list[str] = []
    for md in iter_markdown(paths):
        checked += 1
        errors.extend(check(md, required))
    for e in errors:
        print(e)
    if not args.quiet:
        print(f"frontmatter: {checked} files checked, {len(errors)} error(s)", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
