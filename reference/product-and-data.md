# Product Design, Data Honesty, and Build-vs-Buy

## Competitive UX teardown before choosing a pattern

When deciding how to present data or design a surface, study how the best
products in the category solve the same problem first. Split the study into two
clusters: direct category peers (whoever sells to the same buyer) and craft
exemplars (premium products in adjacent spaces whose polish is worth stealing).

For each, extract concretely, not generically:
- the primary on-screen unit (card, row, table, feed, chat)
- how they make dense data digestible (one-number summary, plain-word label
  alongside a precise value, badges, progressive disclosure)
- how they earn trust in the output (cite every claim to a source, show your
  work, human-ratification affordances)
- what they deliberately avoid (walls of raw numbers, exposed model
  probabilities, black-box output, saturated color everywhere)

Then produce: similarities (the category conventions), unique factors (what
each owns), the shared no-nos, where your product already overlaps, and where
the honest gaps are. Rank the gaps and fix the trust-breaking one first.

Patterns that recur across strong data products, worth reusing:
- **Dual-encode a score:** a precise value for sorting plus a plain word for
  glancing. Never ship the raw model number alone.
- **The table is the trust primitive:** one row per item, columns you define,
  every cell cited to its source, so a user can audit fast and reject one cell
  without rejecting the whole answer.
- **Spend one accent color,** on the action and the number that must be
  verified, nothing else.
- **Self-hiding empty states:** a field with no data renders nothing, never an
  empty label.

## The honesty tags

Make provenance a first-class, visible property, not a footnote:

- **Sample vs Verified** on contact or any human-entered data. Compute Verified
  strictly (real, checked, not in a known-fake range); everything else is
  Sample. Never let a seeded value inherit a "verified" label from a source
  column.
- **Estimate vs Measured** on any number that is modeled. If revenue or volume
  is a vendor's traffic-based estimate, say so, and cross-check it with an
  independent signal you control.
- **Confidence labels** (corroborated / estimated / low) rather than a fake
  precision percentage.
- **Freshness stamps** ("checked <date>") on every mined field, so nothing
  pretends to be real-time.
- **Cited source** on every claim, clickable where possible.

The rule: a reader should never be able to discover that a confident-looking
value is actually weak. Tell them first.

## Build-vs-buy at the field level

When a data vendor's cost or quality is questioned, do not answer at the level
of the whole product. Decompose:

1. List the fields you actually pull and, grounded in the code, which ones
   drive decisions vs which are display.
2. For each load-bearing field, classify the vendor's method: scraped-direct
   (reliable), modeled/estimated (directional), or third-party enriched (thin).
3. Rate replicability: could you produce this yourself, and how hard.
4. Find the one thing that is genuinely hard to replicate. Usually it is not a
   field at all, it is a capability (discovery, enumeration, scale). That is
   what you are actually paying for.
5. Recommend: keep buying the hard-to-replicate capability, replace the weak
   modeled field with your own derivation, and spend build effort on the metric
   the vendor structurally cannot give you (that is your moat).

The trap to avoid: conflating a weak field (a modeled estimate) with the whole
product, and concluding "it is just estimates, do it ourselves" when the value
was never the estimate.

## Data provenance write-ups

For a stakeholder, document where data comes from so it is defensible:
- a data dictionary (field, data type, category, source, one-line description),
  metadata-only so it is safe to share (no PII)
- a source-provenance report for the biggest vendor: how they collect it, which
  fields are hard vs modeled, freshness, accuracy per third-party review, the
  compliance gaps worth confirming directly

Mark every claim as directly-stated, modeled, or inference. The honest framing
usually turns a dependency into a moat argument: you buy the census, you own
the ground truth they cannot produce.

## Scope questions worth asking

Ask a focused question only when the answer changes the build materially:
- real integration vs stub (days vs minutes, needs credentials/sandboxes)
- whole-repo sweep vs one file
- what belongs in a shared artifact vs stays internal (PII, candid quotes)

Give 2-4 concrete options with the trade-off on each, lead with the
recommendation, and proceed on the answer. For everything else, pick the
sensible default and state it.
