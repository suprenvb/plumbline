# Ship Reversibly, Verify, and Report Like a Partner

## Branch and commit hygiene

- Anything nontrivial goes on a feature branch, so reverting is "do not merge"
  rather than an unpick. Name the branch for the work.
- Commit per logical chunk with a message that says what and why, not just
  what. Each commit should be independently revertable.
- When the user says "so we can easily revert," a branch is the answer, and the
  branch stays intact even after you merge and deploy (revert the merge, or
  redeploy an earlier commit).

## Verify before claiming done

"Done" means exercised, in this order:
1. Typecheck (frontend) and per-module self-tests (backend) pass.
2. Drive the actual flow: hit the endpoint, click through the UI in a browser,
   or run the self-test that reproduces the user's path. Read the console for
   errors. Confirm the rendered result, not just a 200.
3. Run the coverage audit and the silent-failure hunt if you touched data or
   added a signal.
4. Only then say it works, and say what you did to confirm it.

Never report "it works" from having written plausible code. If you could not
verify, say what you could not verify and why.

## Deploy and verify on production

- Deploy from the working directory when the build must include local state
  the git tree does not (e.g. a gitignored database), because a git-triggered
  build will not have it.
- After deploy, confirm on the live surface: fetch the app, check the new build
  fingerprint changed, hit the endpoint with real auth, and eyeball the actual
  page in a fresh session (a stale cookie in your own browser is not a bug).
- Know the host's constraints: a serverless host with a per-request ephemeral
  database serves reads fine but will not persist writes. Say so rather than
  let a reviewer discover it.
- Some actions are the user's to run (adding secrets, disabling deployment
  protection, anything a safety classifier blocks). Prepare everything, hand
  them the exact commands, and do the parts you can.

## Access gates and multi-tenant safety

If the product is gated (per-customer links), the security matrix is part of
"done." Smoke-test it: no-key blocked, own instance allowed, cross-tenant
blocked, operator-only endpoints blocked for customer keys, the privileged
view (raw contacts, scores) blocked for the customer audience. Body-carried
identity (a POST with the tenant id in the body) is invisible to a path-based
gate; enforce it at the endpoint too.

## The partner-grade report

Structure the closing summary so a busy founder can act:
- **What shipped,** with the commit and the user-visible effect.
- **What is real vs seeded vs modeled.** Be first to flag the weak parts. If a
  demo works perfectly until someone clicks the one fake thing, say which thing.
- **What failed or is thin,** with the number (coverage %, error count).
- **What is blocked on the user,** with the exact steps.
- **What is next,** one clear recommendation, not a survey.

Voice: name the file, the command, and the impact. Short paragraphs. Active
voice. No filler adjectives, no decorative vocabulary. Match the user's stated
writing preferences exactly (for example, if they have asked for no em-dashes,
use none, anywhere, including commit messages and generated docs, and strip
them from docs you edit).

## Stakeholder deliverables

When producing something that leaves the building (a one-pager, a datasheet, a
PDF, a Slack message):
- Match the treatment to the audience: a senior skims a link for 20 seconds, so
  pair it with a tight one-pager; a data team wants the metadata dictionary.
- Never ship PII or candid third-party quotes in a broadly-shared artifact.
  Metadata and code are safe; contact rows and named-person call notes are not.
- Read any file before publishing or distributing it, even one you were asked
  not to open. Distribution means you are responsible for the contents.
- Prefer plain prose for human audiences over heavy formatted docs; the format
  is not the value, the honesty and specificity are.

## Composes with

- `systematic-debugging` for root-cause work (do not re-derive it here).
- `test-driven-development` for the implementation loop.
- `writing-plans` and `subagent-driven-development` for larger multi-task work.
- `requesting-code-review` before a merge that matters.
- The official `skill-creator` to refine this skill with an eval loop later.
