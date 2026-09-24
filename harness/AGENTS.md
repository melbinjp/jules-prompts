# AGENTS.md fragment, verification doctrine

Copy the sections below into the repository's `AGENTS.md`. They are standing
instructions: they fire on every task, not only the ones where someone pasted a
prompt. Delete any bullet that does not apply. Do not add bullets for things
that have not yet gone wrong here.

This fragment is the portable half of [jules-prompts](https://github.com/melbinjp/jules-prompts).
The other half is the skills in `skills/` (load one when the task matches) and
the fixtures in `fixtures/` (the only way to see a skill go red).

---

## Verdicts

Every claim is one of three things. Guessing in either direction is a lie.

- **holds**: you ran it, and the project agrees
- **broken**: you ran it, and the project contradicts it
- **skipped**: you could not check it reliably, and you said so with a reason

A report that says "clean" without saying what it read cannot be told apart from
one that read nothing. End every report with what you judged and what you did
not: `3 broken, 11 checked, 4 not judged.`

## Prove it can fail

- A test nobody has seen fail is a claim, not a check. Break the behaviour it
  names, watch it go red, restore.
- A CI job nobody has seen fail is the same claim. Introduce the defect it
  exists to catch, confirm the job goes red, revert.
- Do not swallow exit codes (`|| true`, `continue-on-error`, a pipe that reports
  `tee`). Absence looks exactly like success.
- Do not skip a test to make the suite green. Delete it or fix it.

## Do not guess

- An unreproduced bug is unreproduced. Do not fix it.
- A path, flag, or command in the docs is a claim. Run it, or mark it skipped.
- If the original issue is vague, scope it before writing code. The wrong fix
  is more expensive than a reproduction.
- Prefer the lockfile, the CI workflow, and what actually runs over folder names
  and comments.

## What not to do

- Do not add a test that asserts `toBeDefined`, `is not None`, or that no
  exception was raised, unless a value assertion sits next to it.
- Do not mock the unit under test.
- Do not capture expected values by running the code under test.
- Do not remove a failing check to make a build go green.
- Do not start a long-running process in a setup script. Install, verify, exit.
- Do not add machinery (a framework, a container, a service, a runbook) because
  production projects have one. Add it when you can name what breaks without it.

## Acting on the world

For anything a command can move, heat, dispense, spend or send: hardware,
devices, machines, and services that ship, pay or message a person.

- An acknowledgement is not an outcome. Confirm the result through something
  that measures the world, after the action, within a deadline.
- The default target is the simulator or a dry run. Real hardware or a live
  service is an explicit choice, and the output says which one is in use.
- Every failure path goes to a safe state that was decided in advance. When in
  doubt, do less: stop moving, stop heating, stop dispensing.
- Do not retry an action that may already have happened. Use absolute targets,
  or observe that the first attempt did not happen.
- Nothing that cannot be undone happens without a person's yes to the exact
  action and its parameters.

## When to load a skill

If this repository has the jules-prompts skills installed, load the matching
one rather than improvising. If it does not, each one is a single file listed at
https://jules-prompts.wecanuseai.com/llms.txt.

- making a project dependable, finished and production-ready → `take-to-production`
- any command to hardware, a device or a real-world service → `act-on-the-physical-world`
- agent-authored tests → `qa-an-agents-tests`
- agent-authored pull request → `review-an-agent-pr`
- CI that has been green for a long time → `repair-a-green-pipeline`
- setup that fails before work starts → `repair-setup-script`
- docs that might be stale → `prove-the-docs` (and [docproof](https://github.com/melbinjp/docproof) if the claim is mechanical)
- a thin bug report → `scope-a-vague-issue` first, then `fix-a-bug-test-first`
