# fullstack-product-partner

A Claude Code / Agent Skill that turns Claude into a cofounder-grade full-stack
product partner: it designs, builds, debugs, ships, and makes build-vs-buy calls
with an honesty-first discipline. The core idea is that plausible output is not
the goal. Output that is true, exercised, and honest about its own limits is.

## Why this exists

The skills ecosystem is saturated on breadth and on generic code review, but
three product-critical habits are essentially unbuilt as first-class skills:

1. **Honesty and data-coverage auditing.** Verify claims against the real code
   and data instead of the model's memory, and audit what fraction of real
   cases a signal actually handles before it ships.
2. **Silent-failure hunting as the primary job**, not one agent among many. The
   dangerous bugs pass every happy-path check: swallowed exceptions, a key
   dying mid-run and caching junk, a field displayed that is 0% populated.
3. **Build-vs-buy decisioning** at the field level, with an honest cost,
   coverage, and maintenance comparison.

This skill is the connective honesty-first discipline that sits on top of the
existing skill catalog. It does not replace per-framework or methodology skills.
It composes with them. See [reference/github-rollup.md](reference/github-rollup.md)
for the surveyed landscape and where each existing repo fits.

## The nine principles

1. Verify against reality, never claim from memory.
2. Honesty is a feature, not a caveat (label estimate vs measured, sample vs verified).
3. Hunt silent failures (add kill switches and end-of-run summaries).
4. Audit coverage before you ship a signal (count real, non-placeholder coverage).
5. Ship reversibly, and verify before claiming done (branch, commit, exercise the flow).
6. Build-vs-buy at the field level (own the one thing a vendor structurally cannot give you).
7. Design with restraint, informed by the category (competitive UX teardown first).
8. Ask only when scope genuinely diverges (a days-vs-minutes fork).
9. Report like a partner (what is real, what is seeded, what failed, what is next).

## Install

Clone straight into your personal skills directory:

```bash
git clone https://github.com/suprenvb/fullstack-product-partner \
  ~/.claude/skills/fullstack-product-partner
```

Or add it to a project so a team shares it:

```bash
git clone https://github.com/suprenvb/fullstack-product-partner \
  .claude/skills/fullstack-product-partner
```

Claude loads the skill automatically when the work matches the description
(building or shipping a feature end to end, debugging something that looks fine
but might be lying, a UX teardown, a data-quality or coverage audit, a
build-vs-buy call, or preparing an honest stakeholder deliverable). You can also
invoke it explicitly with `/fullstack-product-partner`.

## What is inside

```
SKILL.md                        the 9 principles, the UNDERSTAND -> SHIP arc, the reference index
reference/verify-and-debug.md   verifying against reality, the silent-failure hunt, coverage audits
reference/product-and-data.md   competitive UX teardowns, the honesty tags, build-vs-buy at field level
reference/ship-and-report.md    branch/verify/deploy hygiene, the partner-grade report
reference/github-rollup.md      curated catalog of skills to reuse or compose with
scripts/validate_skill.py       validates frontmatter, body length, references, house style
```

## Composes with

- [`obra/superpowers`](https://github.com/obra/superpowers) for methodology
  (`systematic-debugging`, `test-driven-development`, `writing-plans`).
- A per-framework bundle such as
  [`Jeffallan/claude-skills`](https://github.com/Jeffallan/claude-skills) for
  stack depth.
- A review fleet such as
  [`anthropics/claude-code-security-review`](https://github.com/anthropics/claude-code-security-review)
  for a hard security gate.

This skill owns verification, coverage, provenance, and the build-vs-buy call
on top of those.

## Validate

```bash
python3 scripts/validate_skill.py
```

This checks frontmatter, body length, that every reference file resolves, and
house style. Run it before you commit a change to the skill.

### Optional CI

A ready-to-use GitHub Actions workflow lives on disk at
`.github/workflows/validate.yml`. Pushing a workflow file needs a token with the
`workflow` scope, so it is not committed by default. To turn on CI:

```bash
gh auth refresh -s workflow          # one-time, grants the scope
git add .github/workflows/validate.yml
git commit -m "ci: run skill validator on push"
git push
```

## License

MIT. See [LICENSE](LICENSE).
