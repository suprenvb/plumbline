# GitHub Skill-Repo Rollup

A curated catalog of Claude Code / Agent Skills repos worth reusing or
composing with, rather than reinventing. Use it two ways: to pull in an
existing skill for a job this one does not cover deeply (a specific framework,
a security review), and to know what already exists before authoring something
new. Star counts were observed 2026-07-22 via the GitHub API; treat exact
magnitudes as approximate, the relative standing is what matters.

## Canonical / official (the format source of truth)

- `anthropics/skills` : the spec, the SKILL.md template, the document skills
  (docx/pdf/pptx/xlsx), and example skills. Cite this for the format.
- `anthropics/claude-plugins-official` : home of the `skill-creator` meta-skill
  that scaffolds, refines, and evals skills.
- `agentskills/agentskills` (agentskills.io) : the vendor-neutral open spec, if
  portability across Codex/Gemini/Cursor matters.

## Methodology (reuse, do not rewrite)

- `obra/superpowers` : the dominant methodology layer. Its `test-driven-
  development`, `systematic-debugging`, `writing-plans`, and
  `verification-before-completion` skills are the ones this partner composes
  with. Do not re-implement them here; call them.
- `obra/superpowers-marketplace` : the install front door for the above.

## Full-stack engineering bundles (per-framework depth)

- `Jeffallan/claude-skills` : 66 curated specialist skills (languages, backend
  and frontend frameworks incl. Next.js, infra, testing, DevOps). Best single
  pick when you need current per-framework expertise this skill does not carry.
- `jezweb/claude-skills` : a real shipping stack (Cloudflare Workers, Vite+
  React, Hono, D1/Drizzle, Tailwind v4, shadcn/ui, Stripe). Good if your stack
  matches.
- `alirezarezvani/claude-skills` : 330+ skills, the broadest bundle. Mine it for
  anything the curated sets miss; expect noise.

## Debugging / review / quality (compose for a hard review)

- `anthropics/claude-code-security-review` : official diff-aware security review
  GitHub Action. The trustworthy security gate.
- `awesome-skills/code-review-skill` : a strong four-phase, framework-aware
  reviewer.
- `tag1consulting/claude-comprehensive-review` : a fleet of specialist review
  agents, including a `silent-failure-hunter` and `edge-case-hunter`. The
  closest public analog to this skill's silent-failure discipline; read it for
  structure, then apply the coverage-audit and honesty layers this skill adds.
- `HermeticOrmus/code-review-skills` : classify the code first, then run that
  domain's real failure modes. A good framing to borrow.

## Product / UX / design (the strategy and teardown layer)

- `wondelai/skills` : the strongest product-and-UX-thinking bundle. Turns Jobs
  to Be Done, The Mom Test, and Refactoring UI into structured workflows with
  real reference docs. Reach for it when the task is discovery or heuristic UX
  review, upstream of the competitive teardown this skill runs.
- `wilwaldon/Claude-Code-Frontend-Design-Toolkit` : tools and CLAUDE.md tricks
  that measurably improve frontend output on current React/Next/Tailwind.

## Data / analytics (query engines, not provenance)

- `duckdb/duckdb-skills` : zero-infra analytical SQL over local files. Useful
  for the coverage audits this skill calls for.
- `nimrodfisher/data-analytics-skills` : analyst workflow incl. data-quality
  checks. Closest public repo to data-quality-first, but note it stops short of
  provenance and coverage-completeness, which this skill treats as first-class.

## Deploy / DevOps

- `BagelHole/DevOps-Security-Agent-Skills` : 80+ K8s/Terraform/cloud skills with
  runnable configs and SOC2/ISO playbooks. Overkill for a solo product build;
  the DevOps subset inside `Jeffallan/claude-skills` is usually enough.

## Meta-indexes (when hunting for a specific skill)

- `hesreallyhim/awesome-claude-code` : the canonical Claude Code index. Start here.
- `ComposioHQ/awesome-claude-skills` : largest raw breadth, 1000+ entries.

## Authoring / validation tooling

- `davila7/claude-code-templates` : the most-adopted discovery/install CLI.
- `himself65/skill-lint` and `skill-tools/skill-tools-plugin` : validate a
  SKILL.md (name format, description length, frontmatter) before shipping. Worth
  wiring into your own authoring loop.
- `zantific/skill-security-review-lens` : scans third-party SKILL.md files
  before you install them. Use it before adopting any skill from this list.

## What this skill fills that none of the above do

The ecosystem is saturated on breadth and on generic code review, but three
product-critical capabilities are essentially unbuilt as first-class skills, and
they are exactly this skill's core:

1. **Honesty and data-coverage auditing.** Nothing else verifies claims against
   the real code and data instead of the model's memory, or audits what fraction
   of real cases a signal actually handles before it ships.
2. **Silent-failure hunting as the primary job**, not one agent among many.
3. **Build-vs-buy decisioning** with an honest cost, coverage, and maintenance
   comparison.

So this skill is not a replacement for the catalog above. It is the connective
honesty-first discipline that sits on top of it: compose superpowers for
method, a framework bundle for stack depth, and a review fleet for breadth,
while this skill owns verification, coverage, provenance, and the build-vs-buy
call.
