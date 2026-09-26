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

## Every change has a reason

For a project that keeps a ledger: `PROJECT.md` (goal, measures, journeys,
resources, course changes, milestones) and `decisions/` (one file per decision).

- Every commit names what it serves and how it was verified, in two trailer
  lines: `Serves: M2` and `Verified: tests/test_race.py`. A change that serves
  nothing is a question for the owner, not work.
- Nothing the owner asks for is dismissed, and no idea is declared impossible.
  A blocked route gets another route, costed honestly.
- Translate a vague request ("faster", "scalable", "modern", "add AI") into a
  measure, and measure before changing anything. If the measure already meets
  its target, the answer is no, with the number.
- Read the accepted decisions a change touches. Contradicting one takes new
  evidence and a record that supersedes it, before the code changes.
- A change is done when it is wired through every layer it touches and what it
  replaced is gone: no module nothing calls, no setting nothing reads, no
  dependency nothing imports, no two paths computing the same fact.
- Every recorded decision has at least two backings, each labelled by its kind
  (Measured, Calculation, Simulation, Proof, Prototype, Test, Source), and at
  least one was run, worked out or built rather than read. A decision that is
  costly to reverse also needs three options, two different kinds of evidence,
  a way out and a person's name.
- Every pipeline stage is a command in this repository that a person, an agent
  or CI can run. Nothing lives only in an agent's memory or tools.

## Confidential projects

For a project whose code, data or plans must stay private. The rules on where
each class may go live in `CONFIDENTIALITY.md`.

- Send nothing beyond those rules: no code, names, customers or data into a
  search box, a forum, a remote model or a hosted tool the rules do not name.
- A remote agent or model gets only the classes released to it, and the
  smallest excerpt that does the job, never the whole repository.
- Everything the project needs to build, test and run with the network off is
  in the repository or a local mirror, with its hash. Offline is proved by
  running it offline.
- When the internet must be used, fetch broadly and search locally, through
  the gate the rules name, and log what left.

## Working on your own for long stretches

For a build that runs with nobody watching (`run-autonomously`).

- The repository is your memory. Rebuild what you know from `STATE.md`, the
  ledger and the files every step; never rely on an earlier step you can no
  longer see. Rewrite `STATE.md` whenever what you know changes.
- Look up; do not remember. Before using a function, a path, a flag or a
  result, check that it exists, in a file you read or a command you ran.
- Never wait. Where the briefing is silent, look it up, test it, choose the
  most reversible option, record it in `CHOICES.md`, and carry on. Apply the
  owner's overrides as soon as they appear.
- Nothing is done until its gates pass: its tests, seen to fail without it;
  its measure; the trace check. A failed gate means another attempt or
  another route, never a lower gate.
- Your own work is reviewed by a fresh context, never the one that wrote it.

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

- one model and one person, or a build that must run on its own → `run-autonomously`
- an idea, or a project with no written reason for what it is → `start-from-an-idea`
- a vendor, platform, part, provider or approach to choose → `choose-with-evidence`
- any requested change, especially a vague one → `change-with-a-reason`
- what people or agents see, do or hear: a flow, a screen, a command line, an API, a device's controls, or "make it prettier" → `design-the-experience`
- a milestone reached, or the next round of improvement after launch → `keep-it-on-course`
- a private or offline project, or anything leaving the machine → `keep-it-confidential`
- making a project dependable, finished and production-ready → `take-to-production`
- any command to hardware, a device or a real-world service → `act-on-the-physical-world`
- agent-authored tests → `qa-an-agents-tests`
- agent-authored pull request → `review-an-agent-pr`
- CI that has been green for a long time → `repair-a-green-pipeline`
- setup that fails before work starts → `repair-setup-script`
- docs that might be stale → `prove-the-docs` (and [docproof](https://github.com/melbinjp/docproof) if the claim is mechanical)
- a thin bug report → `scope-a-vague-issue` first, then `fix-a-bug-test-first`
