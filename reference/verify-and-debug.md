# Verify Against Reality, and Hunt Silent Failures

## Verify against reality, never memory

Before any factual claim about the system, check the actual source. The
pattern is always: state that you are checking, run the check, then answer from
what you saw.

- Schema / column names: read `pragma_table_info`, the model, or the migration.
  Do not guess `carrier_id` when it is `id`.
- Endpoint routes and payload shapes: read the route decorator and the payload
  builder, not your recollection of them.
- Data coverage or counts: query the database, do not estimate.
- Config, env, and file locations: read them.

Wrong-from-memory answers are the most expensive kind, because they look
authoritative. A ten-second grep beats a confident mistake every time.

## The silent-failure hunt

Real bugs often pass every happy-path check. Look specifically for output that
is plausible but false:

- **Swallowed exceptions.** `except: pass`, empty catch blocks, functions that
  return a default on error without logging. Grep for them. Each one can hide a
  real failure behind a normal-looking result.
- **Credential death mid-run.** A batch job whose API key runs out of credits
  partway through can cache error strings as if they were verdicts, and the run
  still reads as complete. Add a FATAL kill switch: on a billing or auth error,
  stop pulling work, leave remaining rows untouched (queued for next run), and
  exit non-zero with a summary. A partial failure must never look clean.
- **Frozen error rows.** If failed rows are cached and a refresh TTL then skips
  anything "recently checked," a transient failure freezes for the whole TTL.
  Make error rows always eligible for retry.
- **Displayed-but-empty signals.** A field wired into the UI that is populated
  on 0% of rows is filler. If it self-hides when empty it is merely dead code;
  if it renders an empty label or is advertised as a searchable capability that
  returns nothing, it actively misleads. Audit before trusting.
- **Fabricated / seeded data labeled real.** Seed data (fictional phone numbers
  in a reserved range, placeholder contacts) marked "verified" is the Trust
  Gap. Detect it (e.g. a phone in an official fiction range is never real
  whatever the source column claims) and label it honestly.
- **Stray-directory writes.** A `cat >> file` or a relative path run from the
  wrong working directory lands in the wrong file silently. After shell writes,
  confirm the change landed where intended (grep the target).

Always end a long or batch run with a verdict/error summary and a non-zero exit
on abort, so the outcome is legible without reading the whole log.

## The coverage audit

Before shipping a signal or trusting a field, count real coverage:

```
for each displayed signal:
  count rows where the field is non-null AND not a placeholder
      ("not found", "none", "n/a", "-", empty)
  report both overall and among the rows the user actually sees
      (e.g. the sellable / in-scope subset, not the whole table)
```

Sort the result. The near-zero ones are either dead miners (built, no data
yet) or genuinely misleading if advertised. The high-coverage ones are your
workhorses. This is a fast query and it repeatedly finds filler that a feature
demo would have presented as substance.

## Regression discipline before piling on more code

- Keep per-module self-tests and run them after each change.
- Keep byte-level baselines for anything order- or output-sensitive; a
  deliberate change re-baselines, an accidental diff is caught.
- Typecheck the frontend after every edit.
- New work should be additive: a change that grows the output is safer to
  verify than one that mutates shared logic. When it must mutate shared logic,
  re-run the regression gate first.

## Long-running miners / batch jobs

- **Per-row commits.** Never hold a write transaction open across a network
  fetch. A miner that commits every 20 rows while fetching can hold a database
  writer lock for a minute and block the app. Commit each row.
- **Own connection per worker.** Parallel workers each get their own DB
  connection; never share one across threads.
- **Resumable.** Stamp each row checked (even a miss, as "looked, found
  nothing") so a killed run keeps everything already paid for and never
  re-probes.
- **Honest miss vs error.** A miss is stamped and skipped next time. A
  transient error is NOT stamped, so it retries.

## Regex and parsing traps

Validate extraction patterns against real pages, not just the happy example. A
loose pattern for a UK postcode matched CSS hex colors (`E2C4AC`) as fake
postcodes; requiring the mandatory space and a valid inward code fixed it. When
you build an extractor, deliberately test the false-positive it is most likely
to hit and assert it is rejected.
