# AGENTS.md fragment, standing rules

Copy the sections below into the repository's `AGENTS.md`. They are standing instructions: they
fire on every task, not only the ones where the conductor was loaded. Delete any bullet that does
not apply. Do not add bullets for things that have not yet gone wrong here.

This fragment is the portable half of [jules-prompts](https://github.com/melbinjp/jules-prompts).
The other half is the conductor, an Agent Skill in `conductor/` that you install as a whole
folder, and the fixtures in `fixtures/` that show it catching planted failures. The same block,
kept in step with the conductor's guidance, is in `conductor/guidance/autonomy.md`.

---

## Start from the conductor

- For any project, or any piece of work in one, load `conductor/SKILL.md` and follow it. It
  classifies the project, runs the control loop and says which guidance to load.
- If it is installed (`.agents/skills/conductor/` or `.claude/skills/conductor/`), use that copy,
  whole. If it is not, fetch https://jules-prompts.wecanuseai.com/llms.txt: it links the archive of
  the whole folder and every file in it. `SKILL.md` alone is incomplete.
- On a small context window, load one guidance file at a time, and only the sections the work needs.

## Reporting

Every item ends as one of these, and guessing in either direction is a lie.

- **verified**: you ran it or inspected it, and the evidence agrees
- **failed**: you ran it, and the project contradicts it
- **not verified**: you could not check it reliably, and you said why
- **not applicable**: with the recorded decision that says so
- **exception**: with who authorised it, its scope and when it expires

The last two are never counted as passes. A report that says "clean" without saying what it read
cannot be told apart from one that read nothing. End every report with what you judged and what
you did not: `14 verified, 2 failed, 3 not verified, 2 not applicable of 21 items.`

## Prove it can fail

- A test nobody has seen fail is a claim, not a check. Break the behaviour it names, watch it go
  red, restore.
- A CI job nobody has seen fail is the same claim. Introduce the defect it exists to catch,
  confirm the job goes red, revert.
- Do not swallow exit codes (`|| true`, `continue-on-error`, a pipe that reports `tee`). Absence
  looks exactly like success.
- Do not skip a test to make the suite green. Delete it or fix it.

## Do not guess

- An unreproduced bug is unreproduced. Do not fix it.
- A path, flag, or command in the docs is a claim. Run it, or mark it not verified.
- If the original issue is vague, scope it before writing code. The wrong fix is more expensive
  than a reproduction.
- Prefer the lockfile, the CI workflow, and what actually runs over folder names and comments.

## What not to do

- Do not add a test that asserts `toBeDefined`, `is not None`, or that no exception was raised,
  unless a value assertion sits next to it.
- Do not mock the unit under test.
- Do not capture expected values by running the code under test.
- Do not remove a failing check to make a build go green.
- Do not start a long-running process in a setup script. Install, verify, exit.
- Do not add machinery (a framework, a container, a service, a runbook) because production
  projects have one. Add it when you can name what breaks without it.

## Every change has a reason

- Every change traces to the objective, a requirement or an accepted decision. A change that
  serves none of them is a question for the owner, not work.
- Every change links to its work item in the project's own tool and names how it was verified
  (the test seen to fail without it, the measurement before and after).
- Decisions are recorded as ADRs (`conductor/templates/adr.md`): options, evidence, a way out and
  the condition that reopens them. Contradicting an accepted decision takes a superseding record
  before the code changes.
- Translate a vague request ("faster", "scalable", "modern", "add AI") into a measure, and measure
  before changing anything. If the measure already meets its target, the answer is no, with the
  number.
- A change is done when it is carried through every layer it touches and what it replaced is gone:
  no module nothing calls, no setting nothing reads, no dependency nothing imports.
- Nothing the owner asks for is dismissed, and no route is declared impossible. A blocked route gets
  another route, costed honestly.
- Every stage of the work is a procedure another person or agent can repeat. Nothing lives only in
  an agent's memory or tools.

**A project that already keeps the older ledger** (`PROJECT.md`, `decisions/`, and `Serves:` and
`Verified:` lines in every commit) can keep it, and keep running `harness/check_trace.py` in its CI:
that check is unchanged. A new project does not adopt the ledger. It uses the conductor's records
instead, in the tools it already has.

## Confidential projects

For a project whose code, data or plans must stay private (`conductor/guidance/confidentiality.md`).
The rules on where each class may go live in the project's confidentiality record.

- Send nothing beyond those rules: no code, names, customers or data into a search box, a forum, a
  remote model or a hosted tool the rules do not name.
- A remote agent or model gets only the classes released to it, and the smallest excerpt that does
  the job, never the whole repository.
- Everything the project needs to build, test and run with the network off is in the repository or a
  local mirror, with its hash. Offline is proved by running it offline.
- When the internet must be used, fetch broadly and search locally, through the gate the rules name,
  and log what left.

## Working on your own for long stretches

For a build that runs with nobody watching (`conductor/guidance/autonomy.md`).

- The records are your memory. Rebuild what you know from the state note, the records and the files
  every step; never rely on an earlier step you can no longer see. Rewrite the state note whenever
  what you know changes.
- Look up; do not remember. Before using a function, a path, a flag or a result, check that it
  exists, in a file you read or a command you ran.
- Never wait on what can be looked up or reversibly chosen. Where the briefing is silent, test it,
  choose the most reversible option, record it for the owner, and carry on. Apply the owner's
  overrides as soon as they appear.
- Nothing is done until its gates pass: its tests, seen to fail without it; its measure; a review
  by someone other than its author, in a fresh context. A failed gate means another attempt or
  another route, never a lower gate.

## Acting on the world

For anything a command can move, heat, dispense, spend or send: hardware, devices, machines, and
services that ship, pay or message a person (`conductor/guidance/physical.md`).

- An acknowledgement is not an outcome. Confirm the result through something that measures the
  world, after the action, within a deadline.
- The default target is the simulator or a dry run. Real hardware or a live service is an explicit
  choice, and the output says which one is in use.
- Every failure path goes to a safe state that was decided in advance. When in doubt, do less: stop
  moving, stop heating, stop dispensing.
- Do not retry an action that may already have happened. Use absolute targets, or observe that the
  first attempt did not happen.
- Nothing that cannot be undone happens without a person's yes to the exact action and its
  parameters.

## Which guidance to load

Load the guidance the work needs, after `conductor/SKILL.md` has classified the project.

- a choice that matters: a vendor, platform, part, provider or approach: `guidance/decisions.md`
- what people or agents see, do or hear: a flow, a screen, a command line, an API, a device's
  controls, or "make it prettier": `guidance/design.md`
- the bar a result must meet, or reviewing work: `guidance/quality.md`
- any software: tests, CI, setup, bugs, reviews, migrations, dependencies, docs: `guidance/software.md`
- a release to people, or a product that works and nobody uses: `guidance/product.md`
- a live product failing people now, or keeping one healthy: `guidance/operations.md`
- a private or offline project, or anything leaving the machine: `guidance/confidentiality.md`
- any command to hardware, a device or a real-world service: `guidance/physical.md`
- an event, a film, a document, training or another delivered service: `guidance/service.md`
- one model and one person, an unattended build, or several agents: `guidance/autonomy.md`
- dates, dependencies, resources, risks or changes to scope: `guidance/planning.md`
- docs that might be stale: `guidance/software.md`, and [docproof](https://github.com/melbinjp/docproof)
  if the claim is mechanical
