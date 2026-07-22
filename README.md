<h1 align="center">Plumbline</h1>

<p align="center">
  <strong>A Claude Code skill that makes your AI build the whole product, then hold it against reality before calling it done.</strong><br>
  Verify against reality instead of memory. Hunt the silent failures. Say what is real, seeded, or modeled. Ship reversibly.
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
  <img alt="Claude Code Skill" src="https://img.shields.io/badge/Claude%20Code-Skill-6C3EF5">
  <img alt="Agent Skill spec" src="https://img.shields.io/badge/Agent%20Skills-compatible-0aa">
  <a href="#validate"><img alt="Validator" src="https://img.shields.io/badge/skill-validated-brightgreen"></a>
</p>

---

A plumbline is the builder's tool that shows what is truly vertical, not what
merely looks straight. Coding agents are fast builders that also confidently
produce work that looks right and is quietly wrong: a swallowed exception, a
field wired into the UI that is populated on 0% of rows, an API key that dies
mid-run and caches junk as if it were data, a seeded value labeled "verified."

Plumbline is the discipline that catches that. It turns Claude into a
cofounder-grade product partner that designs, builds, debugs, and ships across
the stack, and refuses to call something done until it has been exercised and
checked against the real code and data. Plausible output is not the goal.
Output that is true, exercised, and honest about its own limits is.

> **See it catch a real bug:** [plumbline-demo](https://github.com/suprenvb/plumbline-demo)
> is a 60-second hands-on demo. Clone it, point Claude at it, and watch Plumbline
> flag three defects that a green status report was hiding.

## Quickstart

```bash
git clone https://github.com/suprenvb/plumbline ~/.claude/skills/plumbline
```

That is the whole install. Open Claude Code and it loads automatically when the
work matches: building or shipping a feature end to end, debugging something
that looks fine but might be lying, a competitive UX teardown, a data-quality or
coverage audit, a build-vs-buy call, or preparing an honest stakeholder
deliverable. You can also invoke it by name with `/plumbline`.

## What it changes

Without Plumbline, an agent tends to answer from memory, ship the happy path,
and report "done" from having written plausible code. With it, the loop becomes:

```
UNDERSTAND -> SCOPE -> BUILD -> VERIFY -> SHIP -> REPORT
```

and two audits that are easy to skip and expensive to miss get run every time:
a **coverage audit** (what fraction of real rows does this signal actually fire
on) and a **silent-failure hunt** (what looks fine but is lying).

## The nine principles

1. **Verify against reality, never claim from memory.** Read the schema, query the DB, read the actual endpoint before answering.
2. **Honesty is a feature, not a caveat.** Label estimate vs measured, sample vs verified, seeded vs real.
3. **Hunt silent failures.** Swallowed exceptions, dead keys caching junk, 0%-populated fields. Add kill switches and end-of-run summaries.
4. **Audit coverage before you ship a signal.** Count real, non-placeholder coverage against the actual dataset.
5. **Ship reversibly, and verify before claiming done.** Branch, commit per chunk, exercise the flow, then deploy and confirm.
6. **Build-vs-buy at the field level.** Own the one thing a vendor structurally cannot give you.
7. **Design with restraint, informed by the category.** Competitive UX teardown before choosing a pattern.
8. **Ask only when scope genuinely diverges.** A days-vs-minutes fork earns one question. Otherwise pick the default and say so.
9. **Report like a partner.** What is real, what is seeded, what failed, what is next.

## What is inside

```
SKILL.md                        the 9 principles, the UNDERSTAND -> REPORT arc, the reference index
reference/verify-and-debug.md   verifying against reality, the silent-failure hunt, coverage audits
reference/product-and-data.md   competitive UX teardowns, the honesty tags, build-vs-buy at field level
reference/ship-and-report.md    branch/verify/deploy hygiene, the partner-grade report
reference/github-rollup.md      curated catalog of skills to reuse or compose with
scripts/validate_skill.py       validates frontmatter, body length, references, house style
```

Progressive disclosure keeps the always-loaded footprint small: only `SKILL.md`
rides in context by default, and each reference file loads when its phase comes up.

## Composes with, does not replace

Plumbline is the connective honesty layer. It expects you to bring depth skills
alongside it:

- [`obra/superpowers`](https://github.com/obra/superpowers) for methodology
  (`systematic-debugging`, `test-driven-development`, `writing-plans`).
- A per-framework bundle such as
  [`Jeffallan/claude-skills`](https://github.com/Jeffallan/claude-skills) for stack depth.
- A review fleet such as
  [`anthropics/claude-code-security-review`](https://github.com/anthropics/claude-code-security-review)
  for a hard security gate.

See [reference/github-rollup.md](reference/github-rollup.md) for the surveyed
landscape and where each existing repo fits. The short version: the ecosystem is
saturated on breadth and generic code review, but honesty-and-coverage auditing,
silent-failure hunting as the primary job, and field-level build-vs-buy are
essentially unbuilt. That gap is what this skill fills.

## Use it in a project (team-shared)

Drop it into a repo so everyone on the team gets it:

```bash
git clone https://github.com/suprenvb/plumbline .claude/skills/plumbline
```

## Validate

```bash
python3 scripts/validate_skill.py
```

Checks frontmatter, body length, that every reference file resolves, and house
style. Run it before committing a change to the skill.

### Optional CI

A ready-to-use GitHub Actions workflow lives on disk at
`.github/workflows/validate.yml`. Pushing a workflow file needs a token with the
`workflow` scope, so it is not committed by default. To turn on CI:

```bash
gh auth refresh -s workflow
git add .github/workflows/validate.yml
git commit -m "ci: run skill validator on push"
git push
```

## Contributing

Issues and PRs welcome. Keep the house style: no em-dashes, explain the *why*
behind an instruction rather than piling on rigid rules, and run the validator
before you push.

## Author

Built by Grayson Valashinas. Say hi on
[LinkedIn](https://linkedin.com/in/grayson-valashinas).

## License

MIT. See [LICENSE](LICENSE).
