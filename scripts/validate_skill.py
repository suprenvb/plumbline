#!/usr/bin/env python3
"""Validate the Plumbline skill.

Checks the things a broken skill fails on, so a green run here means the skill
will actually load and trigger:
  - SKILL.md exists and has parseable YAML frontmatter
  - frontmatter has a valid `name` (lowercase, digits, hyphens) and `description`
  - description is within the 1024-char metadata budget and non-trivial
  - SKILL.md body stays under the 500-line progressive-disclosure guideline
  - every reference/*.md pointed to from SKILL.md exists on disk
  - no em-dashes anywhere (a house style rule for this repo)

Exits non-zero on the first category with failures, printing every failure, so
CI shows exactly what to fix rather than a single opaque error.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DESC_MAX = 1024
BODY_MAX_LINES = 500


def fail(errors: list[str], msg: str) -> None:
    errors.append(msg)


def parse_frontmatter(text: str) -> dict[str, str]:
    """Minimal single-level YAML frontmatter reader (name/description only)."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end].strip("\n")
    out: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            out[key.strip()] = val.strip()
    return out


def main() -> int:
    errors: list[str] = []

    if not SKILL.exists():
        print("FAIL: SKILL.md not found at repo root", file=sys.stderr)
        return 1

    text = SKILL.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)

    name = fm.get("name", "")
    if not name:
        fail(errors, "frontmatter: missing `name`")
    elif not NAME_RE.match(name):
        fail(errors, f"frontmatter: `name` {name!r} must be lowercase letters, digits, hyphens")

    desc = fm.get("description", "")
    if not desc:
        fail(errors, "frontmatter: missing `description`")
    else:
        if len(desc) > DESC_MAX:
            fail(errors, f"frontmatter: description is {len(desc)} chars, max {DESC_MAX}")
        if len(desc) < 40:
            fail(errors, "frontmatter: description is too short to trigger reliably")

    # Body length (everything after the closing frontmatter fence).
    body_start = text.find("\n---", 3)
    body = text[body_start + 4 :] if body_start != -1 else text
    body_lines = body.count("\n") + 1
    if body_lines > BODY_MAX_LINES:
        fail(errors, f"SKILL.md body is {body_lines} lines, over the {BODY_MAX_LINES}-line guideline")

    # Every referenced reference/*.md must exist.
    for ref in re.findall(r"reference/([A-Za-z0-9_-]+\.md)", text):
        if not (ROOT / "reference" / ref).exists():
            fail(errors, f"SKILL.md points to reference/{ref} but the file is missing")

    # House style: no em-dashes in any tracked markdown.
    for md in sorted(ROOT.rglob("*.md")):
        for i, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if "—" in line:
                rel = md.relative_to(ROOT)
                fail(errors, f"em-dash in {rel}:{i}")

    if errors:
        print(f"validate_skill: {len(errors)} failure(s)\n", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    refs = sorted(p.name for p in (ROOT / "reference").glob("*.md"))
    print("validate_skill: OK")
    print(f"  name:        {name}")
    print(f"  description: {len(desc)} chars")
    print(f"  body:        {body_lines} lines")
    print(f"  references:  {', '.join(refs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
