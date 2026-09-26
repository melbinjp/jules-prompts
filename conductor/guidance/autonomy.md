# Autonomy: agents, harnesses and unattended work

Load when the work is done by an agent that does not yet have a working harness, when it will run
unattended or for long stretches, when several agents share the work, or when choosing which agent
does which work. A model on its own is not an agent: it answers one message and forgets it. The
work needs something that acts for days, reads and writes files, runs commands, keeps decisions,
and does not invent what it cannot see.

## Choosing the agent and harness

- **Take stock by trying:** can the model read a file, write one, run a command, reach a network,
  reach the person? What can it not do, and what would close each gap?
- **Use an existing harness when one meets §What a harness must do.** Harnesses differ in command
  access, reachable hosts, a browser, secrets, hardware access, long-running processes, approval
  pauses, parallel agents, context size and cost; choose on the project's requirements
  (`decisions.md`). Build one only when no existing harness can meet them (for example, a strictly
  offline project whose local model no available harness supports), and then prove it against the
  requirements; jules-prompts' `harness/conformance.py` is one such test.
- **Make the way of working a setting, not a design.** The model endpoint, the package source and
  every outside service have a local and a remote form, chosen by configuration, so the same project
  runs fully offline, fully online or mixed without code changes; prove each mode the
  confidentiality rules allow (`confidentiality.md §Working offline`). The same loop runs unattended,
  supervised (each action shown for a yes) or by hand (a person following the state note), and any
  procedure can move between a model and a person, because every procedure and every decision is in
  the records. A change of circumstance changes a setting, not the build.

## What a harness must do

Whether stock or built, check that it:

- **loops** (look, decide, act, check, record) until the model says done, a step limit is reached,
  or the person stops it; and exits cleanly at each;
- **rebuilds a fresh, bounded context every step** from files, never a growing conversation: the
  rules and the action format; the task; the guidance for the current work (only the sections needed
  when it would take more than half the window); the state note; the person's overrides; the last few
  actions and results, oldest dropped first, each cut to fit; every prompt inside the window with
  room for the reply, including a small window;
- **takes actions as one structured reply** (read a range of a file, write a file, run a command in
  the project, record a choice, replace the state note, done), shows what was read or run in the next
  step, and answers an unreadable reply with the format rather than crashing;
- **keeps boundaries that do not depend on the model behaving:** files inside the project only; the
  person's override lines and the harness's own log written by the person and the harness, never by
  the model;
- **checkpoints after every step that changed the project** (a version-control commit), so any step
  can be undone and an earlier version recovered;
- **logs every step:** what was sent, what was done, what it cost;
- **starts a new run from the state note and the records,** not from memory;
- **honours a stop the person can trigger without the agent** (a stop file or equivalent), checked
  before acting;
- **treats the model endpoint as configuration:** a local or a hosted runtime; an endpoint off the
  local network refused unless explicitly allowed; remote traffic through the project's egress proxy
  when one is set (`confidentiality.md §Agents and models`).

## Building a missing tool

- **Discover what exists first:** the tools on the machine, the libraries in the mirror, the
  documentation downloaded, established open-source tools.
- **Whatever is missing** (a browser, hardware access, a simulator, a test jig, a search index over
  downloaded documentation, a way to notify the person) **is built into the repository with its own
  test,** so it outlives the agent and the harness that built it.
- **A step done three times, or one whose mistakes are costly, becomes a tool.**
- No harness, tool or simulator is a reason to stop; each is a thing to find, or build and prove.

## Briefing: ask once

The build may run for days, and after the briefing it does not wait. Ask the person everything only
they can answer, at the start, in one sitting, and record the briefing in the project's records:

- the objective, what success looks like, and why they are doing it (`product.md §Intake: what only
  the owner knows`);
- the decisions of taste, money, law and risk that only they can make, and the ones they delegate,
  with the limits of that delegation;
- the accounts, keys, hardware and access the work will need, set up now;
- **standing limits for anything that leaves the working environment:** money it may spend and on
  what; what it may publish or send and where; what physical actions it may take and within which
  bounds (`physical.md`); and, once live, which restoring actions it may take on its own in an
  incident, and which it may never take (silencing alerts, disabling checks, deleting data)
  (`operations.md §Incidents: restore first`). Inside the limits it acts without asking; outside them
  it takes another route;
- the budget: time, money and model use, and what happens as it runs low;
- the confidentiality classes, and whether the model may be remote (`confidentiality.md`);
- how and how often they want to hear about progress;
- for each open question you can foresee, their answer, or the default they accept.

An hour with the person at the start buys days of work without them.

## Choices on the owner's behalf

When the briefing is silent, decide, in this order:

1. look in the repository and the records;
2. look in the documentation and sources available (downloaded, or through the project's internet
   gate);
3. run an experiment, a calculation or a prototype that decides it;
4. choose, by `decisions.md` sized to the stakes, preferring the choice that is easiest to reverse.

Record each choice with its reason, how to undo it, and a line where the owner can override it. Never
wait on the person for what can be looked up (which test runner, where the tests are) or reversibly
chosen: a question at eleven at night that stops everything until morning is the failure. Read the
overrides before every step and apply each at once, undoing what depended on the old choice. A major
update or decision that cannot be taken yet is recorded with its blocker and route, and the rest
continues. At each review, show the owner the choices made since the last one.

## Sandbox, checkpoints and stop

- **A sandbox:** the agent runs in an environment of its own (a container, a virtual machine, a
  dedicated user account) holding the project and its tools, and none of the person's other files or
  credentials. Inside it, any command is safe to run, so it never has to ask.
- **Checkpoints:** every step is committed; a step that breaks the build is reverted, not repaired in
  place on top of a mess.
- **Standing limits enforced where the action happens,** not by the agent's good behaviour: a spending
  cap on the payment account, a publishing target that is a test channel until a milestone says
  otherwise, device limits in firmware.
- **A stop the person can trigger without the agent,** and a clean state whenever it stops.

## Budget

- **Counted in the log as it is spent,** in money, time and model use.
- **At 80%, slow the pace and tell the person.**
- **When it runs out, the run pauses and the project does not:** the state note holds where the work
  is and the next step, and the report names the routes to continue (a cheaper or local model, fewer
  agents at once, a funding route), so the work resumes the moment budget does.

## Context and state

Most invented code in long runs is a context problem: the less of the truth is in front of the model
and the more noise is, the more it fills gaps with what is plausible (a function that should exist, a
flag that sounds right, a test it believes passed).

- **The records are the memory; the context is a view of them.** Rebuild what you know every step
  from the state note, the records and the files; never rely on an earlier step you can no longer see.
- **Rewrite the state note** after every step that changes what is known: where the work is, what was
  decided and why, what is waiting, what is next. Keep it under a page.
- **Stay under half the window.** The model reasons worse as it fills.
- **One guidance file at a time,** and only the sections the current work needs.
- **Read by range, not whole:** search first, then read the lines that matter; keep long outputs in
  files and read back what is needed.
- **Look up; do not remember.** Every fact acted on comes from a file read this step, a command run
  this step, or a recorded answer or source. Before using a function, a flag, a path or a result,
  check that it exists.

## Routing work to agents

- **By what each agent may see, first:** where it runs (this machine, the owner's network, a named
  provider) and which of the project's confidentiality classes it may receive. No agent receives a
  class the rules have not released to it, however capable it is (`confidentiality.md §Agents and
  models`).
- **Then by measured ability, not reputation:** qualify each agent for each kind of work on a small
  task held back from this project and of the same kind, scored against its acceptance criteria;
  record the scores. A model's reputation, size or benchmark is a claim. Re-qualify when a model, its
  settings or the harness changes, and move the work to its fallback if the score fell.
- **Fit the work to the agent:** a small local model with a short context gets smaller, tightly scoped
  work packages and one guidance section at a time; a stronger one gets more.
- **No procedure rests on one agent:** record, for each, the agent, where it runs, the classes it may
  see, its score, and its fallback (another agent or a person). A provider's outage, price change or
  policy change then moves the work to its fallback instead of stopping the project.

## Several agents

- **Split into several roles only where it pays:** builder, reviewer, researcher, tester, each with a
  fresh context and only the guidance it needs. One model can play several roles in turn.
- **They coordinate through the records and the repository,** and share nothing else: work items are
  claimed in the work records before work starts, one branch or workspace each.
- **The reviewer is never the author** of what it reviews.

## Standing rules for the project

A short block for the project's agent instructions (its `AGENTS.md` or equivalent), so the rules
apply even when nobody loads this guidance. Adapt it; delete lines that do not apply.

```markdown
## How work is done here

- Start from the conductor: classify, then take the next ready work package from the work records
  (in <the project's tool>). Record every change with a link to its work item and its evidence.
- Every result is verified, failed or not verified (with the reason). "Not applicable" and
  authorised exceptions are recorded as such and never reported as passes. End each report with
  what was checked and what was not.
- A test, check or inspection nobody has seen fail is a claim: show it detects the defect it is for.
  Never swallow exit codes, skip a test, or remove a failing check to go green.
- Do not guess: reproduce before fixing; a documented path or flag is a claim until run; prefer the
  lockfile, CI and what actually runs over names and comments.
- No test that asserts only shape, mocks the unit under test, or captures expected values from the
  code under test. Setup installs, verifies and exits.
- Every change traces to the objective, a requirement or an accepted decision (ADRs in <place>), is
  measured before and after, is carried through everything it touches, and removes what it replaces.
  Contradicting an accepted decision takes a superseding ADR first.
- Add machinery only when you can name what breaks without it.
- The records are the memory: rebuild from them each session; look up, do not remember; never wait
  on what can be looked up or reversibly chosen, and record each such choice for the owner.
- Nothing is done until its gates pass, checked after the last change, and reviewed by someone
  other than its author.
- Acting on the world: an acknowledgement is not an outcome; the default target is the simulator;
  every failure goes to a decided safe state; never retry what may already have happened; nothing
  irreversible without a person's yes to the exact action.
- Confidential work: send nothing beyond <the confidentiality record>; remote models get only the
  released classes and the smallest excerpt; offline is proved by running offline.
- Commands: install `<command>`, test `<command>`, required environment `<variables>`.
```
