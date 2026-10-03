---
layout: guide
excerpt_separator: ""
title: "Planning: deliverables, work, dependencies, schedule and resources"
description: "Every project has work to choose and records to keep, so read at least §Choosing methods by need and §Work records in the project's tool on every project. Read the rest when there are dependencies, dates, shared resources, risks, or changes to agreed scope."
permalink: /conductor/guidance/planning.html
kind: guidance
file: "guidance/planning.md"
source_url: /.well-known/agent-skills/conductor/guidance/planning.md
toc: [{"id": "choosing-methods-by-need", "title": "Choosing methods by need"}, {"id": "deliverables-and-work-breakdown", "title": "Deliverables and work breakdown"}, {"id": "work-packages-and-acceptance-criteria", "title": "Work packages and acceptance criteria"}, {"id": "milestones-as-usable-slices", "title": "Milestones as usable slices"}, {"id": "dependencies-and-the-schedule", "title": "Dependencies and the schedule"}, {"id": "critical-path-and-resources", "title": "Critical path and resources"}, {"id": "flow-boards-and-kanban", "title": "Flow: boards and Kanban"}, {"id": "responsibilities", "title": "Responsibilities"}, {"id": "risks-assumptions-issues-and-dependencies", "title": "Risks, assumptions, issues and dependencies"}, {"id": "change-control", "title": "Change control"}, {"id": "rolling-wave-planning-and-exploration", "title": "Rolling-wave planning and exploration"}, {"id": "resources-and-their-sources", "title": "Resources and their sources"}, {"id": "estimates-and-arithmetic", "title": "Estimates and arithmetic"}, {"id": "time-limits", "title": "Time limits"}, {"id": "work-records-in-the-project-s-tool", "title": "Work records in the project's tool"}]
---
{% raw %}Every project has work to choose and records to keep, so read at least §Choosing methods by need
and §Work records in the project's tool on every project. Read the rest when there are
dependencies, dates, shared resources, risks, or changes to agreed scope. These are established project-management methods (ISO 21502 and
the APM body of knowledge describe them); what follows is enough to apply them without either.
They are chosen by need, not all at once, and none of them is a separate document for its own
sake.

## Choosing methods by need {#choosing-methods-by-need}

| Mechanism | What it supplies | Use it when |
|---|---|---|
| Deliverable list; product and work breakdown | What is produced, and the work each needs | Always a list; a hierarchy when there are several deliverables, teams or substantial scope |
| Work packages and tasks | Assignable units with acceptance criteria | Always; detailed enough to choose and verify the next action, no further |
| Dependency network | What is blocked by which prerequisite | Whenever one piece of work needs another first, or an outside party must hand something over |
| Milestones and a Gantt schedule | Dates, durations, parallel work, handoffs | When deadlines, lead times, availability or coordination materially affect delivery |
| Critical path and resource analysis | Which delays move the finish; whether the plan is feasible | For connected schedules; include calendars, unavailable equipment and shared people |
| Task board; Kanban when appropriate | Work in progress, waiting and done | For active flow; real Kanban also has an explicit workflow and work-in-progress limits |
| Responsibility matrix (RACI) | Who performs, decides, is consulted or informed | When roles or handoffs become ambiguous; otherwise a named owner and acceptor suffice |
| Risks, assumptions, issues, dependencies (RAID) | Uncertainty, obstacles and responses | Consider material items on every project; one consolidated record, not empty logs |
| Change control | Effects on scope, resources, dates, quality, acceptance | Whenever something agreed would change |
| Rolling-wave planning | Near-term detail, honest distant estimates | When uncertainty makes a detailed long-term schedule unreliable |

These are different relationships: a breakdown says what work belongs to a deliverable; a
dependency says what must happen before other work can proceed; a Gantt chart shows time; a board
shows workflow state; an architecture diagram describes the product. None substitutes for another.

## Deliverables and work breakdown {#deliverables-and-work-breakdown}

1. **List the deliverables** (the product breakdown): every output the project produces or
   hands over, including the ones that are not the main product: documentation, training,
   certification files, packaging, a handover pack, an archive.
2. **For each deliverable, list the work it needs** (the work breakdown): design, build or make,
   procure, inspect, test, install, rehearse, review, accept.
3. **The breakdown covers everything and nothing twice:** all the work, at every level, is the
   sum of its children; work that belongs to no deliverable is a question (it serves nothing, or
   a deliverable is missing).
4. **Break down only as far as needed:** a leaf is a work package when one owner can do it, its
   acceptance is checkable, and it fits within one reporting period. Do not atomise into
   keystrokes.

## Work packages and acceptance criteria {#work-packages-and-acceptance-criteria}

Each work package records, in the project's tool (§Work records in the project's tool):

- the deliverable it belongs to;
- the responsible actor, and who accepts it;
- acceptance criteria: concrete, checkable conditions on the actual result, agreed before work
  starts;
- the procedure that will produce and verify it (`../SKILL.md §4. Procedures and evidence`);
- its prerequisites and the resources it needs;
- an estimate, and dates where the schedule needs them;
- its state: not ready, ready, in progress, waiting (on what), done (with a link to evidence).

## Milestones as usable slices {#milestones-as-usable-slices}

- **Vertical slices, not layers.** "1: backend. 2: frontend. 3: hardware. 4: integration."
  leaves nothing anyone can use until the last layer, so the first setback leaves nothing. Each
  milestone leaves something a person can use, and names the measures it moves.
- **A walking skeleton before any breadth:** the thinnest version of the first journey, end to
  end through every stage (built from clean, a test seen to fail, released or deployed or
  installed, observed in use, and rolled back once). For a physical product, one real reading or
  action on the bench, confirmed by an independent measurement (`physical.md §Commands and
  observed outcomes`). Create only the folders, services, parts and dependencies the skeleton
  uses; an empty folder for a service that may exist one day is a decision taken without
  evidence.
- **The first release to real people is an early milestone,** with its route to them ready.
- **Each milestone ends with a review** before the next starts (`quality.md §Reviewing work`;
  for anything already running, `operations.md §Periodic review`).

## Dependencies and the schedule {#dependencies-and-the-schedule}

Across projects, link only real prerequisites and shared-resource constraints in their existing
records. Each project retains its own objective, authority and acceptance; being in one workspace
does not make all adjacent or parked work commissioned (`../SKILL.md §1. Classify the project`).

1. **Record each real prerequisite as a link** between work packages ("B cannot start until A is
   done"; occasionally "cannot finish until", or a lag such as "concrete cures for 7 days").
   Record outside handoffs (a supplier delivery, an approval, a client's content) as work
   packages or milestones owned by that party, with the date they committed to.
2. **Estimate each duration** in working time, and note the calendar it runs on (a person's
   working days, a supplier's lead time in calendar days, a lab's opening hours).
3. **Draw the network or the Gantt chart when it makes coordination clearer;** the records hold
   the links and dates, the chart is a view of them.
4. **Keep the schedule honest:** a date is either committed by the party who controls it, or an
   estimate marked as such. What may stand as that source, and what may not, is §Time limits.

## Critical path and resources {#critical-path-and-resources}

For a connected schedule, work out which delays move the finish:

1. **Forward pass:** each package's earliest start is the latest earliest-finish of its
   prerequisites; earliest finish = earliest start + duration.
2. **Backward pass:** from the finish date, each package's latest finish is the earliest
   latest-start of the work that depends on it; latest start = latest finish − duration.
3. **Float** = latest start − earliest start. Packages with zero float form the critical path:
   any delay to them delays the finish. Near-zero float is nearly critical.
4. **Check resources, not just arrows.** For each person, machine, room or budget, add up the
   demand per period against availability (holidays, other projects, a machine booked
   elsewhere). Where demand exceeds it, move work within its float first; if that is not enough,
   the finish moves, and the plan says so.
5. **When anything changes** (a delivery slips, a person is unavailable, an estimate was wrong),
   recompute, update the forecast, and tell the owner which milestones and acceptances move.
   Pick the next ready work from what the new schedule allows; do not mark delayed work done or
   rebuild unrelated work to look busy.

A timeline view in a tool is not a computed critical path or a resource-feasible schedule. If the
project needs these and its tool cannot provide them, choose an existing scheduling tool on that
requirement (`decisions.md`); do not build one.

## Flow: boards and Kanban {#flow-boards-and-kanban}

- **A board is a view of the work records' state** (not ready, ready, in progress, waiting, in
  review, done). It is not a second plan.
- **Real Kanban adds explicit rules:** the columns and what moves an item between them, a limit
  on work in progress per column, and attention to items that wait. Adopt them when flow matters
  (continuous work, support, operations), not for a one-off build.
- **Limit work in progress** even without Kanban: finishing one thing beats starting three.

## Responsibilities {#responsibilities}

- **Every deliverable and work package has one responsible actor and one acceptor.** For a small
  project that is enough.
- **Use a responsibility matrix when roles or handoffs become ambiguous:** for each deliverable or
  decision, who is Responsible (does it), Accountable (one person who decides and accepts),
  Consulted (asked before), Informed (told after). One Accountable per row.
- **The operating model** records, for each procedure, who performs it today (a person, an agent
  or automation), who approves it, and the fallback (`../SKILL.md §4. Procedures and evidence`).
  A procedure only one person or one agent can perform is one absence from stalling.

## Risks, assumptions, issues and dependencies {#risks-assumptions-issues-and-dependencies}

- **Keep one consolidated record** of the material items, not four empty logs:
  - a *risk* is something that may happen, with its likelihood, its impact, the response
    (avoid, reduce, transfer, accept) and an owner;
  - an *assumption* is something taken as true without evidence, with how and when it will be
    checked;
  - an *issue* is something happening now that needs action, with an owner and a date;
  - a *dependency* on something outside the project, with who controls it.
- **Consider them on every project;** revisit them at each review and whenever the evidence
  changes. A risk that happened becomes an issue; an assumption that failed changes the plan.

## Change control {#change-control}

1. **Anything that changes agreed scope, resources, dates, quality or acceptance** is a change
   request, however small it looks and whoever asks for it.
2. **Assess it:** what it affects (deliverables, schedule, cost, risks, acceptance), and the
   options, including not making it.
3. **Decide it within the delegated authority** set in the briefing, and record the decision and
   its effects; outside that authority, take it to the person who can decide, with the
   assessment, and do not act on it until decided.
4. **Update the records** (work packages, schedule, acceptance criteria, risks) so the plan and
   the work agree.

## Rolling-wave planning and exploration {#rolling-wave-planning-and-exploration}

- **Plan the near term in detail and the distant work honestly:** the next milestone as work
  packages with estimates; later ones as deliverables with ranges. Detail the next wave as the
  current one nears its end.
- **Where nothing is known** (an invention, a system nobody has built), write the unknowns as
  questions; for each, the cheapest experiment, simulation or prototype that would answer it; run
  the ones that decide the most first; record every result, failures included, as evidence.
  Search prior work first, so the experiment starts where others stopped.

## Resources and their sources {#resources-and-their-sources}

- **Choose every resource's source; do not take the first.** Accounts, keys, models and the
  agent's token budget, hosting, domains, parts and test devices, suppliers, venues, people and
  hours, money. For each, compare at least two sources, including what the owner already has and
  building or making it, on cost now and at the target size, lock-in, lead time, and who has to
  act (`decisions.md`).
- **Record, for each resource, the decision that chose its source, or that the owner already has
  it.**
- **Send the owner one message with the whole resource table and a recommendation;** never nag
  toward a vendor. A resource the owner cannot provide is a constraint to route around: a free
  tier, a grant, a cheaper part, a borrowed tool, something built.
- **Set a budget for agent and model use,** and record spend against it.
- **At each review compare spend with budget for every line** (hosting, services, parts,
  contractors, agent and model use), note free tiers that ended and prices that moved, work out
  the runway, and route around what changed: another source, a cheaper design, a funding route.
  Money is a constraint to engineer around, never the reason a project stops.

## Estimates and arithmetic {#estimates-and-arithmetic}

- **Show every calculation with its units and inputs,** so another person can redo it.
- **Recompute every number you rely on,** including a supplier's or vendor's, which is a claim
  until a second source or a measurement confirms it.
- **Where a calculation would rest on a guess, simulate or prototype.**
- **Name the assumptions that would change the answer, and by how much they would have to move.**
- **Estimate durations as ranges where uncertain** (an optimistic, a likely and a pessimistic
  value; a common point estimate is (optimistic + 4 × likely + pessimistic) ÷ 6), and say which
  estimates are guesses.

Failures this prevents: a battery that lasts two days where the idea promised a season; a free
tier that becomes a four-figure bill at the target size; a bill of materials above the price.

## Time limits {#time-limits}

A time limit is a check, in the same way a budget is (`quality.md §Budgets as checks`). A date, a
quarter or a duration in the schedule is kept only when its source is named. Otherwise the check
fails and the run stops. This section says what the conductor can time, how that limit is
reached, and the line an unsourced date may not cross.

**What can be timed**

- **The next wave, as a distribution from work the doer has already finished.** For software,
  the method is Joel Spolsky, Evidence-Based Scheduling, 26 October 2007
  (https://www.joelonsoftware.com/2007/10/26/evidence-based-scheduling/). Break a task the
  person has done before into at most 16 hours. A larger package means the steps were not
  listed. Only the actor who will do the work estimates it. Another actor's number is not a
  source. Do not press an estimate shorter to protect a date. Velocity is that actor's
  estimate divided by the time the task actually took. His practice drops velocities older
  than about six months. A new estimator keeps a stand-in history, deliberately wide, until
  about half a dozen real tasks exist. Do not add the estimates into one ship date. Draw many
  futures. His essay draws 100, and treats each as 1 percent. In each future, divide each
  estimate by a velocity drawn at random from that history, then place the hours on that
  person's calendar. The result is a distribution, not a day. In each round, the team is done
  when the last person finishes. A person shared with other work is not free for the whole of
  that round (`§Critical path and resources`).
- **A committed date.** Only when the party who controls the date has committed, and the record
  names the artefact (a signed date, a written confirmation, a contract clause). An estimate is
  not that artefact.
- **A reference class of the same kind of finished work.** Bent Flyvbjerg, "From Nobel Prize to
  Project Management: Getting Risks Right", Project Management Journal, vol. 37, no. 3, August
  2006, pp. 5-15 (arXiv:1302.3642), gives three steps. Identify a class of past similar
  projects, broad enough to be statistically meaningful and narrow enough to be comparable.
  Establish the probability distribution from credible empirical data for a sufficient number
  of projects in that class. Place this project on that distribution. The outside view uses the
  outcomes of similar completed actions. It does not forecast the events inside this one. The
  paper's curriculum case is one project of that kind. The team's own estimates ran from 18 to
  30 months. About 40 percent of the comparable efforts were abandoned. The rest took seven to
  ten years. The work finished eight years later. Those figures time curriculum work of that
  kind. They do not time a software change. A different kind of work is not a source. Record
  that the class was rejected, and do not copy its figures.
- **The same method on a different class is still not this project's numbers.** Flyvbjerg, Hon
  and Fok, arXiv:1710.09419, submitted 3 October 2017, report a 2012 Hong Kong Development
  Bureau study. It covered 25 roadwork projects. Forecast costs and durations were compared
  with actual outcomes. The projects were benchmarked against 863 similar projects. The
  abstract states those counts. It does not state a percentage to lift. The roadworks
  distribution does not time software.

**When nothing above exists**

No history of finished tasks, and no opened class of the same kind, means the next work is to
measure or to open a class. Until then the item is unscheduled. It carries no calendar date, no
quarter and no duration. Spolsky's half-dozen tasks are his stated practice for a software
estimator. They are not a law for every trade. Say whose practice a threshold is.

**What this procedure will not treat as a limit**

- The weighted average in §Estimates and arithmetic is an inside view of this task. It is not a
  reference class and it is not a measured velocity. The curriculum case is why: the inside
  estimates and the outcomes of similar finished work were different distributions.
- One ship date as the sum of the estimates. Spolsky's point is that the sum sounds right and
  is the wrong result.
- A shorter estimate written to keep a date. His picture is a box of wood blocks. Use a bigger
  box, or fewer blocks. Do not shrink the blocks. If the date must move, cut scope or move the
  date. On Excel 5, the feature list would not fit the schedule, so the team cut it and called
  the cuts a deferral to the next version. When that next list was reviewed, not one deferred
  feature was worth doing. Cutting scope was the schedule. Shrinking the estimates would have
  hidden the choice.
- An old date kept by adding people. His essay says new people will probably work at 50 percent
  for several months, and will slow the people who teach them. That 50 percent is his
  illustration, not a constant to paste into a plan. Adding people starts a new estimate.
- A multiplier in place of a breakdown. He writes that thinking of the code without listing the
  steps makes the work seem to take n, when listing the steps makes it more like 4n. That is
  what an unlistable package hides. It is not a measured ratio to multiply into a schedule. The
  remedy is the 16-hour breakdown, not a multiplier.
- A space-flight confidence level copied onto a small task. NASA's planning page states a joint
  confidence level as the probability that cost is at or under the target and the schedule
  finishes at or under the target date. It describes CADRe as the historical record of cost,
  schedule and technical attributes for analogous projects, completed at each milestone and
  stored in ONCE (https://www.nasa.gov/ocfo/ppc-corner/ppc-guidance-documents/). The Schedule
  Management Handbook and Cost Estimating Handbook Appendix J are listed there. This procedure
  does not take a percentage from a handbook it has not opened, and it does not apply one
  agency's threshold to a different kind of work.

**How a limit is written, so a check can see it**

In the schedule record, under a heading `## Schedule`, each item uses one of these markers.
The text after the colon is not empty.

- `measured:` the doer's own completed tasks, which velocities were kept, and the distribution
  that followed. For software, name Evidence-Based Scheduling when that is the method used.
- `committed:` the artefact and the party who controls the date.
- `reference class:` the opened source, the class, and the figure that source states. A class
  of a different kind of work is recorded as rejected, not used.
- `unscheduled:` why there is no history and no opened class. No date, quarter or duration on
  that item.

`scripts/check_time_limits.py` reads that section. A date, a quarter or a duration with none of
the first three markers fails, and the message names the claim. A marker with nothing after the
colon fails. An unscheduled item that still states a date, a quarter or a duration fails. A
file with no `## Schedule` section passes, because it claimed no schedule. The check has to be
run. A rule that is not run does not block the work.

**When the date slips**

Recompute. If the ship date moves later by more than one day per day, work is being added
faster than it is finished. That is Spolsky's stated test, not a new ratio. Cut scope or move
the date. Do not edit the velocities to recover the old day.

## Work records in the project's tool {#work-records-in-the-project-s-tool}

- **Use the fields and links the tool already has.** For example, in an issue tracker with
  projects: a deliverable as a parent item with its work packages as sub-items; prerequisites
  as "blocked by" links; owner as the assignee; dates, estimates and state as project fields;
  milestones as the tool's milestones; the board and the roadmap as views. In a spreadsheet:
  one row per work package with the same columns. Offline or with nothing else: one Markdown
  file with a table, kept in the repository.
- **No invented ID scheme or file format.** Refer to items by the tool's own identifiers (an issue
  number, a spreadsheet row). A plain file has none: number the rows of each table (1, 2, 3) and
  refer to them in words, such as "work item 3" or "the second measure". Do not create families of
  prefixed codes (G1, M2, J3, W4, Q5) or rules for cross-referencing them between files; that is
  the private format this guidance exists to avoid.
- **Mark every export with its source and date,** and do not edit it as a separate plan.
- **Use an existing linked view for shared state and takeover.** Show objective, authority,
  accepted core, active work, duty modes, evidence and exceptions from the authoritative records.
  If no suitable view exists, `../templates/state.md` is a small optional Markdown fallback,
  not another plan, store or source of authority. Verify the next operator's actual access,
  authority and capability before declaring a takeover complete.
{% endraw %}
