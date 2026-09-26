# Planning: deliverables, work, dependencies, schedule and resources

Load when planning work, sequencing it, scheduling it, assigning it, or when something changes a
date, a resource or the scope. These are established project-management methods (ISO 21502 and
the APM body of knowledge describe them); what follows is enough to apply them without either.
They are chosen by need, not all at once, and none of them is a separate document for its own
sake.

## Choosing methods by need

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

## Deliverables and work breakdown

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

## Work packages and acceptance criteria

Each work package records, in the project's tool (§Work records in the project's tool):

- the deliverable it belongs to;
- the responsible actor, and who accepts it;
- acceptance criteria: concrete, checkable conditions on the actual result, agreed before work
  starts;
- the procedure that will produce and verify it (`../SKILL.md §4. Procedures and evidence`);
- its prerequisites and the resources it needs;
- an estimate, and dates where the schedule needs them;
- its state: not ready, ready, in progress, waiting (on what), done (with a link to evidence).

## Milestones as usable slices

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

## Dependencies and the schedule

1. **Record each real prerequisite as a link** between work packages ("B cannot start until A is
   done"; occasionally "cannot finish until", or a lag such as "concrete cures for 7 days").
   Record outside handoffs (a supplier delivery, an approval, a client's content) as work
   packages or milestones owned by that party, with the date they committed to.
2. **Estimate each duration** in working time, and note the calendar it runs on (a person's
   working days, a supplier's lead time in calendar days, a lab's opening hours).
3. **Draw the network or the Gantt chart when it makes coordination clearer;** the records hold
   the links and dates, the chart is a view of them.
4. **Keep the schedule honest:** a date is either committed by the party who controls it, or an
   estimate marked as such.

## Critical path and resources

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

## Flow: boards and Kanban

- **A board is a view of the work records' state** (not ready, ready, in progress, waiting, in
  review, done). It is not a second plan.
- **Real Kanban adds explicit rules:** the columns and what moves an item between them, a limit
  on work in progress per column, and attention to items that wait. Adopt them when flow matters
  (continuous work, support, operations), not for a one-off build.
- **Limit work in progress** even without Kanban: finishing one thing beats starting three.

## Responsibilities

- **Every deliverable and work package has one responsible actor and one acceptor.** For a small
  project that is enough.
- **Use a responsibility matrix when roles or handoffs become ambiguous:** for each deliverable or
  decision, who is Responsible (does it), Accountable (one person who decides and accepts),
  Consulted (asked before), Informed (told after). One Accountable per row.
- **The operating model** records, for each procedure, who performs it today (a person, an agent
  or automation), who approves it, and the fallback (`../SKILL.md §4. Procedures and evidence`).
  A procedure only one person or one agent can perform is one absence from stalling.

## Risks, assumptions, issues and dependencies

- **Keep one consolidated record** of the material items, not four empty logs:
  - a *risk* is something that may happen, with its likelihood, its impact, the response
    (avoid, reduce, transfer, accept) and an owner;
  - an *assumption* is something taken as true without evidence, with how and when it will be
    checked;
  - an *issue* is something happening now that needs action, with an owner and a date;
  - a *dependency* on something outside the project, with who controls it.
- **Consider them on every project;** revisit them at each review and whenever the evidence
  changes. A risk that happened becomes an issue; an assumption that failed changes the plan.

## Change control

1. **Anything that changes agreed scope, resources, dates, quality or acceptance** is a change
   request, however small it looks and whoever asks for it.
2. **Assess it:** what it affects (deliverables, schedule, cost, risks, acceptance), and the
   options, including not making it.
3. **Decide it within the delegated authority** set in the briefing, and record the decision and
   its effects; outside that authority, take it to the person who can decide, with the
   assessment, and do not act on it until decided.
4. **Update the records** (work packages, schedule, acceptance criteria, risks) so the plan and
   the work agree.

## Rolling-wave planning and exploration

- **Plan the near term in detail and the distant work honestly:** the next milestone as work
  packages with estimates; later ones as deliverables with ranges. Detail the next wave as the
  current one nears its end.
- **Where nothing is known** (an invention, a system nobody has built), write the unknowns as
  questions; for each, the cheapest experiment, simulation or prototype that would answer it; run
  the ones that decide the most first; record every result, failures included, as evidence.
  Search prior work first, so the experiment starts where others stopped.

## Resources and their sources

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

## Estimates and arithmetic

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

## Work records in the project's tool

- **Use the fields and links the tool already has.** For example, in an issue tracker with
  projects: a deliverable as a parent item with its work packages as sub-items; prerequisites
  as "blocked by" links; owner as the assignee; dates, estimates and state as project fields;
  milestones as the tool's milestones; the board and the roadmap as views. In a spreadsheet:
  one row per work package with the same columns. Offline or with nothing else: one Markdown
  file with a table, kept in the repository.
- **No invented ID scheme or file format.** Refer to items by the tool's own identifiers.
- **Mark every export with its source and date,** and do not edit it as a separate plan.
