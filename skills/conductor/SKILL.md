---
name: conductor
description: One entry point for delivering any project, software, physical, service or hybrid, from nothing, a single word, an idea, an existing build or a live product, to an accepted result, and for handing over whatever must keep running. It classifies the project, runs a control loop of established project responsibilities (objective and acceptance, deliverables and work, owners, dependencies and resources, execution within authority, verification and validation, change, handover or closure), keeps one authoritative set of work records in the project's own tool, and never counts work as done without evidence about the actual result and an accountable verifier. Focused guidance loads only when the project needs it.
---
# Conductor: deliver any project, with evidence

Start here, whatever the project is and whatever state it is in. This file decides what to do
next and which guidance to load. Do not choose a guidance file by its title and work from it
alone: each one is a part of this loop, not a substitute for it.

## How to use this

- **Read this file whole, then load guidance as §Guidance to load says.** When the context
  window is small, load one guidance file at a time, and only the sections the current work
  needs; this file stays in view.
- **Nothing here depends on a particular agent, harness or hosted service.** Where a step
  names a pull request, CI, an issue tracker, a package registry or a web search, use the
  project's own equivalent, which may be local and offline. Send nothing anywhere beyond what
  the project's confidentiality rules allow (`guidance/confidentiality.md`).
- **The people.** The *owner* decides what the project is for and approves what only they can.
  Each piece of work has a *responsible* actor who performs it (a person, an agent or
  automation), an *acceptor* who accepts the result, and a *verifier* who checks the evidence
  and is not its author. Operations, once handed over, have a named *operator*.
- **Established practice, not a new method.** The planning and delivery methods named in the
  guidance are the ordinary ones (work breakdown, dependencies, schedules, boards, RACI, risks,
  change control, decision records, verification and validation). Use the ones the project
  needs, in the tools it already has. Build a tool only when a demonstrated need is not met by
  one that exists.
- **Stay within the law and the terms of every service used.**

## 1. Classify the project

Before planning, write down, in the project's records, and revisit whenever the evidence
changes:

1. **The output.** Software; physical (a device, an installation, a product made or fitted);
   service or creative (an event, a film, a document, training, a delivered service); or a
   hybrid, naming which parts are which.
2. **The starting state, from evidence.** Nothing yet, or a single word; an idea; an existing
   project (a prototype, a half-built or inherited build, a working product with gaps); live
   and failing people now; stalled or drifting. A report, a README or a status page is a claim
   about the state, not the state: check what exists and what runs.
3. **Scale and uncertainty.** How many deliverables, people, teams and outside parties; lead
   times; money at stake; how much of the work is already known. This sets how much planning
   the project gets (`guidance/planning.md`).
4. **Finite, ongoing or mixed.** What is delivered and accepted, what must keep operating,
   and who or what operates each part. Record each continuing duty's agreed mode: manual,
   assisted or autonomous. These are literal outcomes, not labels: autonomous duties complete
   without human intervention; assisted duties name the human checkpoints; manual duties have
   a usable human procedure (`guidance/operations.md`). Reuse adequate existing cloud jobs,
   services and operators. Do not impose continuing operation on a finite project or substitute
   a manual procedure for an agreed autonomous outcome.
5. **Confidentiality.** Whether anything (the idea, code, data, designs, names, even the fact
   that the project exists) must not leave. If so, load `guidance/confidentiality.md` before
   anything is sent anywhere, including searches and remote models.
6. **Authority and budget.** What the owner decides, what is delegated and within which
   limits, and the budget in money, time and agent or model use (§8).
7. **The operator of the work.** A person, an agent in a working harness, an agent that must
   first get a harness, several agents, or a build that will run unattended
   (`guidance/autonomy.md` for any but the first two).
8. **Actions on the physical world.** Anything the work will move, heat, dispense, spend or
   send (`guidance/physical.md`).

**An existing project** has its records written from what is there before anything changes:
what it is for (in the owner's words), what exists and what actually runs, the decisions it
already embodies with the evidence they had (often none), and those nobody can justify marked
for revisiting. Then it starts where §2 says, like any other.

**Nothing, or a single word:** `guidance/product.md §Starting from nothing or a single word`.

**Several projects or a workspace.** Identify each project and continuing duty with its own
objective, authority, records and acceptance. Apply the loop to the work commissioned in each;
coordinate actual dependencies and shared resources through linked views in existing records.
Make competing priorities explicit; allocate only within the owner's priorities and delegation.
Do not merge separate authorities, copy private runtime data into source, override deterministic
responsibilities or restart parked or retired work without authorisation. Parked work may be
evaluated within an authorised review and recommended for reopening; that does not commission it.

## 2. The control loop

These are the responsibilities of any project. Work through them, and come back to any of
them whenever the evidence changes.

1. **Establish the objective and acceptance.** What changes in the world, for whom; the
   measures that show it; what an accepted result must satisfy
   (`guidance/product.md`).
2. **Identify the deliverables and the work.** What is produced, and the work each needs,
   broken down only as far as choosing and verifying the next action requires
   (`guidance/planning.md`).
3. **Assign ownership.** A responsible actor and an acceptor for every deliverable and work
   package; a named owner for every area the product needs (`guidance/product.md §Areas and
   owners`).
4. **Account for dependencies and resources.** What must happen before what; the people,
   equipment, parts, money, access and time each piece needs, and when they are available;
   the forecast that follows (`guidance/planning.md`).
5. **Execute within authority.** Take the next ready work package (§5); perform it by its
   procedure (§4); run its gates (§6); record the result (§3); take the next. Nothing outside
   the delegated authority is done without the decision it needs (§8).
6. **Verify and validate.** The result meets its requirements, and it serves its intended use
   for the people and operators it is for (§6).
7. **Handle changes.** Requests, new evidence, changed dates or resources, and decisions whose
   reopening condition fired (§7).
8. **Hand over or close** (§9).

**Recurring activities.** Discovery, design, risk and validation are not one-time steps before
building. Return to them when a measure moves the wrong way, a test with people fails, a
supplier or resource changes, a decision's reopening condition fires, or a new need appears.

**Interrupts.** Harm to people or their data right now comes before everything: restore first
(`guidance/operations.md §Incidents: restore first`), then return to the loop. A change
request enters at §7. A decision's reopening condition enters at
`guidance/decisions.md`. An exhausted budget pauses the work with the next step recorded (§8).

**Where to start.** Scope comes from the request. When the request is the project itself
(start it, finish it, get it ready for people), start at the first responsibility whose
acceptance is not met, judged from evidence rather than from the project's label: a live product
with no measurable objective starts at 1; an idea whose objective and deliverables are clear but
whose dependencies are unknown starts at 4. When the request is a bounded piece of work (a bug
fix, a review, a change), readiness (§5) applies to that work and its actual dependencies; a
project-wide responsibility comes first only when its absence blocks the requested work or its
acceptance. A bounded fix does not rebuild the business case.

**The smallest loop that finishes things.** One ready work package at a time: do it, run its
gates, record it with a link to its evidence, update the state note, take the next. Review at
each milestone before starting the next (`guidance/quality.md §Reviewing work`).

**Coverage before methods.** For a whole-project request, reconcile the recorded requirements,
supported features, journeys, surfaces, state, external actions and continuing duties with the
actual project. Include indirect outputs: messages, reports, background work, administration,
machine interfaces and handoffs. Each item has evidence, an open gap or an authorised scope change.
For bounded work, account for its consequences: behaviour and design, interfaces and words,
data and migrations, security/privacy/permissions, dependencies or parts, checks/delivery and
operations/handoffs. Discover these from actual sources, entry points and operating services,
not only a task label. Select guidance from that inventory; record considered exclusions with
their reasons. An unread section does not prove non-applicability. Keep this proportionate in
existing records, not another tracking system.

**Challenge before commitment.** Apply `guidance/quality.md §Challenging recommendations and
existing methods` to consequential proposals, including your own. Turn model suggestions into
testable hypotheses and compare defensible alternatives (`guidance/decisions.md §Options`).

## 3. Work records

- **One authoritative set of work records, in the project's existing tool**: its issue
  tracker, project board, spreadsheet, or plain files in the repository when the project is
  offline or has nothing else. If it has no tool and needs one, choose an existing tool on the
  project's requirements (`guidance/decisions.md`); do not build one.
- **Each work item records** the deliverable it belongs to, its owner, its acceptance
  criteria, its state, its dependencies and resource constraints, and, where useful, an
  estimate and dates. When it is done it links to its evidence. Use the tool's own fields,
  identifiers and links; do not invent an ID scheme or a file format. In a plain file, which has
  no identifiers of its own, number the rows and refer to them in words ("work item 3", "the
  second measure"); do not create families of prefixed codes (G1, M2, J3, W4) or rules for
  cross-referencing them: that recreates a private format everyone must learn
  (`guidance/planning.md §Work records in the project's tool`).
- **Views are views.** A board, a Gantt chart, a burn-down or a report is a view of the
  records, or an export marked with its source and date. Never edit an export as a second plan.
- **Authority and settled core.** Name the current requirements, accepted decisions, delegated
  limits and authoritative sources for policy and operating values. Record precedence where
  sources conflict; do not invent a universal file hierarchy. Reconcile contradictions within
  authority and mark superseded material historical. Give repeated material facts one source:
  derive the copies where practical, otherwise check them. Historical evidence retains its dates
  and values. Outward prose includes material terms and consequences, without unnecessary
  implementation detail; simplification remains truthful.
- **The project's other records** live where the project keeps documents (often a `docs/`
  folder, or the team's shared space): the objective, measures and acceptance; the production
  bar; decisions as ADRs (`templates/adr.md`); the briefing and standing limits; choices made on
  the owner's behalf; risks, assumptions, issues and dependencies; handover notes.
- **Every change links to what it serves and how it was verified.** In software: the change
  references its work item, and its description names the evidence (the test seen to fail
  without it, the measurement before and after). Outside software: the record of the work
  names the work item and the inspection, acceptance or measurement that verified it.
- **Nobody works in the dark.** The owner can see the project's state as measured, not as
  opinion; the options and their costs before any choice; why each part exists; and who
  performs each procedure. A gap in what someone can see gets its own record.
- **A short state note** says where the work is, what is waiting and on what, and what is
  next. It is rewritten, not appended, and it is a view: the records are the truth.
- **A shared view for takeover.** Reuse that note or the project's native view; `templates/state.md`
  is a Markdown fallback, not a mandatory store migration. Link the milestone, accepted core,
  operating evidence, active work and owner exceptions to their authoritative records. Change
  ownership/mode there, then refresh the view. Takeover verifies authority, access, capability,
  prerequisites and resumption state; editing a name or mode does not establish them. Qualified
  human and agent operators use shared procedures within the same limits. Do not build a
  dashboard merely to provide this summary.

## 4. Procedures and evidence

- **Every stage of the work is a reproducible procedure with a responsible actor and
  evidence.** A script or command is one form. An inspection, a rehearsal, an operator
  demonstration, an installation, a commissioning test or a client acceptance is another.
  Write each so another responsible person or agent could repeat it; nothing lives only in one
  person's head or one agent's tools.
- **Evidence refers to the actual output, version and environment.** The command, its exit
  code and its summary line, verbatim; the inspection record with who, when and what was
  measured; the photograph or reading timestamped after the action; the acceptance signed by
  the acceptor.
- **Work nobody performed stays pending.** Generating a plan or a checklist does not complete
  the work it describes. An order is not receipt; receipt is not a passed inspection; an
  acknowledgement from a device or a service is not the outcome; passing software tests is not
  system acceptance.
- **A procedure's report must be able to fail.** Verify each step by its effect, not by the
  absence of an error (`guidance/software.md §Automations that report their own failure`).
- **The operating model.** For each procedure: who performs it today (a person, an agent or
  automation), who approves it, and the fallback if they are unavailable. Moving between
  manual, hybrid and automated changes this record, not the procedure. Anything that cannot be
  undone keeps a person's exact approval or explicit scoped standing authority at every level
  of automation (§8).

## 5. Readiness, blocking and resumption

- **Show that work is ready before starting it:** its prerequisites are met, with evidence;
  its resources (people, equipment, parts, money, access, time) are available; its acceptance
  criteria are written in the work records (§3), and on an existing project the records of what
  is there are written first (§1); and the action is authorised, within the standing limits or
  approved. No change to the product starts before this.
- **When work is blocked,** record the actual waiting condition (what, on whom or what, since
  when, expected when) and update the forecast (`guidance/planning.md §Critical path and
  resources`). Take independent ready work if there is any. Never mark blocked work done, and
  never rebuild unrelated work to fill the time. A block that persists gets another route to
  the same objective (`guidance/product.md §Alternative routes`).
- **When a wait could run past a date the work depends on,** record the latest date to
  decide, and before it put the choice, with a recommendation, to whoever decides. A fixed date
  that passes while work waits on an answer that never came is a failure of the plan.
- **On resumption** (a new session, a new context, another agent, after an interruption):
  1. read the real artifacts and external state first: the records, the repository, the
     tool, messages, order and delivery status, deployments, device state;
  2. for every action that might have happened (an order, a payment, a message, a deployment,
     a physical action), confirm whether it did before retrying; retry only when an
     observation shows it did not, or when the action is idempotent. A physical action is
     confirmed by its independent observation, not the device's acknowledgement, and a fault
     found this way is reported, not retried (`guidance/physical.md §Commands and observed
     outcomes`);
  3. carry over the standing limits and permissions unchanged;
  4. rewrite the state note, then choose the next ready work.
- **When a date, duration or resource changes,** recompute the forecast and say which
  milestones and acceptances move.

## 6. Gates: verification and validation

- **Every gate has three parts:** a concrete acceptance condition; evidence about the actual
  output, version and environment; and an accountable verifier, named. Failed or absent
  evidence cannot establish readiness.
- **Keep effective existing checks.** Changing records, tools or guidance does not silently
  remove safeguards. Every required rule has a verification method that can detect violation:
  existing project/provider checks where practical, otherwise competent independent inspection,
  rehearsal or acceptance. An enforcement replacement records its guarantee and demonstrates
  the replacement, or has an authorised exception. Do not build a general harness for one rule.
- **"Does not apply" is a recorded decision with its reason. An authorised exception names
  who authorised it, its scope and when it expires.** Neither is ever reported as a pass.
- **Verification and validation are different questions.** Verification: does the result
  meet its requirements? Validation: does it serve its intended use, for the people and
  operators it is for, and move the objective's measures? Acceptance needs both.
- **A check nobody has seen fail is a claim.** Every test, pipeline step, inspection or
  review checklist that a gate relies on has been shown to detect the defect it exists for.
- **The author does not approve their own work.** Review is by someone else: a person, or an
  agent in a fresh context given the work and its claims. A fresh-context review challenges
  claims; it does not replace competent human judgment, or an inspection the law requires
  (electrical, gas, structural, medical, food, radio certification and the like).
- **After a change, walk again the journeys it touches,** and measure again the way the
  measure says it is taken.
- **Gates run after the last change.** A result checked before a later change is not checked:
  before the verdict, revalidate every piece of evidence a later change could have affected.
  Re-run from cold (a clean checkout or setup, every gate again, every journey walked again) where
  risk or acceptance calls for it: a release, a handover, or the acceptor's criteria. A physical
  step is revalidated by the inspection, measurement or simulation its risk needs, not replayed by
  default.
- **A failed gate means another attempt or another route, never a lower gate.**
- **Completion is a delivered result and its acceptance,** not a count of closed tasks. An
  assessment with failed or unverified items is a completed assessment; on its own it does not
  support a claim that the result is ready to release or hand over.

## 7. Changes

- **Every change traces to the objective, a requirement or an accepted decision.** A change
  that serves none of them is a question for the owner, not work.
- **Requests, however worded** ("faster", "prettier", "scalable", "add AI"), are translated
  before they are acted on (`guidance/product.md §Requests, however they are worded`).
- **Measure before and after,** the way the measure says it is taken. Find the cause before
  choosing the change. Do not change anything on a guess.
- **Evidence in proportion to the stakes.** A change that is costly to reverse needs its
  decision first (`guidance/decisions.md`).
- **Read the accepted decisions a change touches.** Take a route that keeps the decision, or
  propose reopening it under the recorded conditions or an explicit authorised request, and
  obtain any required superseding decision before the change. A change that quietly
  contradicts a recorded decision is drift.
- **Authority is not immunity from scrutiny.** Challenge inefficient methods and empirical
  premises with evidence, even when current targets hold. Distinguish a suspected inefficiency,
  a demonstrated deficiency and a verified improvement. Propose reopening when the evidence
  warrants it; authorisation and the recorded reopening process still govern actual changes.
- **Whole or not at all.** A change is carried through everything it touches (in software:
  every layer, `guidance/software.md §Complete changes, nothing detached`; outside software:
  every drawing, document, procedure, record, label and supplier order), and what it replaces
  is removed.
- **Change control.** A change that affects agreed scope, resources, dates, quality or
  acceptance is made within the delegated authority and recorded; outside it, it goes to the
  person who can decide it first (`guidance/planning.md §Change control`).

## 8. Authority, budget and confidentiality

- **The briefing** (`guidance/autonomy.md §Briefing: ask once`, or, for a person-led project,
  a conversation recorded the same way) establishes what the owner decides, what is delegated
  and within which limits, the standing limits for anything outside the working environment
  (money, publishing or sending to people, physical actions, actions during an incident), the
  budget, and the confidentiality rules.
- **Inside the limits, act without asking. Outside them, take another route, or ask once with
  everything the owner needs to decide.**
- **Running existing code or equipment is an action with effects.** Before running it, find
  what it reads, writes, sends or moves: a hard-coded path, a real account or service, a device.
  For a test, baseline, mutation or walk from cold, redirect effects outside the working
  environment (a temporary folder, a test account, a simulator) or do not run it; a check that
  finds the real target stops the test. A deliberately live operating run instead verifies its
  target and explicit scoped authority, enforces the authorised limits and observes the actual
  outcome and failure paths. A test's permission never authorises a live run.
- **Write the plan before starting a piece of work.** Where the plan needs someone's approval
  and the harness can pause for it, wait. Where it cannot pause, state the plan and proceed with
  everything inside the delegated authority; an action outside it (a costly-to-reverse or
  irreversible action not covered by scoped standing authority, or anything over a standing
  limit) is recorded as proposed and not taken
  until it is approved.
- **Anything that cannot be undone** (spending, sending to a person, publishing, cutting,
  dispensing, deleting records, acting near people) needs a person's yes to the exact action
  and its parameters, or an explicit, scoped, written standing authorisation.
- **The budget** is counted as it is spent. At 80% slow down and tell the owner. When it runs
  out the work pauses and the project does not: the state note holds where the work is and the
  next step, and the report names the routes to continue.
- **Confidential projects** load `guidance/confidentiality.md` before anything leaves.

## 9. Closure and handover

- **A finite project closes** when its delivery is accepted by the named acceptor with
  evidence; its obligations are settled (payments, suppliers, licences, warranties, reports
  owed to a funder, client or authority, promises to people); its materials are archived where the owner can find them (records, source,
  drawings, files, credentials held by the owner rather than an agent); and what was learned is
  recorded.
- **When the last event arrives** (the delivery, the event, the installation), do in that same
  session everything closure needs that waits on no one: the records archived, each report owed
  drafted, what was paid set against what is receipted, the handover written, the lessons
  recorded. List what still waits on someone, with who and by when. A project waiting only on
  acceptance or a receipt is closed except for that item.
- **Whatever must keep running is handed over** (`templates/handover.md`): a named operator,
  their responsibilities, the resources and budget, the procedures, the review cadence and the
  triggers that call for action, the contacts, and access transferred with keys rotated. From
  then on `guidance/operations.md` applies to that operator.
- **Closing a project does not abandon the owner's broader goal.** A next objective starts as
  a new project, with this one's records. A blocked route gets alternatives costed honestly.
  If no feasible authorised route is demonstrated, record the evidence and uncertainties and
  propose the needed constraint or objective change; do not invent success or commission work.
- **A pause** keeps security updates, backups and the data people rely on running, and
  records what restarts the work.
- **Anyone could pick the project up from its records alone.**

## 10. Reporting

- **Every item ends as one of:** *verified* (performed or inspected, and the evidence agrees);
  *failed* (the evidence contradicts the claim); *not verified* (it could not be checked, with
  the reason); *not applicable* (with the recorded decision); *exception* (with who authorised
  it). The last two are never counted as passes.
- **Lead with one sentence: whether the work does what it claims.** Then say what could not be
  checked, and why, before the details.
- **One row per item the work promised** (each requirement, journey, check, step, decision,
  action or claim), each with its result and its evidence or reason.
- **Report workflow and delivery separately.** A correctly handled block is good workflow; it
  is not a delivery.
- **Quote evidence verbatim** where it is output.
- **A message that leaves states only what is true now.** An intention is written as an
  intention ("we intend to arrange cover"), never as done.
- **End every report with its counts**, for example: `14 verified, 2 failed, 3 not verified,
  2 not applicable of 21 items.`

## Guidance to load

Load by what the classification (§1) and the current work need. Each file starts with what it
covers; sections refer to each other as `file §Heading`.

| When | Load |
|---|---|
| Always, for the objective, measures, requests and reaching people | `guidance/product.md` |
| Always, at least `§Choosing methods by need` and `§Work records in the project's tool`; the rest when there are dependencies, dates, shared resources, risks or changes to control | `guidance/planning.md` |
| Any choice that matters: a tool, supplier, part, platform, design or route | `guidance/decisions.md` |
| Anything people or agents see, hear or operate | `guidance/design.md` |
| Setting or checking the bar a result must meet | `guidance/quality.md` |
| Any software in the output or in the work | `guidance/software.md` |
| Physical products, installations, devices, or actions on the world | `guidance/physical.md` |
| Service or creative delivery | `guidance/service.md` |
| Anything that keeps running, incidents, backups, periodic review | `guidance/operations.md` |
| An agent without a working harness, unattended runs, several agents | `guidance/autonomy.md` |
| Anything that must not leave | `guidance/confidentiality.md` |

Templates: `templates/adr.md` for decisions, `templates/handover.md` for handover,
`templates/state.md` for a shared state view when the project has no suitable one.
