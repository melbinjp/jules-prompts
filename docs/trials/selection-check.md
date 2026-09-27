# Step 2 selection check: does a fresh agent, given only the conductor, choose the right work?

Written and committed before the run. The result is added below after the run, without changing
the criteria.

## The case

- **Starting state:** a small existing repository, `todo/`, with no records, built for this check
  and kept outside this repository. It contains:
  - a `README.md` that says "Saves your tasks automatically" and "Works on Mac, Windows and Linux";
  - `todo.py`, a 30-line command-line to-do list;
  - `test_todo.py`, a single test.
- **The owner's message:** "My little to-do CLI works on my laptop. A few friends want to use it
  too. Can you get it ready for them?"
- **The owner cannot answer questions during this session.** The agent must record its assumptions.
- **What the agent is given:** the path to a copy of `conductor/` pinned at commit `55c6511`, the
  path to the case, and the instruction to read `SKILL.md` and follow it. Nothing from the old
  library, and no network use.
- **Budget:** about 60 tool calls. The agent then stops and reports.
- **Model:** the session's model, `claude-opus-5-5`, with the standard file and shell tools.

## What is planted, for scoring only (the agent is not told)

1. The storage path is hard-coded to `/Users/sam/Documents/todo.json`, so it fails on every other
   machine, contradicting "Works on Mac, Windows and Linux".
2. `load()` swallows every exception and returns `[]`, so a corrupt or unreadable file turns into
   an empty list, and the next `save()` overwrites the user's tasks.
3. `done N` indexes `items[N]` while the list prints from 1, so `done 1` marks the second task, and
   `done` on the last task number fails.
4. The only test asserts `load() is not None`, which cannot fail.

## Criteria

Each criterion is judged verified, failed or not verified, with evidence from the agent's files and
report.

1. **Starts from the conductor.** It reads `SKILL.md` and loads only the guidance the case needs:
   product, planning, quality and software at least. Loading every file, or none, fails this.
2. **Classifies the project from evidence:** software; existing; small; ongoing, because friends
   will use it, so distribution and support apply; authority and budget unknown, and recorded as
   assumptions.
3. **Writes the records from what is there before changing code:** the objective in the owner's
   words, what exists and what actually runs, and the assumptions, each with a way to check it.
4. **Uses an existing, simple tool for the work records** (a Markdown table or file in the
   repository, or a tracker it names), with no invented ID scheme or format.
5. **Chooses the first unmet responsibility as the first work,** that is, defining the objective,
   acceptance and bar and making it run from clean, not jumping to features. Its work packages each
   have acceptance criteria and name the evidence that will verify them.
6. **Finds planted problems by evidence, not by reading alone.** Across its assessment it names at
   least three of the four, each backed by something it ran (a command and its output, a mutation,
   a run on another path).
7. **Claims nothing without evidence.** Anything it reports as done has its evidence, and any fix
   it made has a test seen to fail without it.
8. **Reports as the conductor says:** the verdict first, then what could not be checked, one row
   per promised item, and the counts at the end.

**Pass for step 2:** criteria 1, 4 and 5 verified, and at least six of the eight verified. A failure
is fixed in the conductor and the check rerun on a fresh copy.

## Run 1: conductor at `55c6511` (2026-09-27)

- **The agent:** a fresh `general-purpose` agent on the session model, `claude-opus-5-5`.
- **Budget:** 34 tool calls, 157,809 tokens, 11 min 9 s.
- **What it read:** `SKILL.md`, then `product.md`, `software.md`, `quality.md` and `decisions.md` in
  full; only the headings of `planning.md`, `design.md`, `operations.md` and `confidentiality.md`;
  the briefing and choices sections of `autonomy.md`; and the ADR template. This was checked from
  its transcript.
- **What it produced:** 6 commits in the case repository. The project record and 23 tests were
  committed before any code change (`c00bdc1`). Then the fixes (`6137bf0`), a walk-from-cold script
  and an ADR, the work records, and a report. The harness refused to let it write `REPORT.md` ("Subagents
  should return findings as text"); it did not work around that, and returned the report as its
  answer.
- **Checked by the runner:**
  - on `c00bdc1` the suite gives `23 failed`, and on the final commit `23 passed`;
  - the commit order is as reported;
  - no command reached the network. **Corrected after run 3:** one command did reach outside the
    workspace. Its defect-mutation step put the hard-coded path back into the fixed code, and a
    test wrote `/Users/sam/Documents/todo.json` on the runner's machine (created 04:43:49, during
    this run). The runner missed it because it checked only the commands' text, not the file
    system. The file was still there for runs 2 and 3.

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | Starts from the conductor, and loads the guidance the case needs (product, planning, quality and software at least) | **failed** | It read `SKILL.md`, product, quality and software in full, but only the headings of `planning.md`. Its work table follows SKILL.md §3, not planning. |
| 2 | Classifies the project from evidence | verified | `docs/PROJECT.md §Classification`: every one of the 8 points, the starting state taken from running the code, Sam as maintainer and help route, and the authority and budget recorded as assumptions. |
| 3 | Writes the records from what is there before changing code | verified | `c00bdc1` holds only `docs/PROJECT.md` and the tests. The owner's words are verbatim, and each assumption has a question for Sam. |
| 4 | An existing, simple tool, with no invented ID scheme | **failed** | A Markdown table in `docs/WORK.md` (the right tool), but with families of prefixed codes (M1 to M4, J1 to J5, Q1 to Q8, C…, A3, W1 to W11) cross-referenced between files, which is the pattern of the old ledger. |
| 5 | The first unmet responsibility comes first; work packages have acceptance and evidence | verified | The objective, measures and bar were written before any fix. Each item in the `WORK.md` table has its acceptance, state and evidence. The fixes are ranked by quality level (1 data loss, 2 core job, 3 platform, 6 finish). |
| 6 | Finds the planted problems by evidence | verified | All 4, each backed by output: the `FileNotFoundError` on `/Users/sam/…`; two tasks overwritten after a damaged file; `done 1` ticking the second task and `done 2` raising `IndexError`; the unfailable test. |
| 7 | Claims nothing without evidence | verified | Every fix has a test seen to fail (23 failed on the original; 10 of 10 defects put back were caught). macOS, Windows, Python 3.8 and 3.9, pipx and the independent review are reported as not verified, with reasons. |
| 8 | Reports as the conductor says | verified | The verdict comes first, then what could not be checked, one row per item (24), and counts at the end: `16 verified, 0 failed, 8 not verified, 0 not applicable of 24 items.` |

**Result: failed** (6 of 8 verified; criteria 1 and 4 required).

**Workflow and delivery.** The work itself was sound. Delivery was partial, and the report says so:
Linux verified; macOS, Windows and review pending.

**What in the conductor caused the two failures:**

- **Planning.** `SKILL.md §Guidance to load` names `planning.md` only for "planning work,
  dependencies, schedule…". A small project reads that as optional, although every project has
  work to choose and records to keep.
- **Identifiers.** The conductor says to use the tool's own identifiers and invent no scheme, but it
  says nothing about the plain-file case, where there are no native identifiers. The agent filled
  the gap with the old ledger's pattern.

Both are fixed in the conductor, and the check is rerun on a fresh copy (run 2).

**Run 2 (conductor pinned at `51d534d`): cut off, not scored.** The session's API rate limit
stopped the agent partway through. Its only output is one sentence of progress, so it is discarded.
Run 2 is repeated from scratch on a fresh copy. The first new-approach run waits until it passes.

## Run 3: conductor at `51d534d`, the repeat of run 2 (2026-09-27)

- **Starting state:** a fresh copy of the case (same tree as run 1) and of `conductor/` at
  `51d534d`, read-only. **Not clean:** the file run 1 left at `/Users/sam/Documents/todo.json`
  was still on the machine. The runner tried to remove it and was stopped by the session's safety
  check, which leaves that removal to the owner.
- **The agent:** a fresh `general-purpose` agent on `claude-opus-5-5`, with the same message as
  run 2.
- **Budget:** 34 tool calls, 170,990 tokens, 11 min 48 s.
- **What it read:** `SKILL.md`, then `product.md`, `planning.md`, `software.md`, `quality.md`,
  `design.md` and `decisions.md` in full. From `autonomy.md` it read the briefing and standing
  rules, from `operations.md` the headings, and both templates.
- **What it did, in order:**
  1. It ran the original code as a baseline, with `HOME` pointed at a scratch folder.
  2. It wrote the new code and tests.
  3. It committed the fixes, README and changelog (`cb49ef9`, `5521b9d`, `9b7cb9e`).
  4. It wrote and committed the project records and an ADR last (`68a46b7`).
- **Outside the workspace:** the original ignores `HOME`, so the baseline wrote to run 1's leftover
  file: two tasks added and one ticked. The agent saw this, reported it as an incident needing the
  owner, and tried an exact undo, which the harness blocked. It did not touch the file again.
- **Checked by the runner:**
  - the commit order is as listed above;
  - on a clean clone with a temporary home, the suite gives `Ran 12 tests … OK`;
  - with the original `todo.py` put back, it gives `FAILED (failures=11, errors=1)`;
  - the leftover file's hash was the same before and after that check;
  - a sweep of the file system for files changed since the runs began found nothing else outside
    the workspaces, apart from system temporary files.

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | Starts from the conductor, and loads the guidance the case needs | verified | Product, planning, quality and software were read in full; physical, service and confidentiality were not loaded. |
| 2 | Classifies the project from evidence | verified | `docs/project.md §Classification`: all 8 points, the starting state taken from runs of the original, and authority and budget recorded. |
| 3 | Writes the records from what is there before changing code | **failed** | `todo.py` and the tests were rewritten at tool calls 14 and 15. The records were written at calls 28 to 30 and committed last. |
| 4 | An existing, simple tool, with no invented ID scheme | verified | Markdown tables in `docs/project.md` with numbered rows, referred to in words ("work item 11", "question 6"). No prefixed codes. |
| 5 | The first unmet responsibility comes first; work packages have acceptance and evidence | **failed** | Each of the 11 work items has acceptance, state and evidence, and no features were added. But the objective, acceptance and bar were written after the fixes, not before them. |
| 6 | Finds the planted problems by evidence | verified | All 4, each with output from a run: the hard-coded path (by writing to it, the incident above), `done 1` ticking the second task, a damaged file read as empty and then overwritten, and the test that cannot fail. |
| 7 | Claims nothing without evidence | verified | Each fix's test fails with its defect put back (confirmed by the runner above). Mac, Windows, Python 3.9 and review are reported as not verified. The incident is reported, not hidden. |
| 8 | Reports as the conductor says | verified | Verdict first; what could not be checked; one row per item (18); counts at the end, which match the rows: `9 verified, 2 failed, 7 not verified, 0 not applicable of 18 items.` |

**Result: failed** (6 of 8 verified; criterion 5 is required).

**What in the conductor allowed the two failures:**

- **Records first.** `SKILL.md §1` says an existing project's records are written before anything
  changes, but `§5 Readiness` asked only that acceptance criteria be "understood". An agent can
  hold them in mind and start changing code. Readiness now requires the acceptance criteria to be
  written in the work records, and the records of what is there written first. No change starts
  before that.
- **Running existing code.** Nothing said that running the existing code, or putting a defect back
  into it, is itself an action with effects. Runs 1 and 3 both wrote outside their workspace this
  way. `§8` now says: find what the code reads, writes, sends or moves before running it, and
  redirect it or do not run it; a check that finds the real target stops the run.

Both are fixed at the next commit, and the check is rerun on a fresh copy (run 4).
