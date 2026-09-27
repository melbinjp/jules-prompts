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
