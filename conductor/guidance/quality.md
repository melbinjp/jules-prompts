# Quality: the bar a result must meet, and how it is checked

Load when setting or checking what "good enough to hand over" means, for any kind of output:
software, a physical product or installation, a service, an event, a document. It also holds the
rules for reviewing any work, including your own.

Asked to make something "production-grade", an agent reaches for the visible signs: a CI file, a
container, a coverage badge, docstrings, a runbook. They are cheap to add and none of them is the
thing. A project can have all of them and still lose a person's work when the tab closes, fail on
the phone half its users carry, and greet a mistake with "Something went wrong."

## Write the bar first

Production quality is a property of what a person experiences on their worst day, on a real device
or site, not of the repository's furniture. It means four things, each checked rather than claimed:

1. it does the one job it exists for, on every platform or in every environment its people use;
2. it never loses, corrupts or exposes what people trusted it with, whatever the environment or an
   attacker does;
3. it feels finished to use: nothing rough, unexplained or unreachable;
4. it carries nothing it does not need.

Before changing anything, write the bar in the project's records, short:

- **the one job,** in a sentence the person using it would say (from the owner; if absent, derived
  from the project, saying how);
- **who does it, and on what:** the people and, where they operate it, the agents and automation;
  the actual devices, operating systems, browsers, networks, venues, or hardware and conditions;
- **the three to five journeys that must never fail;**
- **what must never be lost or corrupted;**
- **the budgets** that decide "fast enough" and "small enough": load time, size, frame rate,
  memory, battery, latency, cost per use, time on site;
- **the assumptions** made where the project gave no evidence, and why.

Read the evidence: the promises the README, listing, brochure or contract already makes (the bar
the project has set itself); what actually runs and what is actually checked; everything that
stores, sends or moves what people care about; the dependency or parts list, read as a list of
costs; and the bad days already reported (issues, crash reports, complaints, returns).

## Walk every area

For every area below, add rows to the bar, or write one line on why it does not apply, so a
reader can tell a considered omission from a forgotten one. The method everywhere: make the
failure or the attack happen, then look.

- **Security:** `software.md §Standards to apply` (and physical access, `physical.md §Access to
  devices`).
- **Privacy:** what personal data is collected, where it goes, who else receives it (analytics,
  error trackers, third-party scripts, model providers, suppliers), how long it is kept, and how a
  person deletes it.
- **Data:** where every piece of state lives, what writes it, what happens when two writers meet;
  backups restored at least once; migrations on real-shaped copies (`operations.md §Backups and
  restore`, `software.md §Data migrations`).
- **Reliability:** every external dependency made to fail and to go slow (`software.md §Error
  paths`).
- **Performance and capacity:** the budgets; for anything serving more than one person, the
  expected peak with a margin, measured; memory and handles steady over a long run; the cost of
  one use known.
- **Compatibility:** §Every platform and environment, for real.
- **Accessibility and craft:** §Craft standard and `design.md`.
- **Operators:** each journey done end to end by each operator the bar names (a person, an agent
  through the machine interface, automation), under the same limits (`design.md §Every operator`).
- **Operations:** §Operable, and `operations.md`.
- **Delivery:** `software.md §Delivery: review, CI, deploy, rollback`, or the physical and service
  equivalents.
- **Maintainability:** set up from clean, documentation whose instructions work, dependencies
  current, the complexity budget.
- **Legal:** licences of dependencies, fonts, images, music, footage and data compatible with how
  the result is distributed, with the notices they require; terms, a privacy notice, contracts and
  certifications the result needs.
- **Physical safety,** whenever it moves, heats, dispenses, spends or sends
  (`physical.md §Safety states and irreversible actions`).

## Fix in order of cost to the person

Rank every finding and work from the top; do not polish a level 6 while a level 1 is open:

1. loses, corrupts or exposes what they trusted it with;
2. cannot do the core job;
3. broken on a platform or in an environment they use;
4. unsafe, insecure or inaccessible;
5. slower or heavier than the budget;
6. unfinished to use;
7. everything else.

Close the gap in small, reviewable changes, each with the evidence that it worked; re-walk the
affected journeys after each.

## Scope by the job

- **Whatever the core job needs in order to be dependable is in scope, however large; whatever it
  does not need is out, however easy.** "No new features" is the wrong rule, and so is "add
  whatever seems useful". If it cannot keep what it is given, add the keeping; if one platform
  cannot run it at all, make it run.
- **Refuse additions the bar does not need, and list what you refused.**
- **Dependable beats impressive.** When a feature and dependability conflict, dependability wins.

## Every platform and environment, for real

- **Run each engine, operating system, device class, board revision or site the bar names:**
  emulated where that is faithful, real where emulation would lie.
- **Detect capabilities instead of assuming them,** and give each missing capability a fallback or
  a plain explanation to the person.
- **Include the previous version's data and settings, other locales and scripts, and slow or
  metered networks** (or, for a venue or installation, the other rooms, weathers and times of day
  it will meet).
- **One you could not run is not verified, with the reason.** Never infer it from another that
  passed. Say first what you could not test: that is where the next complaint comes from.

## Failures caused on purpose

For each item the bar says must never be lost, make the bad day happen and watch what the person
would see: storage full or unavailable; offline in the middle of an operation; the process, tab or
device killed mid-write; sent to the background; permission refused, then granted; a slow device;
a wrong clock; two instances at once; an upgrade over existing data. For a physical or service
delivery: power cut, a supplier no-show, the wrong part delivered, a person absent, rain. Each is
certain to happen to someone; imagining it once is not causing it.

## Craft standard

For every surface a person touches:

- every state is designed: empty, loading, partial, error, offline, disabled, success;
- every action shows it was received within 100 ms, even if only to say it is working;
- every error says what happened and what to do next, in the person's words;
- it works at the smallest size the bar names (320 CSS px wide for the web) with no sideways
  scrolling, touch targets of at least 44 px, and text that reflows at 200% zoom;
- it is fully usable by keyboard with a visible focus, labelled for screen readers, and meets WCAG
  2.2 AA contrast;
- one set of spacing, type and colour values everywhere, in light and dark where the platform has
  both, with motion that respects reduced motion;
- nothing jumps, shifts or reflows after it has appeared.

For a result with no screen (a command line, an API, a library, a device, a printed document), the
standard applies to what it does have: help text, exit codes, error bodies, logs, lights, sounds,
labels, instructions. Polish is not ornament; it is the absence of rough edges. Take away before
you add.

## Budgets as checks

- **Every budget in the bar is asserted by a check that fails when it is exceeded:** in CI for
  software; in the recurring inspection or acceptance procedure otherwise. A budget measured once
  in a report is a snapshot, not a budget.

## Complexity budget

- **Every dependency, service, build step, abstraction, component, supplier and document names
  what breaks without it.** Prefer what the platform already provides.
- **Do not add a container, a framework, a state library, a queue, a cluster or a runbook because
  production projects have one.** Add it when the bar cannot hold without it, and say which item it
  holds. Microservices, queues and a cluster for a project with no users are a cost now and a
  migration later.
- **Remove what does not earn its place, and count what you removed.** Well-engineered systems look
  simple because someone kept saying no.

## Operable

- The running result can report its version, and there is a changelog a person can read.
- There are diagnostics a person can copy into a report with no developer present, containing
  nothing private.
- An update cannot strand anyone on a broken version or lose their data; rolling back is one
  action, and has been tried.
- For anything that runs as a service: a health check; an alert on each critical journey that fires
  before a person reports it; logs with enough context to diagnose a failure that cannot be
  reproduced, kept long enough to investigate one; a restoring action tried before it is needed
  (`operations.md §Incidents: restore first`).
- The repository holds only source: no build output, dependency folders, secrets, or links into
  someone's machine.

## Reviewing work

Applies to any work: a change, a deliverable, a report, a decision, and your own.

- **Review is by someone other than the author:** a person, or an agent in a fresh context given
  the work and its claims, never the context that produced it.
- **Every claim the work makes about itself is checked or marked unchecked.** A description, a
  status report or a handover note is a set of claims; check each against the actual result, by
  running, inspecting, measuring or asking the acceptor. Reading is not reviewing.
- **Check the requirement, not the implementation.** Read the original request, requirement or
  acceptance criteria line by line and mark each met, partly met or not addressed, with where it is
  settled. The requirement that was quietly dropped does not announce itself.
- **Check that the checks can fail:** a new test, inspection or gate is shown to detect the defect
  it exists for (`software.md §Tests that can fail`).
- **Distrust anything weakened to pass:** a loosened check, a skipped step, a widened tolerance, an
  exception swallowed. Each needs its stated reason.
- **Do not widen the scope:** problems the work did not introduce are recorded separately.
- **Say what you could not check, and why.** An unverified claim reported as unverified is useful;
  reported as fine, it is the failure the review exists for.
- **The verdict comes first:** one sentence on whether the work does what it says, then the
  evidence.
- **A review over nothing is not a pass:** if there was nothing in scope to review, say so.
