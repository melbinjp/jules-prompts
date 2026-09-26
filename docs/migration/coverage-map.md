# Coverage map: from the current library to the conductor

Status: step 1 of the approved plan, for review. Nothing here is removed yet; the current
library stays in place until the trials in step 3 have been reviewed.

Baseline: every item below is read from commit `f5fc9c0e721f4323f4ee79554220bb76128f796d` by
`scripts/inventory_map.py`, which also checks that every item is listed here. That check is an
inventory aid only: it shows that nothing was forgotten, not that its meaning survived. The
meaning is for review, row by row.

How to read a row: the IDs it covers (`skill.R3-R7` means R3 to R7 of that skill's Requirements;
O objective, C context, R requirements, G guiding principles, E execution flow, D deliverables);
where the item lands in the conductor, as `file §Heading`; and how it lands, or why it is
removed. A destination marked **replaced** keeps the behaviour and changes the mechanism, most
often a home-made format replaced by an established one. **Removed** means the behaviour itself
is not kept, and the reason says why.

## What changes in kind, not item by item

These decisions recur through the map. Each is taken from the finalisation proposal.

1. **Home-made records become established ones.** `PROJECT.md` with G/M/J/R/K/MS rows, the
   `decisions/D0001` front matter, the `Serves:`/`Verified:` trailers and `check_trace.py` are
   replaced by: the objective, measures and acceptance criteria in the project's own records;
   decisions as ADRs (MADR); work items in the project's existing tool, with native links from a
   change to the work item and to its evidence. The rules those formats enforced (every decision
   has options and verified evidence; every change has a reason and a verification; nothing
   serves a rejected decision) are kept as instructions, and are checked at review.
2. **"holds / broken / skipped" becomes plain terms.** A result is verified, failed, or not
   verified (with the reason); an item may be not applicable (with a justified decision) or an
   authorised exception. Neither of the last two is ever reported as a pass. Every report still
   ends with its counts.
3. **Fixed skill order becomes a control loop.** The eleven-step path and the entry states are
   replaced by the responsibilities in `SKILL.md §2. The control loop`; where a project starts
   is decided by what it lacks (its first unmet acceptance), not by a label.
4. **Every stage is a command becomes every stage is a procedure.** A script is one kind of
   reproducible procedure; an inspection, rehearsal, demonstration, installation or client
   acceptance are others. Work nobody performed stays pending.
5. **"It is never finished" becomes closure with handover.** A finite project closes when its
   delivery is accepted, obligations are settled and materials are archived; anything that must
   keep running is handed to a named operator with review triggers. The owner's broader goal is
   not abandoned, and no route is declared impossible: a blocked route still gets another route.
6. **Agent-specific failure knowledge stays.** No standard covers the ways agents fail (tests
   that cannot fail, green pipelines that check nothing, accepted commands that never happened);
   those rules move into the guidance where the failure happens, as performable instructions.
7. **A citation never replaces an instruction.** Where an established method is named, the
   guidance still says what to do, so an agent offline can follow it.

## Target outline

The destinations below. Step 2 writes these files; `scripts/inventory_map.py --destinations`
then checks that every `file §Heading` in this map exists.

- `conductor/SKILL.md`: How to use this · 1. Classify the project · 2. The control loop ·
  3. Work records · 4. Procedures and evidence · 5. Readiness, blocking and resumption ·
  6. Gates: verification and validation · 7. Changes · 8. Authority, budget and confidentiality ·
  9. Closure and handover · 10. Reporting · Guidance to load
- `conductor/guidance/planning.md`: Deliverables and work breakdown · Work packages and acceptance
  criteria · Milestones as usable slices · Dependencies and the schedule · Critical path and
  resources · Flow: boards and Kanban · Responsibilities · Risks, assumptions, issues and
  dependencies · Change control · Rolling-wave planning and exploration · Resources and their
  sources · Estimates and arithmetic · Work records in the project's tool
- `conductor/guidance/product.md`: Intake: what only the owner knows · Starting from nothing or a
  single word · What it takes · Objective, outcomes and measures · Alternative routes · Areas and
  owners · Journeys and threads · Experience design · Requests, however they are worded ·
  Releasing to people · Hearing back
- `conductor/guidance/decisions.md`: Which decisions need evidence · Options · Criteria before
  scores · Evidence · Redo every number · A way out and a reopening condition · Recording and
  superseding decisions · Asking the owner
- `conductor/guidance/quality.md`: Write the bar first · Walk every area · Fix in order of cost to
  the person · Scope by the job · Every platform and environment, for real · Failures caused on
  purpose · Craft standard · Budgets as checks · Complexity budget · Operable · Reviewing work
- `conductor/guidance/software.md`: Setup that runs from cold · Tests that do not need services ·
  Pipelines that can fail · Automations that report their own failure · Architecture from what
  runs · Scoping a vague issue · Fixing a bug, failing test first · Tests that can fail ·
  Reviewing an agent's change · Security of agent-written code · Error paths · Data migrations ·
  Dependencies · Documentation that matches the code · Translations · Complete changes, nothing
  detached · Delivery: review, CI, deploy, rollback · Standards to apply
- `conductor/guidance/physical.md`: Specification and interfaces · Procurement, receipt and
  inspection · Parts, suppliers and lead times · Assembly, test jigs and calibration ·
  Installation, commissioning and acceptance · Commands and observed outcomes · Safety states and
  irreversible actions · Access to devices · Certification · Packaging, shipping, repairs and
  recalls · Hybrid versions and compatibility · Simulation and what it can establish
- `conductor/guidance/service.md`: Brief and acceptance · Rehearsals and reviews · Observed
  delivery · Closure and archive
- `conductor/guidance/operations.md`: Handover to operations · Periodic review · Incidents: restore
  first · After an incident · Backups and restore · Upkeep
- `conductor/guidance/design.md`: What design covers · People and their situation · Flows, states
  and words · Threads to the architecture · Every operator · One system of look and behaviour ·
  Accessible and inclusive · Taste and evidence · Testing with people · Seeing the design
- `conductor/guidance/autonomy.md`: Choosing the agent and harness · What a harness must do ·
  Building a missing tool · Briefing: ask once · Choices on the owner's behalf · Sandbox,
  checkpoints and stop · Budget · Context and state · Routing work to agents · Several agents ·
  Standing rules for the project
- `conductor/guidance/confidentiality.md`: Classes and where they may go · Every channel that can
  carry the work out · Agents and models · Working offline · Using the internet without revealing
  the work · Stripping what identifies the project · Proving it · When something has leaked
- `conductor/templates/adr.md` (MADR) and `conductor/templates/handover.md`

`quality.md`, `design.md` and `confidentiality.md` are three more guidance files than the plan's
list. The production bar applies to physical and service work as well as software, so it does not
belong in `software.md`; design and confidentiality each have enough substance to load on their
own, and only projects that need them load them.

## Summary

- **1,825 items** read from the baseline: 26 skills paragraph by paragraph (including the author
  template), `workflow.json`, `harness/AGENTS.md`, every finding `check_trace.py` can raise, every
  property `conformance.py` checks, the ledger example, 146 planted defects, and the 18 owner
  requests recorded in `QUALITY.md`. Every one appears in exactly one row below.
- **92 removed.** 75 carry no instruction: headings ("Key Files & Folders"), phase labels
  ("Explore & Plan") and connective sentences ("The failures are the same…"). 17 are the author
  template for the standalone-skill format the conductor retires; its three lasting rules are
  kept. No rule, failure case, planted defect or owner request is removed.
- **Replaced mechanisms** are marked **Replaced** in their rows: the ledger and trace check, the
  trailers, the fixed path and its entry states, the skill router, the `compact/` short forms,
  and a self-built harness as the default. The behaviour each protected is kept.
- **Changed behaviour**, from the finalisation proposal, is marked **Changed** or **qualified**:
  finite projects close with a handover instead of an endless loop; a bar with open failures is a
  completed assessment, not a release claim; a stock harness comes before a built one.

## Headings with no row

Some headings in the outline have no row pointing at them: in `planning.md` the work breakdown,
work packages, dependencies and schedule, critical path and resources, boards and Kanban, RAID,
change control and work records; all of `service.md`; and in `physical.md` procurement, receipt
and inspection. They are new content from the finalisation proposal (its method table and its
software, physical, service and hybrid delivery sections), not moved from the old library, so
nothing in the inventory maps to them. Step 2 writes them from the proposal and its sources.

## Rows common to every skill

| IDs | Where it lands | How |
|---|---|---|
| act-on-the-physical-world.role, automate-a-workflow.role, change-with-a-reason.role, choose-with-evidence.role, design-the-experience.role, fix-a-bug-test-first.role, handle-an-incident.role, isolate-tests-from-services.role, keep-it-confidential.role, keep-it-on-course.role, map-the-architecture.role, prove-the-docs.role, qa-an-agents-tests.role, release-to-people.role, repair-a-green-pipeline.role, repair-setup-script.role, review-an-agent-pr.role, run-autonomously.role, run-the-error-paths.role, scope-a-vague-issue.role, security-review-agent-code.role, start-from-an-idea.role, take-to-production.role, translate-the-docs.role, update-dependencies.role, verify-a-migration.role, template-master-prompt.role | conductor/SKILL.md §How to use this | The paragraph repeated in all 26 skills (harness-agnostic; no hosted service assumed; use the project's own equivalent, local or offline; send nothing the confidentiality rules forbid) is stated once. The role each skill named (founding engineer, reviewer, operator…) becomes the responsibility being exercised in the control loop. |

## run-autonomously

| IDs | Where it lands | How |
|---|---|---|
| run-autonomously.O1, run-autonomously.O8 | conductor/SKILL.md §6. Gates: verification and validation | Nothing is done on the agent's say-so; completion is evidence plus an accountable verifier. |
| run-autonomously.O2 | conductor/guidance/autonomy.md §Choosing the agent and harness; conductor/guidance/autonomy.md §What a harness must do | **Replaced**: an existing harness that meets the requirements is chosen first, on evidence; building one is the last route. The conformance test stays available as the check for a built harness (its location is a step 4 decision). |
| run-autonomously.O3 | conductor/guidance/autonomy.md §Building a missing tool | Kept. |
| run-autonomously.O4 | conductor/guidance/autonomy.md §Briefing: ask once | Kept. |
| run-autonomously.O5 | conductor/guidance/autonomy.md §Choices on the owner's behalf | Kept. |
| run-autonomously.O6 | conductor/guidance/autonomy.md §Context and state | Kept. |
| run-autonomously.O7 | conductor/guidance/autonomy.md §Sandbox, checkpoints and stop | Kept. |
| run-autonomously.O9 | conductor/guidance/autonomy.md §Choosing the agent and harness; conductor/guidance/confidentiality.md §Working offline | Kept: offline, online or mixed, unattended, supervised or by hand, as settings. |
| run-autonomously.O10 | conductor/SKILL.md §2. The control loop | **Replaced**: the fixed order of skills becomes the control loop; guidance loads by what the project needs. |
| run-autonomously.C1 | conductor/guidance/product.md §Intake: what only the owner knows | The project in the owner's own words, kept word for word. |
| run-autonomously.C2, run-autonomously.E1 | conductor/guidance/autonomy.md §Choosing the agent and harness | Take stock by trying: can it read, write, run, reach a network, reach the person. |
| run-autonomously.C3, run-autonomously.C15 | conductor/guidance/autonomy.md §What a harness must do | Why a model alone is not an agent; the step log. |
| run-autonomously.C4, run-autonomously.C5, run-autonomously.R21-R26, run-autonomously.G1 | conductor/guidance/autonomy.md §Context and state | The conversation is not the memory; the repository and the work records are. Fresh, small context; look up, do not remember. |
| run-autonomously.C6, run-autonomously.G2 | conductor/guidance/autonomy.md §Briefing: ask once | Ask once, early, completely; then do not wait. |
| run-autonomously.C7, run-autonomously.G3 | conductor/guidance/autonomy.md §Sandbox, checkpoints and stop | Safety from the setup. |
| run-autonomously.C8, run-autonomously.G4 | conductor/SKILL.md §6. Gates: verification and validation | "Done" means evidence passed, checked by someone other than the author. |
| run-autonomously.C9, run-autonomously.G6 | conductor/guidance/autonomy.md §Choosing the agent and harness | The way of working is a setting. |
| run-autonomously.C10 | removed | Heading only ("Key Files & Folders"); it carries no instruction. |
| run-autonomously.C11 | conductor/guidance/autonomy.md §Briefing: ask once | The briefing is recorded in the project's records, wherever it keeps them. |
| run-autonomously.C12 | conductor/SKILL.md §5. Readiness, blocking and resumption; conductor/guidance/autonomy.md §Context and state | A short state note stays, as a view for resumption; the authoritative work records are in the project's tool. |
| run-autonomously.C13 | conductor/guidance/autonomy.md §Choices on the owner's behalf | Kept: each choice with its reason, how to undo it, and a place for the owner's override. |
| run-autonomously.C14 | conductor/SKILL.md §3. Work records; conductor/guidance/decisions.md §Recording and superseding decisions | **Replaced**: the ledger by the project's own records and ADRs. |
| run-autonomously.R1-R9, run-autonomously.E2, run-autonomously.D1 | conductor/guidance/autonomy.md §What a harness must do | The harness specification (loop, fresh context, structured actions, boundaries, checkpoints, log, connectivity and supervision as settings) becomes the requirements any harness must meet, stock or built. `compact/` short forms are replaced by guidance files small enough to load one at a time. |
| run-autonomously.R10, run-autonomously.G5, run-autonomously.D2 | conductor/guidance/autonomy.md §Building a missing tool | Discover what exists first; build what is missing with its own test. |
| run-autonomously.R11-R14, run-autonomously.R16, run-autonomously.R18, run-autonomously.R19, run-autonomously.E3, run-autonomously.D3 | conductor/guidance/autonomy.md §Briefing: ask once | Kept, item by item. |
| run-autonomously.R15 | conductor/SKILL.md §8. Authority, budget and confidentiality; conductor/guidance/autonomy.md §Briefing: ask once | Standing limits for anything that leaves the sandbox: money, publishing, physical actions, incident actions. Outside them, another route. |
| run-autonomously.R17 | conductor/guidance/confidentiality.md §Classes and where they may go | Kept. |
| run-autonomously.R20, run-autonomously.D4 | conductor/guidance/autonomy.md §Choices on the owner's behalf | Look it up, test it, choose the most reversible, record it, apply overrides at once. |
| run-autonomously.R27-R30, run-autonomously.R32, run-autonomously.E4 | conductor/guidance/autonomy.md §Sandbox, checkpoints and stop | Kept. |
| run-autonomously.R31 | conductor/guidance/autonomy.md §Budget | Kept: counted, slowed at 80%, a pause that keeps the next step recorded, routes to continue. |
| run-autonomously.R33-R36, run-autonomously.R38 | conductor/SKILL.md §6. Gates: verification and validation | Gates for every change, every milestone, the product; a failed gate means another attempt or route, never a lower gate. The trace check in R34 is **replaced** by review against the work record. |
| run-autonomously.R37 | conductor/guidance/autonomy.md §Routing work to agents | **Replaced**: qualification on a small held-back task of the project's own kind; the library's fixtures are optional samples, not the gate. |
| run-autonomously.R39, run-autonomously.E6 | conductor/SKILL.md §2. The control loop | The smallest loop that finishes things: next ready task, change, gates, record, next. `Serves:`/`Verified:` **replaced** by the link to the work item and its evidence. |
| run-autonomously.R40 | conductor/guidance/autonomy.md §Several agents | Kept. |
| run-autonomously.R41 | conductor/guidance/planning.md §Rolling-wave planning and exploration | Unknowns as questions, the cheapest deciding experiment first, prior work searched first. |
| run-autonomously.R42 | conductor/guidance/autonomy.md §Choosing the agent and harness; conductor/guidance/confidentiality.md §Working offline | Kept. "Every stage is a command" **replaced** by every stage a reproducible procedure (SKILL.md §4). |
| run-autonomously.R43, run-autonomously.D5, run-autonomously.D6, run-autonomously.E8 | conductor/SKILL.md §10. Reporting | Report what passed its gates and what did not yet, with counts. The verdict rows become the checks in each autonomy section. |
| run-autonomously.E5 | conductor/SKILL.md §2. The control loop | **Replaced**: "found the project, then design" becomes the loop's first responsibilities. |
| run-autonomously.E7 | conductor/guidance/operations.md §Periodic review | Each review includes the run: budget spent, choices made and overridden, failed gates. |

## choose-with-evidence

| IDs | Where it lands | How |
|---|---|---|
| choose-with-evidence.O1-O8, choose-with-evidence.E1 | conductor/guidance/decisions.md §Which decisions need evidence | The purpose and the frame: real options, criteria from the goal, evidence in proportion, numbers redone, a way out, a reopening condition. |
| choose-with-evidence.C1, choose-with-evidence.R1 | conductor/guidance/decisions.md §Which decisions need evidence | State the question as the job; a named product becomes one option. A choice that serves no objective, measure or constraint is not needed. |
| choose-with-evidence.C2-C4, choose-with-evidence.C6, choose-with-evidence.R15-R25, choose-with-evidence.E3, choose-with-evidence.D8 | conductor/guidance/decisions.md §Options | Doing nothing, what exists, building, buying, combining; second sources for parts; no free pass; nothing excluded except by evidence; a failing hard limit becomes the problem to route around. |
| choose-with-evidence.C5, choose-with-evidence.R11-R14, choose-with-evidence.G2, choose-with-evidence.E2, choose-with-evidence.D7 | conductor/guidance/decisions.md §Criteria before scores | Criteria and weights from named sources, hard limits as pass/fail, recorded before any candidate is scored. |
| choose-with-evidence.C7, choose-with-evidence.C9, choose-with-evidence.R26-R35, choose-with-evidence.G3, choose-with-evidence.D9, choose-with-evidence.D11 | conductor/guidance/decisions.md §Evidence | Primary sources and own measurement shaped like the use; a vendor claim is a claim; kinds of evidence, at least two backings with one verified, two kinds for a costly-to-reverse decision. |
| choose-with-evidence.C8, choose-with-evidence.R36-R39, choose-with-evidence.E4, choose-with-evidence.D2, choose-with-evidence.D10, choose-with-evidence.D12 | conductor/guidance/decisions.md §Redo every number | Recompute with units at today's, the target and ten times the target size; the dominant term; the flipping assumption. |
| choose-with-evidence.C10, choose-with-evidence.R40-R44 | conductor/guidance/decisions.md §Options | One, a portfolio, a sequence with its switch condition, or a timed experiment. |
| choose-with-evidence.C11, choose-with-evidence.R45-R50, choose-with-evidence.G4, choose-with-evidence.G6, choose-with-evidence.E5, choose-with-evidence.D13, choose-with-evidence.D14 | conductor/guidance/decisions.md §A way out and a reopening condition | Seam, owned identifiers and data format, controlled URLs, an export tested once, the exit written, the reopening condition. |
| choose-with-evidence.C12, choose-with-evidence.R51-R56, choose-with-evidence.G5, choose-with-evidence.E6, choose-with-evidence.D4, choose-with-evidence.D15 | conductor/guidance/decisions.md §Asking the owner | One message with the comparison, the recommendation and its cost, the runner-up, and what no would cost; then stop asking. Delegated choices within standing limits are made and recorded. |
| choose-with-evidence.C13 | removed | Heading only. |
| choose-with-evidence.C14-C16 | conductor/guidance/decisions.md §Recording and superseding decisions | **Replaced**: read the project's objective, measures, constraints and earlier ADRs, not `PROJECT.md` and `decisions/`. |
| choose-with-evidence.C17-C19 | conductor/guidance/decisions.md §Evidence | Real usage numbers, primary sources, and where the seam goes. |
| choose-with-evidence.R2-R10, choose-with-evidence.G1 | conductor/guidance/decisions.md §Which decisions need evidence | Stakes first; the signs of a costly-to-reverse decision; effort matched to the stakes. "One-way/two-way door" wording kept as a plain explanation, not as a required field. |
| choose-with-evidence.R57-R61, choose-with-evidence.E7, choose-with-evidence.D3 | conductor/guidance/decisions.md §Recording and superseding decisions | **Replaced**: an ADR in MADR form (`templates/adr.md`), with status, the options, the evidence by kind, the decision, the exit and the reopening condition; a superseded ADR names its successor. |
| choose-with-evidence.R62 | conductor/guidance/decisions.md §Recording and superseding decisions | **Replaced**: the trace check's rules (options counted, backings counted and verified, exit and approval for a costly decision) become the ADR review checklist, applied by the reviewer. |
| choose-with-evidence.R63, choose-with-evidence.D5, choose-with-evidence.D6, choose-with-evidence.D16, choose-with-evidence.D17 | conductor/SKILL.md §10. Reporting | Per-criterion results as verified / failed / not verified; counts at the end. D6 "tied to ledger IDs" **replaced** by tied to the objective or requirement it serves. |
| choose-with-evidence.D1 | conductor/guidance/decisions.md §Criteria before scores | The comparison table, each cell with its evidence and source. |

## change-with-a-reason

| IDs | Where it lands | How |
|---|---|---|
| change-with-a-reason.O1-O7, change-with-a-reason.C10, change-with-a-reason.G2-G5 | conductor/SKILL.md §7. Changes | Every change traces to an objective, requirement or accepted decision; measured before and after; whole through every layer; removes what it replaces; recorded with its reason and verification. |
| change-with-a-reason.O8, change-with-a-reason.R9, change-with-a-reason.R12, change-with-a-reason.R40-R44, change-with-a-reason.G6 | conductor/guidance/product.md §Requests, however they are worded | Nothing asked for ends as a bare no: changed; already meets its target (with the number, and the improvement that matters instead); the owner's call (a proposed new measure); or redirected. |
| change-with-a-reason.C1, change-with-a-reason.C2, change-with-a-reason.R1-R5, change-with-a-reason.R7, change-with-a-reason.R8, change-with-a-reason.G1, change-with-a-reason.E1, change-with-a-reason.E2 | conductor/guidance/product.md §Requests, however they are worded | Keep the request word for word, split it into claims, translate each into its measurable meanings ("slow", "scalable", "modern", "prettier", "AI"), map each to an objective or requirement. |
| change-with-a-reason.C3-C5, change-with-a-reason.R14 | conductor/guidance/product.md §Requests, however they are worded | Failures: optimising what is easy, building the buzzword; find the cause (profile, trace, weigh, meter) before choosing the change. |
| change-with-a-reason.C6, change-with-a-reason.R15-R18 | conductor/SKILL.md §7. Changes; conductor/guidance/decisions.md §Recording and superseding decisions | Read the accepted decisions a change touches; route around one or reopen it with new evidence and supersede it first. Quiet contradiction is drift. |
| change-with-a-reason.C7, change-with-a-reason.C8, change-with-a-reason.R22-R33, change-with-a-reason.D3 | conductor/guidance/software.md §Complete changes, nothing detached | Every layer in the same change; everything added reached from an entry point; everything replaced removed; references searched; the detached-code checklist (module reached, key read, dependency imported, one source per fact, flags with owner and removal date, dead-code tools clean). The non-software form (every document, drawing, procedure and record the change touches) goes in SKILL.md §7. |
| change-with-a-reason.C9, change-with-a-reason.R35-R38, change-with-a-reason.E5, change-with-a-reason.D2 | conductor/SKILL.md §3. Work records; conductor/SKILL.md §7. Changes | **Replaced**: `Serves:`/`Verified:` trailers by a link from each change to its work item and its evidence, in the project's tool; a decision record (ADR) before or with the change that needs one. |
| change-with-a-reason.C11, change-with-a-reason.C12 | removed | Headings only. |
| change-with-a-reason.C13, change-with-a-reason.C14, change-with-a-reason.C15 | conductor/guidance/product.md §Objective, outcomes and measures | **Replaced**: the project's objective, measures and ADRs; with none, write the smallest: the objective and the measure this change moves. |
| change-with-a-reason.C16 | conductor/guidance/product.md §Objective, outcomes and measures | Each measure names how it is taken. |
| change-with-a-reason.C17, change-with-a-reason.C18 | conductor/guidance/software.md §Architecture from what runs | Paths found by what runs, with their history and tests. |
| change-with-a-reason.R10, change-with-a-reason.E3 | conductor/guidance/product.md §Requests, however they are worded | Show the owner the current value, the target and what it means, per claim, before changing anything. |
| change-with-a-reason.R11, change-with-a-reason.R13 | conductor/SKILL.md §7. Changes | Measure before, the way the measure says; do not change on a guess. |
| change-with-a-reason.R19-R21, change-with-a-reason.E4 | conductor/SKILL.md §7. Changes; conductor/guidance/decisions.md §Which decisions need evidence | Evidence sized to the stakes; a costly-to-reverse change needs its decision first. |
| change-with-a-reason.R34, change-with-a-reason.E6 | conductor/SKILL.md §6. Gates: verification and validation | Measure again the same way; the change's test seen to fail without it; walk the journeys it touches. |
| change-with-a-reason.R39 | conductor/guidance/quality.md §Reviewing work | **Replaced**: the trace check by the reviewer checking the change against its work item and evidence. |
| change-with-a-reason.R45, change-with-a-reason.D4, change-with-a-reason.D5, change-with-a-reason.E7 | conductor/SKILL.md §10. Reporting | Counts at the end; one row per meaning. |
| change-with-a-reason.R6 | conductor/guidance/design.md §Taste and evidence | "Prettier" as task success, time and errors on a journey; taste is the owner's call between rendered options. |
| change-with-a-reason.D1 | conductor/guidance/product.md §Requests, however they are worded | The translation table. |

## keep-it-on-course

| IDs | Where it lands | How |
|---|---|---|
| keep-it-on-course.O1 | conductor/guidance/operations.md §Periodic review; conductor/SKILL.md §9. Closure and handover | **Replaced in part**: "a project is never finished" becomes: a finite project closes on accepted delivery; whatever keeps running is handed to a named operator, and the review runs on that operator's cadence (weekly in the first month, monthly after, more often while a measure is off target). The review compares with sources, not the last report. |
| keep-it-on-course.O2-O6, keep-it-on-course.E1, keep-it-on-course.E9, keep-it-on-course.D1-D5 | conductor/guidance/operations.md §Periodic review | The review's outputs: every row measured this run, the next improvements ranked, the course, the records updated. |
| keep-it-on-course.C1 | conductor/guidance/operations.md §Periodic review | With no earlier review, review against the objective and measures alone, and say so. |
| keep-it-on-course.C2-C4, keep-it-on-course.R1, keep-it-on-course.G1, keep-it-on-course.E2 | conductor/guidance/operations.md §Periodic review | Take every measure again from its source; never carry a number forward. |
| keep-it-on-course.C5, keep-it-on-course.R3, keep-it-on-course.G5 | conductor/guidance/decisions.md §A way out and a reopening condition | Evaluate every accepted decision's reopening condition each review; a condition that could never fire is itself a finding. |
| keep-it-on-course.C6, keep-it-on-course.C7, keep-it-on-course.R4-R7, keep-it-on-course.G4, keep-it-on-course.E4 | conductor/guidance/operations.md §Periodic review | Find what nothing serves (superseded work, unused features, jobs, accounts) through the records, the project's own tools and usage; remove it as a change, or record its reason. |
| keep-it-on-course.C8, keep-it-on-course.R8, keep-it-on-course.E5 | conductor/guidance/planning.md §Resources and their sources; conductor/guidance/operations.md §Periodic review | Spend against budget per line, runway, changed prices and sources, routes around them. Money is a constraint to route around. |
| keep-it-on-course.C9, keep-it-on-course.R10, keep-it-on-course.G6 | conductor/guidance/operations.md §Periodic review | Run every procedure both ways: the person's documented path from clean, and the agent's or CI's path; a stage only one can do is broken. Restore and roll back on schedule. |
| keep-it-on-course.C10 | conductor/guidance/operations.md §Backups and restore | A backup nobody has restored is not a backup. |
| keep-it-on-course.C11, keep-it-on-course.R2, keep-it-on-course.G2, keep-it-on-course.E3 | conductor/guidance/product.md §Alternative routes | Evaluate each switch condition with today's numbers; a blocked route gets the next route to the same objective. |
| keep-it-on-course.C12, keep-it-on-course.R14, keep-it-on-course.G3 | conductor/guidance/operations.md §Periodic review | Rank improvements by the measure each moves, distance from target, people affected and cost; a held target can be raised with the owner. Kept for ongoing operations; a finite project does not acquire this loop. |
| keep-it-on-course.C13, keep-it-on-course.C14 | removed | Headings only. |
| keep-it-on-course.C15, keep-it-on-course.C16 | conductor/guidance/operations.md §Periodic review | **Replaced**: the project's objective, measures, alternative routes, resources, operating responsibilities, milestones and ADRs. |
| keep-it-on-course.C17-C20 | conductor/guidance/operations.md §Periodic review | Sources to read: each measure's source, the procedures and who runs them, everything that costs something every month, incidents and earlier reviews. |
| keep-it-on-course.R9, keep-it-on-course.E6 | conductor/guidance/autonomy.md §Routing work to agents; conductor/guidance/confidentiality.md §Proving it | Re-qualify an agent whose model, settings or harness changed; reconcile an egress-logged session with the channel map. |
| keep-it-on-course.R11, keep-it-on-course.E7 | conductor/guidance/operations.md §Upkeep | Advisories, end-of-life notices, changes in law or platform rules, and new options. |
| keep-it-on-course.R12 | conductor/guidance/autonomy.md §Choices on the owner's behalf | Show the owner the choices made since the last review; apply the overrides. |
| keep-it-on-course.R13 | conductor/guidance/product.md §Hearing back | Map every message, review and incident to a measure or journey; people new to it walk the critical journeys unaided at each milestone; an unmapped request becomes a proposal to the owner. |
| keep-it-on-course.R15-R19, keep-it-on-course.E8 | conductor/guidance/operations.md §Periodic review | The course: continue, adjust, re-route, or grow (a new objective started as a new project). |
| keep-it-on-course.R20 | conductor/guidance/operations.md §Periodic review | The owner decides. A pause keeps security updates, backups and people's data running, with what restarts it written down. |
| keep-it-on-course.R21 | conductor/SKILL.md §9. Closure and handover | Anyone could pick it up from the records alone; credentials held by the owner; a proper handover (tell the people, transfer access, rotate keys, one review walked with the new owner). |
| keep-it-on-course.R22 | conductor/SKILL.md §3. Work records | **Replaced**: the review is recorded in the project's records; trailers replaced by links. |
| keep-it-on-course.R23, keep-it-on-course.D6 | conductor/SKILL.md §10. Reporting | Counts at the end. |

## take-to-production

| IDs | Where it lands | How |
|---|---|---|
| take-to-production.O1-O6 | conductor/guidance/quality.md §Write the bar first | Production quality as four checked properties: the one job on every platform its people use; nothing lost, corrupted or exposed; finished to use; nothing it does not need. Applies to physical and service outputs as well as software. |
| take-to-production.C1 | conductor/guidance/quality.md §Write the bar first | What the owner says it is for; if absent, derived from the project and said how. |
| take-to-production.C2, take-to-production.C3, take-to-production.G1 | conductor/guidance/quality.md §Write the bar first | Production is what a person experiences on their worst day, not the repository's furniture. |
| take-to-production.C4, take-to-production.C5, take-to-production.R32, take-to-production.G5 | conductor/guidance/quality.md §Every platform and environment, for real | Run every platform, device, board or environment the bar names; detect capabilities; one not run is not verified, never inferred from another. |
| take-to-production.C6, take-to-production.R33 | conductor/guidance/quality.md §Failures caused on purpose | Storage full, offline mid-operation, killed mid-write, backgrounded, permission refused, slow device, wrong clock, two instances, upgrade over old data: caused, and watched. |
| take-to-production.C7, take-to-production.R34-R41, take-to-production.G3 | conductor/guidance/quality.md §Craft standard | Every state designed; acknowledgement within 100 ms; errors that say what to do; 320 px, 44 px targets, 200% zoom; keyboard, labels, WCAG 2.2 AA contrast; one set of values, light and dark, reduced motion; nothing shifts; the non-screen form (help, exit codes, error bodies, logs, lights, sounds). |
| take-to-production.C8, take-to-production.R7, take-to-production.D4 | conductor/guidance/quality.md §Walk every area | Every area gets a row in the bar or a one-line reason it does not apply, so an omission is visibly considered. |
| take-to-production.C9, take-to-production.R43, take-to-production.G4, take-to-production.D5 | conductor/guidance/quality.md §Complexity budget | Everything added names what breaks without it; count what was removed and what was refused. |
| take-to-production.C10, take-to-production.R31, take-to-production.G2 | conductor/guidance/quality.md §Scope by the job | Whatever the core job needs to be dependable is in scope; the rest is out; dependable beats impressive. |
| take-to-production.C11, take-to-production.R22 | conductor/guidance/physical.md §Safety states and irreversible actions; conductor/guidance/physical.md §Commands and observed outcomes | Physical safety: contracted actions, operating conditions, updates that cannot brick a device. |
| take-to-production.C12 | removed | Heading only. |
| take-to-production.C13-C17 | conductor/guidance/quality.md §Write the bar first | Where the evidence is: the promises in the README or listing, what runs and is checked, what stores or moves what people care about, manifests as costs, the bad days already reported. |
| take-to-production.R1-R6, take-to-production.E5, take-to-production.D1 | conductor/guidance/quality.md §Write the bar first | The bar in the project's records: the job, who and on what (people, agents, automation; devices, networks, hardware, conditions), the critical journeys, what must never be lost, the budgets, assumptions stated. |
| take-to-production.R8-R10 | conductor/guidance/software.md §Standards to apply; conductor/guidance/software.md §Security of agent-written code | Threat model in five lines; per entry point: authorisation enforced server-side, untrusted input, secrets, supply chain, transport, abuse limits; each attack tried. ASVS named as the reference, with these concrete checks kept as the instruction. |
| take-to-production.R11 | conductor/guidance/quality.md §Walk every area | Privacy: what personal data, where it goes, who receives it, retention, deletion. |
| take-to-production.R12 | conductor/guidance/operations.md §Backups and restore; conductor/guidance/software.md §Data migrations | State and writers mapped; backups restored at least once; migrations on real-shaped copies, forwards and back. |
| take-to-production.R13 | conductor/guidance/software.md §Error paths | Every external dependency made to fail and go slow; bounded timeouts, capped safe retries, a usable degraded mode. |
| take-to-production.R14 | conductor/guidance/quality.md §Budgets as checks | Peak with margin measured; steady memory and handles over a long run; cost of one use known. |
| take-to-production.R15 | conductor/guidance/quality.md §Every platform and environment, for real | Previous version's data, other locales and scripts, slow or metered networks. |
| take-to-production.R16 | conductor/guidance/quality.md §Craft standard; conductor/guidance/design.md §Flows, states and words | Design the flows, states and words first where they never were. |
| take-to-production.R17 | conductor/guidance/design.md §Every operator | Each journey done by each operator the bar names, person, agent or automation, under the same limits enforced in one place. |
| take-to-production.R18 | conductor/guidance/quality.md §Operable; conductor/guidance/operations.md §Incidents: restore first | Health check, alerts before a person reports, diagnosable logs kept long enough, a restoring action tried before it is needed. |
| take-to-production.R19 | conductor/guidance/software.md §Delivery: review, CI, deploy, rollback | Reproducible build, merge-gating checks seen to fail, one-action staged release, a rollback tried. |
| take-to-production.R20 | conductor/guidance/software.md §Setup that runs from cold; conductor/guidance/software.md §Documentation that matches the code; conductor/guidance/software.md §Dependencies | Maintainability through those procedures and the complexity budget. |
| take-to-production.R21 | conductor/guidance/quality.md §Walk every area | Legal: licences of dependencies, fonts, images and data; required notices, terms and privacy notice. |
| take-to-production.R23-R30, take-to-production.E6, take-to-production.E7 | conductor/guidance/quality.md §Fix in order of cost to the person | Levels 1 to 7, worst first; do not polish a 6 while a 1 is open; small reviewable changes, each re-walked. |
| take-to-production.R42, take-to-production.E8 | conductor/guidance/quality.md §Budgets as checks | Budgets asserted in CI, or in the equivalent recurring check for non-software, and failing when exceeded. |
| take-to-production.R44 | conductor/guidance/quality.md §Operable | Version reportable, readable changelog, private-free diagnostics, updates that cannot strand anyone, one-action rollback, source only in the repository. |
| take-to-production.R45 | conductor/SKILL.md §6. Gates: verification and validation; conductor/guidance/software.md §Tests that can fail | Every fix's test and every check seen to fail on the defect it exists for. |
| take-to-production.R46, take-to-production.D3, take-to-production.D6, take-to-production.E9 | conductor/SKILL.md §10. Reporting; conductor/guidance/quality.md §Reviewing work | Every bar item verified, failed or not verified, from cold, with evidence; reviewed by someone other than the author. **Changed**: a completed assessment with failed or unverified items is reported as such and does not by itself support a ready-to-release claim (finalisation proposal §4). |
| take-to-production.E1-E3 | conductor/SKILL.md §1. Classify the project; conductor/guidance/software.md §Setup that runs from cold; conductor/guidance/software.md §Architecture from what runs | Establish the starting state from evidence, not the README. |
| take-to-production.E4 | conductor/SKILL.md §8. Authority, budget and confidentiality | Plan stated; wait for approval where the harness can pause and the action needs it. |
| take-to-production.D2 | conductor/guidance/software.md §Delivery: review, CI, deploy, rollback | Each fix listed with its level and evidence in the change description. |

## design-the-experience

Destination file: `conductor/guidance/design.md`, split out of `product.md` because design has
enough substance to load on its own, and only projects with something people or agents operate
need it.

| IDs | Where it lands | How |
|---|---|---|
| design-the-experience.O1-O8, design-the-experience.G1 | conductor/guidance/design.md §What design covers | The outcome and its parts; design is deciding. |
| design-the-experience.C1 | conductor/guidance/design.md §People and their situation | **Replaced**: take the product and its people from the project's objective and records; with none, write the smallest: the objective, the people, the critical journeys. |
| design-the-experience.C2-C4 | conductor/guidance/design.md §Flows, states and words | Designed by default: the flow in build order, nine fields before value, the framework's layout and the developer's words. |
| design-the-experience.C5, design-the-experience.R1, design-the-experience.G2, design-the-experience.E1 | conductor/guidance/design.md §People and their situation | Each kind of person and agent, from evidence with sources; assumptions with the cheapest check; include the new, hurried, oldest-device and assistive-technology user. |
| design-the-experience.C6, design-the-experience.R4, design-the-experience.G3, design-the-experience.E3 | conductor/guidance/design.md §Threads to the architecture | Every state has a component and data that can produce it; every promise (undo, live status, sync, offline) has the data model and interface to keep it; a gap is resolved now with a decision. **Replaced**: "journey threads in the ledger" become a table kept with the design records. |
| design-the-experience.C7, design-the-experience.R12, design-the-experience.G5, design-the-experience.E6 | conductor/guidance/design.md §Taste and evidence | Taste is the owner's, chosen between two or three directions rendered on the real product; everything measurable is measured. |
| design-the-experience.C8, design-the-experience.R5-R9, design-the-experience.G4, design-the-experience.E4 | conductor/guidance/design.md §Every operator | A person's interface and a machine interface for each action, same names, permissions and limits enforced in one place; automation level as a setting; people can see and undo what agents did; irreversible actions keep their confirmation. |
| design-the-experience.C9, design-the-experience.R13, design-the-experience.E7, design-the-experience.D5 | conductor/guidance/design.md §Testing with people | At least five people per critical journey, unaided; stand-ins labelled as simulation, never as measured; the builder is never a participant. |
| design-the-experience.C10 | conductor/guidance/physical.md §Specification and interfaces; conductor/guidance/design.md §One system of look and behaviour | Devices: controls where the thumb is, one meaning per light, reset explained on the device. |
| design-the-experience.C11 | removed | Heading only. |
| design-the-experience.C12 | conductor/guidance/design.md §Threads to the architecture | **Replaced**: the objective, measures, journeys and their threads in the project's records. |
| design-the-experience.C13-C15 | conductor/guidance/design.md §People and their situation | Every surface people or agents meet, every style source, and where people already got stuck. |
| design-the-experience.R2, design-the-experience.R3, design-the-experience.E2, design-the-experience.D2 | conductor/guidance/design.md §Flows, states and words | Shortest flow, steps counted and justified, every field used; every state including first-time; every word written as design. |
| design-the-experience.R10, design-the-experience.G6, design-the-experience.E5, design-the-experience.D3 | conductor/guidance/design.md §One system of look and behaviour | Tokens, components and patterns in code as the only source; a value elsewhere is a defect; the device, CLI and API equivalents. |
| design-the-experience.R11 | conductor/guidance/design.md §Accessible and inclusive | WCAG 2.2 AA computed not eyeballed, keyboard, labels, 44 px, reflow; translations and local formats; the device equivalents (reach, grip, force, colour-blind-safe lights, sound or feel for each light). |
| design-the-experience.R14, design-the-experience.D4 | conductor/guidance/decisions.md §Recording and superseding decisions; conductor/guidance/design.md §Taste and evidence | Design decisions recorded as ADRs; name, habits and machine interfaces are costly to reverse, a colour is not. |
| design-the-experience.R15, design-the-experience.E8 | conductor/guidance/design.md §Seeing the design | Render every surface at smallest, middle and largest size in each theme and look; measure contrast, overflow, targets, accessibility tree, response time; say which surfaces nobody has looked at. |
| design-the-experience.R16 | conductor/guidance/product.md §Requests, however they are worded | A redesign is a change with a measure before and after. |
| design-the-experience.R17, design-the-experience.D6, design-the-experience.D7, design-the-experience.E9 | conductor/SKILL.md §10. Reporting | Counts at the end; the table's rows become the design section checklists. |
| design-the-experience.D1 | conductor/guidance/design.md §What design covers | **Replaced**: `DESIGN.md` becomes the project's design record wherever it keeps records: people and evidence, principles, operators and automation levels, surfaces not yet looked at. |

## release-to-people

| IDs | Where it lands | How |
|---|---|---|
| release-to-people.O1-O7, release-to-people.G1 | conductor/guidance/product.md §Releasing to people | Reaching the people it is for is part of delivery, planned from the start. For a service or creative output this is the delivery to the client or audience (`service.md`). |
| release-to-people.C1 | conductor/guidance/product.md §Releasing to people | **Replaced**: people, reach and measures from the project's objective and records; with none, the smallest this release needs. |
| release-to-people.C2-C4 | conductor/guidance/product.md §Releasing to people | Finished and invisible. |
| release-to-people.C5, release-to-people.R2, release-to-people.G2, release-to-people.E2, release-to-people.D2 | conductor/guidance/product.md §Releasing to people | Walk every way in as a stranger from a clean device, per platform, to the first journey done; a failure blocks the release; then someone new, unaided, watched. |
| release-to-people.C6, release-to-people.R4, release-to-people.G3, release-to-people.E5, release-to-people.D4 | conductor/guidance/software.md §Delivery: review, CI, deploy, rollback; conductor/guidance/physical.md §Packaging, shipping, repairs and recalls | Staged rollout that pauses itself at a preset failure threshold; one-action rollback tried; for devices, small batches and updates that cannot brick. |
| release-to-people.C7, release-to-people.R5, release-to-people.G4, release-to-people.E6 | conductor/guidance/product.md §Releasing to people | Channels from evidence of where people gather, several at once each with its measure, in their words. Announcements, prices and messages are actions outside the sandbox: within standing limits or with the owner's yes. |
| release-to-people.C8, release-to-people.R3, release-to-people.E3, release-to-people.D3 | conductor/guidance/product.md §Releasing to people | Everything that is not code true before release day: listings, pictures, prices and a real small payment and refund, terms and privacy notice checked against the code and a network log, licences and certifications in hand, each with an owner and a check. |
| release-to-people.C9, release-to-people.R7, release-to-people.G5, release-to-people.E4, release-to-people.D5 | conductor/guidance/product.md §Hearing back | A findable help route answered within a stated time, a person behind any agent; every message mapped; a question asked twice becomes a change. |
| release-to-people.C10, release-to-people.R8, release-to-people.G6, release-to-people.E7 | conductor/guidance/product.md §Alternative routes | Measure after the planned period; a quiet channel switches to the next route; a quiet launch is evidence about a channel, not about the idea. |
| release-to-people.C11, release-to-people.R9 | conductor/guidance/physical.md §Packaging, shipping, repairs and recalls | Packaging that survives shipping; first power-on by someone new with only the box; spares and consumables; returns and repair; a way to reach every unit for a recall or update; marks and declarations; customs and shipping rules. |
| release-to-people.C12 | removed | Heading only. |
| release-to-people.C13-C17 | conductor/guidance/product.md §Releasing to people | Where the evidence is: the records, every place people meet the product first, the release pipeline, legal texts against behaviour, the help route. |
| release-to-people.R1, release-to-people.E1, release-to-people.D1 | conductor/guidance/product.md §Releasing to people | The release plan: people, measures (find, start, finish first journey, return), channels, dates, and the next route per channel; kept in the project's records. |
| release-to-people.R6 | conductor/guidance/confidentiality.md §Classes and where they may go | A private project is released privately, to the people its classes allow. |
| release-to-people.R10, release-to-people.D6, release-to-people.D7, release-to-people.E8 | conductor/SKILL.md §10. Reporting | Counts at the end; the table's rows are the release checklist. |

## handle-an-incident

| IDs | Where it lands | How |
|---|---|---|
| handle-an-incident.O1-O5, handle-an-incident.G1, handle-an-incident.C2, handle-an-incident.C4 | conductor/guidance/operations.md §Incidents: restore first | The order: stop harm, restore by a tried action, tell people, keep evidence; understand afterwards, on a copy. Also an interrupt in SKILL.md §2. |
| handle-an-incident.O6-O9 | conductor/guidance/operations.md §After an incident | Cause proved by a failing test, fixed through the normal gates, the class closed, recorded. |
| handle-an-incident.C1, handle-an-incident.E1, handle-an-incident.R1, handle-an-incident.D1 | conductor/guidance/operations.md §Incidents: restore first | Start from alerts, logs and the help route; one person or agent in charge; a timeline with times from the first minute. |
| handle-an-incident.C3 | removed | Connective sentence introducing the failures; no instruction of its own. |
| handle-an-incident.C5, handle-an-incident.R2, handle-an-incident.G2, handle-an-incident.E2 | conductor/guidance/operations.md §Incidents: restore first | Stop harm to data first: pause, block, stop unsafe retries, safe state; snapshot before any repair. |
| handle-an-incident.C6, handle-an-incident.R6 | conductor/guidance/operations.md §Incidents: restore first; conductor/guidance/autonomy.md §Briefing: ask once | Agents on duty act only within restoring actions named in advance; never silence an alert, disable a check, delete data or retry an unsafe action; beyond that, the safest action and the person. |
| handle-an-incident.C7, handle-an-incident.R4, handle-an-incident.G4, handle-an-incident.E4, handle-an-incident.D3 | conductor/guidance/operations.md §Incidents: restore first | Tell people early, where they look, with the next update time, and keep it; within publishing limits. |
| handle-an-incident.C8, handle-an-incident.R5, handle-an-incident.E5, handle-an-incident.D4 | conductor/guidance/operations.md §Incidents: restore first | Copy logs, traces, data state and configuration from the window before rotation or restore; record which change was live. |
| handle-an-incident.C9, handle-an-incident.R8, handle-an-incident.E7, handle-an-incident.D6 | conductor/guidance/operations.md §After an incident | The fix passes the normal gates; only an already-tried restoring action may skip them. |
| handle-an-incident.C10, handle-an-incident.R7, handle-an-incident.G5, handle-an-incident.E6, handle-an-incident.D5 | conductor/guidance/operations.md §After an incident | Reproduce on a copy with a failing test; ask why down to the system; name the check that should have caught it. Blameless: the system changes, never "be more careful". |
| handle-an-incident.C11, handle-an-incident.R9, handle-an-incident.G6, handle-an-incident.E8, handle-an-incident.D7 | conductor/guidance/operations.md §After an incident | Count every person, record and device affected from the data; put each right and check it. |
| handle-an-incident.C12 | removed | Heading only. |
| handle-an-incident.C13-C17 | conductor/guidance/operations.md §Incidents: restore first | Where the evidence is: alerts and logs for critical journeys, release history with rollbacks, restore procedures with their last-tried dates, the status channel, the records of limits and earlier incidents. |
| handle-an-incident.R3, handle-an-incident.G3, handle-an-incident.E3, handle-an-incident.D2 | conductor/guidance/operations.md §Incidents: restore first | The fastest tried, undoable action; journeys walked to confirm, not the graph alone; a missing restoring action is itself recorded. |
| handle-an-incident.R10, handle-an-incident.E9, handle-an-incident.D8 | conductor/guidance/operations.md §After an incident | Close the class: a test, an alert before a person reports it, a limit, an idempotency key, a tried procedure, a drill scheduled; recorded against what it protects. |
| handle-an-incident.R11, handle-an-incident.D9, handle-an-incident.D10, handle-an-incident.E10 | conductor/SKILL.md §10. Reporting | Counts at the end; the table's rows are the incident checklist, including time to detect and to restore. |

## keep-it-confidential

| IDs | Where it lands | How |
|---|---|---|
| keep-it-confidential.O1-O6, keep-it-confidential.G1 | conductor/guidance/confidentiality.md §Classes and where they may go | Confidentiality observed, not assumed: rules by class, every channel mapped, offline proved, a careful internet gate, egress reconciled. |
| keep-it-confidential.O7 | conductor/guidance/confidentiality.md §Classes and where they may go | It protects the owner's own work; within the law and every service's terms. |
| keep-it-confidential.C1 | conductor/guidance/confidentiality.md §Classes and where they may go | Default when unstated: everything, and the fact the project exists, is private until the owner says otherwise. |
| keep-it-confidential.C2, keep-it-confidential.C5, keep-it-confidential.C7, keep-it-confidential.G3 | conductor/guidance/confidentiality.md §Every channel that can carry the work out | Leaks come through tools on by default; the concrete examples are kept. |
| keep-it-confidential.C3 | removed | Connective sentence; no instruction. |
| keep-it-confidential.C4, keep-it-confidential.R19, keep-it-confidential.G2, keep-it-confidential.E4, keep-it-confidential.D3 | conductor/guidance/confidentiality.md §Working offline | Offline is proved by blocking egress and running every procedure from a clean checkout; anything reaching out fails loudly and is vendored, mirrored or cached with its hash; unproved offline is not verified. |
| keep-it-confidential.C6, keep-it-confidential.R26-R31 | conductor/guidance/confidentiality.md §Agents and models | A remote agent gets only released classes, the smallest excerpt, names and keys stripped, a provider whose terms exclude training and limit retention, every call logged. |
| keep-it-confidential.C8, keep-it-confidential.R40, keep-it-confidential.G5 | conductor/guidance/confidentiality.md §Stripping what identifies the project | Author, email and time zone set for the project; codenames out of package names, hosts and artifacts; no absolute paths in builds; document and image metadata stripped; outbound logs free of names and data. |
| keep-it-confidential.C9, keep-it-confidential.R32-R39, keep-it-confidential.G4, keep-it-confidential.G6, keep-it-confidential.E5, keep-it-confidential.D5 | conductor/guidance/confidentiality.md §Using the internet without revealing the work | One purpose, one sitting, one gate; fetch broadly and search locally; ask about the technique, never the project; agents off the open web behind a logging allow-list proxy; network identity separated where the threat model calls for it; everything fetched verified by hash and kept; residual exposure recorded as a risk the owner accepted. |
| keep-it-confidential.C10, keep-it-confidential.R24, keep-it-confidential.R25 | conductor/guidance/confidentiality.md §Working offline; conductor/SKILL.md §How to use this | A step naming a hosted service is done with the local equivalent, never skipped. **Replaced**: "the ledger and issues as files in the repository" becomes: the project's chosen offline tool for work records (SKILL.md §3). |
| keep-it-confidential.C11-C16, keep-it-confidential.R9-R18, keep-it-confidential.E2, keep-it-confidential.D2 | conductor/guidance/confidentiality.md §Every channel that can carry the work out | The channel map: every configuration that can send, walked by list (remotes, CI logs, backups and sync, agents, telemetry, registries, the product's own calls, trackers and chat, research, metadata), each closed, controlled or open by written decision, with evidence. |
| keep-it-confidential.R1-R8, keep-it-confidential.E1, keep-it-confidential.D1 | conductor/guidance/confidentiality.md §Classes and where they may go | The classes and destinations from this machine to public, written in the project's confidentiality record. |
| keep-it-confidential.R20-R23, keep-it-confidential.E3 | conductor/guidance/confidentiality.md §Agents and models; conductor/guidance/confidentiality.md §Working offline | Local model runtime with hashed weights and no remote fallback; version control on owner hardware or client-side encrypted; hashed lockfile, local mirror, installs that refuse the public index; internal names never reach a public registry. |
| keep-it-confidential.R41, keep-it-confidential.E6, keep-it-confidential.D4 | conductor/guidance/confidentiality.md §Proving it | A working session with connections and DNS logged; every destination in the channel map; repeated after every new tool, dependency, model or agent. |
| keep-it-confidential.R42 | conductor/guidance/confidentiality.md §When something has leaked | Rotate, revoke, remove, record; add the channel to the map; data that left is assumed kept. |
| keep-it-confidential.R43, keep-it-confidential.D6, keep-it-confidential.D7, keep-it-confidential.E7 | conductor/SKILL.md §10. Reporting | Every channel and procedure verified, failed or not verified; counts at the end. |

## act-on-the-physical-world

| IDs | Where it lands | How |
|---|---|---|
| act-on-the-physical-world.O1, act-on-the-physical-world.O2, act-on-the-physical-world.R1, act-on-the-physical-world.E2 | conductor/guidance/physical.md §Commands and observed outcomes | The action contract before issuing: target state, independent observation, deadline, safe state, reversibility, units. Scope: actuators, robots, instruments, building controls, and services that ship, pay, dispense, dispatch or message a person. |
| act-on-the-physical-world.C1, act-on-the-physical-world.C2, act-on-the-physical-world.C10, act-on-the-physical-world.R2, act-on-the-physical-world.R3, act-on-the-physical-world.G1 | conductor/guidance/physical.md §Commands and observed outcomes | An acknowledgement is not an outcome; confirm through something that measures the world, timestamped after the action, within a deadline; an echo of the setpoint is not evidence. Also stated in SKILL.md §4 as a general rule (an order is not receipt). |
| act-on-the-physical-world.C3 | removed | Connective sentence; no instruction. |
| act-on-the-physical-world.C4, act-on-the-physical-world.R5 | conductor/guidance/physical.md §Commands and observed outcomes; conductor/SKILL.md §5. Readiness, blocking and resumption | Absolute targets over changes; retry a non-idempotent action only after observing that the first did not happen; idempotency keys. The resumption rule in SKILL.md generalises it. |
| act-on-the-physical-world.C5, act-on-the-physical-world.R4, act-on-the-physical-world.G3 | conductor/guidance/physical.md §Safety states and irreversible actions | A safe state decided for each actuator; every failure path lands there; context-dependent safety escalated, not guessed; fail toward stopped. |
| act-on-the-physical-world.C6, act-on-the-physical-world.R13 | conductor/guidance/physical.md §Commands and observed outcomes | Units in names, keys and logs; convert once at the edge with a test value that differs between units. |
| act-on-the-physical-world.C7, act-on-the-physical-world.R7, act-on-the-physical-world.G4 | conductor/guidance/physical.md §Safety states and irreversible actions | A device-side watchdog or a duration in the command; proved by killing the controller mid-run. |
| act-on-the-physical-world.C8, act-on-the-physical-world.R8 | conductor/guidance/physical.md §Simulation and what it can establish | Default target is the simulator or dry run; reaching the real thing is explicit and announced on the first line. |
| act-on-the-physical-world.C9, act-on-the-physical-world.R10, act-on-the-physical-world.C17 | conductor/guidance/physical.md §Access to devices | Authenticated, scoped, encrypted control channels, no default passwords, rate-limited commands. |
| act-on-the-physical-world.C11 | removed | Heading only. |
| act-on-the-physical-world.C12-C16 | conductor/guidance/physical.md §Commands and observed outcomes | Where to look: every exit toward hardware or a real-world service, target configuration and defaults, retry logic, sensor reads, limits and interlocks and where each is missing. |
| act-on-the-physical-world.R6 | conductor/guidance/physical.md §Safety states and irreversible actions | Limits enforced below the agent, in code and independently in the device. |
| act-on-the-physical-world.R9, act-on-the-physical-world.G2 | conductor/guidance/physical.md §Safety states and irreversible actions; conductor/SKILL.md §8. Authority, budget and confidentiality | A person's yes to the exact action and parameters for anything irreversible; standing authorisation explicit, scoped and written. |
| act-on-the-physical-world.R11 | conductor/guidance/physical.md §Hybrid versions and compatibility | Updates verified, power-cut safe, reversible in one step. |
| act-on-the-physical-world.R12, act-on-the-physical-world.D3 | conductor/guidance/physical.md §Commands and observed outcomes | An action log from which a person can reconstruct what was done to the world. |
| act-on-the-physical-world.G5 | conductor/guidance/physical.md §Simulation and what it can establish | Smallest quantities, lowest energies, widest clearances; put the world back. |
| act-on-the-physical-world.E1 | conductor/guidance/physical.md §Commands and observed outcomes | Inventory every physical action with target, reversibility and current safeguards; no irreversible real action without confirmation, whatever the harness allows. |
| act-on-the-physical-world.E3, act-on-the-physical-world.D2 | conductor/guidance/physical.md §Simulation and what it can establish | Rehearse every action and every failure in simulation; each lands in the safe state, with a test. A simulated result establishes workflow behaviour, not a real installation or safety result. |
| act-on-the-physical-world.E4 | conductor/guidance/physical.md §Safety states and irreversible actions | Fix order, most dangerous first. |
| act-on-the-physical-world.E5 | conductor/guidance/physical.md §Installation, commissioning and acceptance | Act for real once, observed, with confirmation where required. |
| act-on-the-physical-world.D1, act-on-the-physical-world.D4 | conductor/SKILL.md §10. Reporting | Verified means an independent observation confirmed it; failed means it contradicted it or a failure path was unsafe; not verified means no independent observation was possible, and why. |

## start-from-an-idea

The largest skill. Its content splits across product, decisions, planning, autonomy and the
conductor itself, which is what the plan intended: founding a project is a set of
responsibilities, not one step.

| IDs | Where it lands | How |
|---|---|---|
| start-from-an-idea.O1-O6, start-from-an-idea.E2, start-from-an-idea.D1 | conductor/guidance/product.md §What it takes | What it takes to make the idea happen, the costly decisions made with evidence, a procedure for every stage, one thin slice end to end, and the records every later change traces to. |
| start-from-an-idea.O7, start-from-an-idea.G1 | conductor/guidance/product.md §Alternative routes; conductor/SKILL.md §1. Classify the project | No idea is declared impossible: constraints get routes, each honestly costed. An existing project has its records written from what is there, its embodied decisions recorded with the evidence they had, and the unjustifiable ones marked for revisiting. |
| start-from-an-idea.C1, start-from-an-idea.R1, start-from-an-idea.E1 | conductor/guidance/product.md §Intake: what only the owner knows | The idea word for word; one message asking only what only the owner knows (who it is for and what they do today, success, why, budget in money, time and agent use, deadlines and refusals, whether it must earn); assumptions written when the harness cannot pause. |
| start-from-an-idea.C2, start-from-an-idea.C4, start-from-an-idea.R2-R10 | conductor/guidance/product.md §What it takes; conductor/guidance/physical.md §Parts, suppliers and lead times | Need, what exists (build on, learn from, stand apart), the difference, cost to build and run (BOM, certification and tooling for physical), several funding routes and runway, reach to the first ten and hundred, what success needs (each gap becomes work, never a verdict), and the path with its first step. |
| start-from-an-idea.C3, start-from-an-idea.C15 | removed | Connective sentence and a heading; no instruction. |
| start-from-an-idea.C5, start-from-an-idea.R11, start-from-an-idea.E3 | conductor/guidance/product.md §Objective, outcomes and measures; conductor/guidance/product.md §Alternative routes | One objective as a change in the world for named people; three to five measures each with target, date and method; the critical journeys; switch conditions naming the next route. **Replaced**: G/M/J/K IDs by the project's own records. |
| start-from-an-idea.C6, start-from-an-idea.R12-R14, start-from-an-idea.R17, start-from-an-idea.G2, start-from-an-idea.E4 | conductor/guidance/decisions.md §Which decisions need evidence | Sort by cost to reverse; the list of costly-to-reverse decisions (data model and identifiers, public interface and who operates each action, language and runtime, hardware platform, data-holding vendor, licence, name, money or commitments to people), made for the target size; two-way choices behind a seam; defer what a seam can hold, with until when. |
| start-from-an-idea.C7, start-from-an-idea.R43 | conductor/guidance/planning.md §Estimates and arithmetic; conductor/guidance/decisions.md §Redo every number | Every number shown with units and inputs so another person can redo it; simulate or prototype where a calculation rests on a guess; name the sensitive assumptions; a vendor number is a claim. |
| start-from-an-idea.C8, start-from-an-idea.R19 | conductor/guidance/decisions.md §Options | The first option found is not the plan; portfolios, sequences and timed experiments; nothing ruled out except by evidence. |
| start-from-an-idea.C9, start-from-an-idea.R35, start-from-an-idea.R36, start-from-an-idea.G5, start-from-an-idea.E6 | conductor/guidance/planning.md §Milestones as usable slices | Vertical slices, not layers; a walking skeleton through every stage (built from cold, a test seen to fail, released, observed, rolled back once; for a physical product one real reading or action confirmed independently); only the folders, services and dependencies it uses; the first release to real people early. |
| start-from-an-idea.C10 | conductor/guidance/product.md §Alternative routes | The first plan is not the only plan. |
| start-from-an-idea.C11, start-from-an-idea.C18, start-from-an-idea.R22, start-from-an-idea.G6 | conductor/SKILL.md §4. Procedures and evidence; conductor/guidance/planning.md §Responsibilities | **Replaced**: "every stage a command" becomes every stage a reproducible procedure with a responsible actor and evidence (a script where the stage is software; an inspection, installation or acceptance where it is not). The operating model (who runs each stage today, who approves, the fallback) is kept; irreversible actions keep a person's yes at every level of automation; connectivity as configuration moves to `autonomy.md §Choosing the agent and harness`. |
| start-from-an-idea.C12, start-from-an-idea.R20 | conductor/guidance/product.md §Areas and owners; conductor/guidance/physical.md §Parts, suppliers and lead times; conductor/guidance/physical.md §Assembly, test jigs and calibration | Every area the product needs, each with an owner, a first deliverable and the measure it serves, or one line on why it does not apply: product, research, design, engineering, quality, security and privacy, confidentiality, operations, supply, legal, finance, distribution, support. |
| start-from-an-idea.C13 | conductor/guidance/quality.md §Complexity budget | Complexity before the need is a cost now and a migration later. |
| start-from-an-idea.C14 | conductor/SKILL.md §7. Changes | Nothing exists without a reason that leads back to the objective, backed by verified evidence. |
| start-from-an-idea.C16 | conductor/SKILL.md §1. Classify the project | Start from whatever the owner already has, including a previous agent's scaffold. |
| start-from-an-idea.C17, start-from-an-idea.R37-R41, start-from-an-idea.D2 | conductor/SKILL.md §3. Work records; conductor/guidance/decisions.md §Recording and superseding decisions | **Replaced**: `PROJECT.md` tables, `decisions/D0001` front matter, `Serves:`/`Verified:` trailers and the trace check in CI become: the objective, measures and acceptance in the project's records; ADRs; work items in the project's tool with each change linked to its item and evidence; the checks applied at review. |
| start-from-an-idea.C19, start-from-an-idea.R42 | conductor/guidance/autonomy.md §Standing rules for the project | The standing rules in the project's `AGENTS.md` or equivalent. |
| start-from-an-idea.R15 | conductor/guidance/decisions.md §Evidence | Two backings labelled by kind, at least one run, worked out or built. |
| start-from-an-idea.R16 | conductor/SKILL.md §7. Changes | Everything smaller is a change carrying its reason and verification. |
| start-from-an-idea.R18, start-from-an-idea.E5, start-from-an-idea.D4 | conductor/guidance/planning.md §Resources and their sources | Every resource's source chosen from at least two (including what the owner has, and building it), on cost now and at target size, lock-in, lead time and who must act; one message with the whole table; a budget for agent and model use, spend recorded. |
| start-from-an-idea.R21 | conductor/guidance/product.md §Journeys and threads | One table per critical journey, one row per step: what the person does, what they see, the component and interface, the data written, the evidence that proves it, the measure it moves; an empty cell is a gap. |
| start-from-an-idea.R23, start-from-an-idea.R25-R27 | conductor/guidance/autonomy.md §Routing work to agents | By what each agent may see first, then by measured ability on a held-back task of this project's kind; fit the work to the harness and context size; every stage has a fallback agent or person. |
| start-from-an-idea.R24 | conductor/guidance/confidentiality.md §Agents and models | Where each agent runs and which classes it may see. |
| start-from-an-idea.R28 | conductor/guidance/autonomy.md §Building a missing tool | A step done three times, or one whose mistakes are costly, becomes a tool in the repository with its own test. |
| start-from-an-idea.R29-R34 | conductor/SKILL.md §3. Work records | Nobody works in the dark: status from measurements; requests translated and confirmed; options and costs shown before choosing; why each part exists; what is there and who runs it. Each gap in visibility gets its mechanism in the records. |
| start-from-an-idea.R44, start-from-an-idea.D6, start-from-an-idea.D7, start-from-an-idea.E8 | conductor/SKILL.md §10. Reporting | Counts at the end; the table's rows become the founding checklist across product, decisions and planning. |
| start-from-an-idea.G3 | conductor/guidance/decisions.md §Evidence | Every reason verified. |
| start-from-an-idea.G4 | conductor/guidance/decisions.md §Asking the owner | The owner decides; the agent brings options and arithmetic. |
| start-from-an-idea.G7 | conductor/SKILL.md §9. Closure and handover | **Replaced**: "it is never finished" becomes closure on accepted delivery with anything ongoing handed to a named operator; launch is a milestone, and the owner's broader goal is not abandoned. |
| start-from-an-idea.E7 | conductor/guidance/planning.md §Milestones as usable slices; conductor/guidance/autonomy.md §Standing rules for the project | Milestones planned as slices with the first release early; the trace check **replaced** by review against work records; standing rules in place. |
| start-from-an-idea.D3 | conductor/guidance/planning.md §Milestones as usable slices; conductor/SKILL.md §4. Procedures and evidence | The walking skeleton, every stage as a procedure, and who runs it. |
| start-from-an-idea.D5 | conductor/guidance/decisions.md §A way out and a reopening condition | Deferred decisions, each with the seam that holds it open and the condition that will close it. |

## Steps shared by the narrow software skills

Twelve of the narrow skills end their Execution Flow with the same generic steps: phase labels
("Explore & Plan", "Execute & Verify", "Test & Review", "Submit"), "write the plan, and wait if
the harness can pause", "request a code review", and "open a pull request with a summary of what
was verified". Their rows below point these to one place each: the labels are removed (they
carry no instruction), the plan-and-wait rule goes to `SKILL.md §8. Authority, budget and
confidentiality`, review goes to `quality.md §Reviewing work`, and the pull request goes to
`software.md §Delivery: review, CI, deploy, rollback`.

## repair-setup-script

| IDs | Where it lands | How |
|---|---|---|
| repair-setup-script.O1, repair-setup-script.C1, repair-setup-script.D1 | conductor/guidance/software.md §Setup that runs from cold | A clean environment installs, builds and runs the tests using only the script, which then exits; defects here are paid for by every future task because harnesses snapshot setup. |
| repair-setup-script.C2 | removed | Heading only. |
| repair-setup-script.C3-C6, repair-setup-script.E2-E5 | conductor/guidance/software.md §Setup that runs from cold | Where to look and the baseline: manifests, lockfiles, the CI workflow's exact commands, every external dependency, the existing setup run and its exact failure. |
| repair-setup-script.R1-R5 | conductor/guidance/software.md §Setup that runs from cold | No long-running processes (detached with a readiness poll if needed; a sleep is not a readiness check); true exit codes (no `\|\| true`); unattended; no secrets; lightweight. |
| repair-setup-script.G1-G5 | conductor/guidance/software.md §Setup that runs from cold | Reproduce before repairing; CI is the best evidence; install from the lockfile; install and verify as separate phases; report what cannot run rather than skipping it. |
| repair-setup-script.E1, repair-setup-script.E7, repair-setup-script.E12, repair-setup-script.E15 | removed | Phase labels; no instruction. |
| repair-setup-script.E6 | conductor/SKILL.md §8. Authority, budget and confidentiality | Plan stated; wait where approval is needed and the harness can pause. |
| repair-setup-script.E8-E11 | conductor/guidance/software.md §Setup that runs from cold | Repair, run, repeat until the runner reports results (not until all pass; no editing tests here); then prove the two silent failure modes: a failed install fails the script, and nothing blocks. |
| repair-setup-script.E13, repair-setup-script.D3 | conductor/SKILL.md §4. Procedures and evidence | Evidence is the commands, their exit codes and the runner's summary line verbatim; what still cannot run is listed with the reason. |
| repair-setup-script.E14, repair-setup-script.E16 | conductor/guidance/quality.md §Reviewing work | Review by someone other than the author; feedback addressed. |
| repair-setup-script.E17 | conductor/guidance/software.md §Delivery: review, CI, deploy, rollback | The change proposed with what was verified and a link to its work item. |
| repair-setup-script.D2 | conductor/guidance/autonomy.md §Standing rules for the project | The install and test commands and required environment variables written where every agent reads them. |
| repair-setup-script.D4, repair-setup-script.D5 | conductor/SKILL.md §10. Reporting | Counts at the end. |

## isolate-tests-from-services

| IDs | Where it lands | How |
|---|---|---|
| isolate-tests-from-services.O1, isolate-tests-from-services.C1, isolate-tests-from-services.D1 | conductor/guidance/software.md §Tests that do not need services | The default suite runs from cold with no services; every test runs without a live service or is excluded by a named marker with its reason; connection errors are never "unrelated to our changes". |
| isolate-tests-from-services.C2 | removed | Heading only. |
| isolate-tests-from-services.C3-C5, isolate-tests-from-services.E2, isolate-tests-from-services.E3 | conductor/guidance/software.md §Tests that do not need services | Where to look, and the inventory from running with nothing up, including import-time connections. |
| isolate-tests-from-services.R1-R4, isolate-tests-from-services.D2, isolate-tests-from-services.D4 | conductor/guidance/software.md §Tests that do not need services | Never change what a test asserts; nothing skipped silently; the isolated run is the default; the full suite against real services stays runnable and documented. |
| isolate-tests-from-services.G1-G5, isolate-tests-from-services.D5 | conductor/guidance/software.md §Tests that do not need services | Find dependencies by running; fake at the existing seam (patching a library is a design finding); in-memory substitutes can lie; record rather than invent API responses; clock, network and randomness are the same problem. |
| isolate-tests-from-services.E1, isolate-tests-from-services.E5, isolate-tests-from-services.E11, isolate-tests-from-services.E14 | removed | Phase labels. |
| isolate-tests-from-services.E4 | conductor/SKILL.md §8. Authority, budget and confidentiality | Plan stated; wait where needed. |
| isolate-tests-from-services.E6-E10, isolate-tests-from-services.D3 | conductor/guidance/software.md §Tests that do not need services | One dependency at a time; genuine exceptions marked; isolation proved with egress blocked or dead ports; collected-test counts before and after reconciled exactly. |
| isolate-tests-from-services.E12 | conductor/SKILL.md §4. Procedures and evidence | Both counts, the reconciliation and the verbatim summary line. |
| isolate-tests-from-services.E13 | conductor/guidance/quality.md §Reviewing work | Review by someone other than the author. |
| isolate-tests-from-services.E15 | conductor/guidance/software.md §Delivery: review, CI, deploy, rollback | The change proposed with what was verified. |
| isolate-tests-from-services.D6, isolate-tests-from-services.D7 | conductor/SKILL.md §10. Reporting | One row per external service; counts at the end. |

## repair-a-green-pipeline

| IDs | Where it lands | How |
|---|---|---|
| repair-a-green-pipeline.O1, repair-a-green-pipeline.C1, repair-a-green-pipeline.R1, repair-a-green-pipeline.R2 | conductor/guidance/software.md §Pipelines that can fail | For every check, introduce the defect it exists for, one at a time on a throwaway branch reverted at once, and watch it go red. Also the general rule in SKILL.md §6 (a check nobody has seen fail is a claim). |
| repair-a-green-pipeline.C2 | removed | Connective sentence. |
| repair-a-green-pipeline.C3-C10 | conductor/guidance/software.md §Pipelines that can fail | The mechanical causes, kept as a checklist: no files matched, a pipe discarding status, `continue-on-error`/`\|\| true`/`set +e`, filters that stopped matching, silently excluded matrix legs, disabled lint rules, stale cached artifacts; absence looks like success. |
| repair-a-green-pipeline.C11 | removed | Heading only. |
| repair-a-green-pipeline.C12-C15, repair-a-green-pipeline.E2, repair-a-green-pipeline.E3 | conductor/guidance/software.md §Pipelines that can fail | Where to look, and the run history: which jobs never went red, which stopped appearing. |
| repair-a-green-pipeline.R3-R5, repair-a-green-pipeline.G1-G6, repair-a-green-pipeline.D2-D5 | conductor/guidance/software.md §Pipelines that can fail | Every step prints its coverage; swallowed exit codes removed or justified in place; no new checks while old ones are inert (missing ones listed separately); count and reconcile; never-red steps first; check a job ran, not that it passed; the setup's own failure path first; a badge is a claim; an unfailable check is said plainly. |
| repair-a-green-pipeline.E1, repair-a-green-pipeline.E5, repair-a-green-pipeline.E11, repair-a-green-pipeline.E14 | removed | Phase labels. |
| repair-a-green-pipeline.E4 | conductor/SKILL.md §8. Authority, budget and confidentiality | Plan stated; wait where needed. |
| repair-a-green-pipeline.E6-E10, repair-a-green-pipeline.D1 | conductor/guidance/software.md §Pipelines that can fail | Defect per step, survivors grouped by cause, repaired and re-broken, coverage lines added, the tree left clean and green. |
| repair-a-green-pipeline.E12 | conductor/SKILL.md §4. Procedures and evidence | The before and after table as evidence. |
| repair-a-green-pipeline.E13 | conductor/guidance/quality.md §Reviewing work | Review by someone other than the author. |
| repair-a-green-pipeline.E15 | conductor/guidance/software.md §Delivery: review, CI, deploy, rollback | The change proposed with what was verified. |
| repair-a-green-pipeline.D6, repair-a-green-pipeline.D7 | conductor/SKILL.md §10. Reporting | Verified means went red on its defect; failed means stayed green; not verified means could not be made to fail, with what was tried. |

## automate-a-workflow

| IDs | Where it lands | How |
|---|---|---|
| automate-a-workflow.O1, automate-a-workflow.C1, automate-a-workflow.C2, automate-a-workflow.G1, automate-a-workflow.G2 | conductor/guidance/software.md §Automations that report their own failure | The script's real job is a trustworthy report of whether the work happened; success without the work is the failure that matters. The non-software form (a checklist that records what was observed) is in SKILL.md §4. |
| automate-a-workflow.C3 | removed | Connective sentence. |
| automate-a-workflow.C4-C8, automate-a-workflow.R2-R5, automate-a-workflow.R8, automate-a-workflow.G3 | conductor/guidance/software.md §Automations that report their own failure | Never a check on the left of a pipe; verify each step by its effect; truncated output is deleted data; ask the system, not an old log; safe to run twice; results written as produced and resumable; the log says what it read. |
| automate-a-workflow.C9 | removed | Heading only. |
| automate-a-workflow.C10-C13, automate-a-workflow.R1, automate-a-workflow.G5, automate-a-workflow.E1, automate-a-workflow.D2 | conductor/guidance/software.md §Automations that report their own failure | Find the workflow in the history before automating it, with how often it runs and what a mistake costs; something rare and cheap may deserve a checklist instead. |
| automate-a-workflow.R6, automate-a-workflow.E3, automate-a-workflow.D3 | conductor/guidance/software.md §Automations that report their own failure | Make it fail on purpose (dependency, permission, input, interruption) and watch each failure reach the exit code and the log. |
| automate-a-workflow.R7, automate-a-workflow.G4, automate-a-workflow.E4, automate-a-workflow.D4 | conductor/guidance/software.md §Automations that report their own failure | Say what it will not do; boring and checkable over clever and total. |
| automate-a-workflow.E2, automate-a-workflow.D1 | conductor/guidance/software.md §Automations that report their own failure | The script and its one command, built to the rules above. |
| automate-a-workflow.E5, automate-a-workflow.D5, automate-a-workflow.D6 | conductor/SKILL.md §10. Reporting | Counts at the end. |

## map-the-architecture

| IDs | Where it lands | How |
|---|---|---|
| map-the-architecture.O1, map-the-architecture.C1-C3, map-the-architecture.G1, map-the-architecture.D1 | conductor/guidance/software.md §Architecture from what runs | The real structure derived from what runs, what imports what, what fails separately and what changes together; every claim with how it was established. Folder names are the claim most likely to be stale. |
| map-the-architecture.C4, map-the-architecture.C5, map-the-architecture.R4 | conductor/guidance/software.md §Architecture from what runs | The tells of a name-based description; co-change in the history names the real modules; report the surprises. |
| map-the-architecture.C6 | removed | Heading only. |
| map-the-architecture.C7-C11 | conductor/guidance/software.md §Architecture from what runs | Where to look: packaging and process definitions and CI, the resolved import graph, process/network/queue/database crossings, configuration, `git log` for co-change. |
| map-the-architecture.R1-R3, map-the-architecture.R5-R7, map-the-architecture.E1-E4, map-the-architecture.D3 | conductor/guidance/software.md §Architecture from what runs | Entry points found and one run; imports resolved; real boundaries are the ones that fail separately; provenance per claim; no diagram the code does not support; what could not be established (dynamic dispatch, reflection, plugins, configuration wiring) named. |
| map-the-architecture.G2-G4, map-the-architecture.D2 | conductor/guidance/software.md §Architecture from what runs | The coupling nobody intended; follow the data; count things. |
| map-the-architecture.G5, map-the-architecture.E5 | conductor/guidance/software.md §Architecture from what runs | A good map predicts: check it against two recent changes. The same test applies to a physical or organisational map (SKILL.md §1, where an existing project's records are written from what is there). |
| map-the-architecture.E6, map-the-architecture.D4, map-the-architecture.D5 | conductor/SKILL.md §10. Reporting | One row per claim and one for the prediction check; counts at the end. |

## scope-a-vague-issue

| IDs | Where it lands | How |
|---|---|---|
| scope-a-vague-issue.O1, scope-a-vague-issue.C1, scope-a-vague-issue.R1 | conductor/guidance/software.md §Scoping a vague issue | Turn a thin report into an exact reproduction, observed and expected behaviour, and a failing test, with no fix; guessing what "broken" means is the failure. The general form (a request is not yet a specification) is in product.md §Requests, however they are worded. |
| scope-a-vague-issue.C2 | conductor/guidance/software.md §Scoping a vague issue | The issue as given. |
| scope-a-vague-issue.C3 | removed | Heading only. |
| scope-a-vague-issue.C4-C6 | conductor/guidance/software.md §Scoping a vague issue | Where to look: the report and its attachments, the tests, the history of the named area. |
| scope-a-vague-issue.R2-R5, scope-a-vague-issue.G1-G5 | conductor/guidance/software.md §Scoping a vague issue | Reproduce or say you could not; evidence per claim; the test fails for the reported reason; no widening; separate report, behaviour and expectation; name each gap and the reading taken; ask the codebase before the reporter; the smallest reproduction; expected behaviour needs a source, or is recorded as undefined. |
| scope-a-vague-issue.E1, scope-a-vague-issue.E6, scope-a-vague-issue.E11, scope-a-vague-issue.E14 | removed | Phase labels. |
| scope-a-vague-issue.E2-E4, scope-a-vague-issue.E7-E10, scope-a-vague-issue.D1-D5 | conductor/guidance/software.md §Scoping a vague issue | List what the issue does not say; the readings it allows; a clean baseline; every attempt recorded; reduce; a failing test confirmed red for the right reason by changing the suspected cause; separate defects recorded, not fixed. |
| scope-a-vague-issue.E5 | conductor/SKILL.md §8. Authority, budget and confidentiality | Plan stated; wait where needed. |
| scope-a-vague-issue.E12 | conductor/SKILL.md §4. Procedures and evidence | The reproduction, the failing test's verbatim output, and the assumptions. |
| scope-a-vague-issue.E13, scope-a-vague-issue.E15 | conductor/guidance/quality.md §Reviewing work | Review by someone other than the author; feedback addressed. |
| scope-a-vague-issue.E16 | conductor/guidance/software.md §Delivery: review, CI, deploy, rollback | Proposed clearly as a reproduction, not a fix. |
| scope-a-vague-issue.D6, scope-a-vague-issue.D7 | conductor/SKILL.md §10. Reporting | Counts at the end. |

## fix-a-bug-test-first

| IDs | Where it lands | How |
|---|---|---|
| fix-a-bug-test-first.O1, fix-a-bug-test-first.C1, fix-a-bug-test-first.C2, fix-a-bug-test-first.R1, fix-a-bug-test-first.R2 | conductor/guidance/software.md §Fixing a bug, failing test first | Test first, red for the reason in the report (the verbatim failure line names the reported behaviour, not an import or fixture error), committed alone before any code change. |
| fix-a-bug-test-first.C3 | conductor/guidance/software.md §Scoping a vague issue | A vague report is scoped first. |
| fix-a-bug-test-first.C4 | removed | Heading only. |
| fix-a-bug-test-first.C5-C7 | conductor/guidance/software.md §Fixing a bug, failing test first | Where to look; the narrowest module found by running. |
| fix-a-bug-test-first.R3-R5, fix-a-bug-test-first.G1-G6, fix-a-bug-test-first.D5, fix-a-bug-test-first.D6 | conductor/guidance/software.md §Fixing a bug, failing test first | The smallest change, split from refactors; never move the assertion to fit; know which tests were already red; narrow the scope; the report's exact input first; unreproducible is a finding; beware fixes that make the test unreachable; say where the cause really was; look for siblings. |
| fix-a-bug-test-first.E1, fix-a-bug-test-first.E5, fix-a-bug-test-first.E11, fix-a-bug-test-first.E14 | removed | Phase labels. |
| fix-a-bug-test-first.E2, fix-a-bug-test-first.E3, fix-a-bug-test-first.E6-E10, fix-a-bug-test-first.D1-D4 | conductor/guidance/software.md §Fixing a bug, failing test first | Reproduce by hand; baseline; the failing test and its verbatim output; commit it alone; fix until green and stop; full suite; the revert check (the test goes red again with the fix removed). |
| fix-a-bug-test-first.E4 | conductor/SKILL.md §8. Authority, budget and confidentiality | Plan stated; wait where needed. |
| fix-a-bug-test-first.E12 | conductor/SKILL.md §4. Procedures and evidence | Failing and passing output, verbatim. |
| fix-a-bug-test-first.E13 | conductor/guidance/quality.md §Reviewing work | Review by someone other than the author. |
| fix-a-bug-test-first.E15 | conductor/guidance/software.md §Delivery: review, CI, deploy, rollback | The change proposed with what was verified. |
| fix-a-bug-test-first.D7, fix-a-bug-test-first.D8 | conductor/SKILL.md §10. Reporting | Counts at the end. |

## qa-an-agents-tests

| IDs | Where it lands | How |
|---|---|---|
| qa-an-agents-tests.O1, qa-an-agents-tests.C1, qa-an-agents-tests.C2, qa-an-agents-tests.R1, qa-an-agents-tests.R2 | conductor/guidance/software.md §Tests that can fail | Tests written from the implementation cannot catch it; prove each can fail by breaking the behaviour (or putting the original defect back precisely), one break at a time, red on its assertion for the stated reason. A claimed fix with no test is a finding. Also the general rule in SKILL.md §6. |
| qa-an-agents-tests.C3, qa-an-agents-tests.G2-G4 | conductor/guidance/software.md §Tests that can fail | The tells: mocking the unit under test, shape-only assertions, expected values captured by running the code, "no exception" as the only check, fixtures captured from the code. |
| qa-an-agents-tests.C4 | removed | Heading only. |
| qa-an-agents-tests.C5-C7, qa-an-agents-tests.E2, qa-an-agents-tests.E3 | conductor/guidance/software.md §Tests that can fail | The list from history, not names; collected, passed and skipped counts from cold. |
| qa-an-agents-tests.R3-R6, qa-an-agents-tests.G1, qa-an-agents-tests.G5, qa-an-agents-tests.G6, qa-an-agents-tests.D2-D5 | conductor/guidance/software.md §Tests that can fail | Revert every break and confirm a clean tree; a test that cannot fail is fixed or deleted; do not raise coverage to compensate; a test that fails once meaningful is a real defect left failing; mutate the code, not the test; check what is collected; read every skip. |
| qa-an-agents-tests.E1, qa-an-agents-tests.E5, qa-an-agents-tests.E11, qa-an-agents-tests.E14 | removed | Phase labels. |
| qa-an-agents-tests.E4 | conductor/SKILL.md §8. Authority, budget and confidentiality | Plan stated; wait where needed. |
| qa-an-agents-tests.E6-E10, qa-an-agents-tests.D1 | conductor/guidance/software.md §Tests that can fail | Mutate, run that test, restore; group survivors by tell; rewrite against the requirement or delete; re-run under the same mutation; full suite green and `git diff` clean. |
| qa-an-agents-tests.E12 | conductor/SKILL.md §4. Procedures and evidence | The numbers plainly, including the coverage change and its sign. |
| qa-an-agents-tests.E13 | conductor/guidance/quality.md §Reviewing work | Review by someone other than the author. |
| qa-an-agents-tests.E15 | conductor/guidance/software.md §Delivery: review, CI, deploy, rollback | The change proposed with what was verified. |
| qa-an-agents-tests.D6, qa-an-agents-tests.D7 | conductor/SKILL.md §10. Reporting | Verified means red for the stated reason; failed means stayed green (then fixed or deleted); not verified means could not be broken without rewriting the code. |

## review-an-agent-pr

| IDs | Where it lands | How |
|---|---|---|
| review-an-agent-pr.O1, review-an-agent-pr.C1, review-an-agent-pr.R1-R4 | conductor/guidance/software.md §Reviewing an agent's change; conductor/guidance/quality.md §Reviewing work | Every claim in the description checked or marked unchecked; run it, reading is not reviewing; no widening; say what could not be checked. The general rule for reviewing any output (claims checked against the actual result, by someone other than the author) is in `quality.md`; the agent-specific tells stay in `software.md`. |
| review-an-agent-pr.C2 | conductor/guidance/software.md §Reviewing an agent's change | The change under review. |
| review-an-agent-pr.C3 | removed | Heading only. |
| review-an-agent-pr.C4-C6, review-an-agent-pr.E2, review-an-agent-pr.E3 | conductor/guidance/software.md §Reviewing an agent's change | The diff and the issue it claims to close, its tests, and which checks actually gate the merge; the issue's requirements as discrete items. |
| review-an-agent-pr.G1-G6, review-an-agent-pr.D2, review-an-agent-pr.D3 | conductor/guidance/software.md §Reviewing an agent's change | A new test can fail; assertions against the issue, not the diff; the quietly dropped requirement; deleted or weakened assertions, skips and widened tolerances; suppressed errors; the gate that should catch it actually runs. |
| review-an-agent-pr.E1, review-an-agent-pr.E5, review-an-agent-pr.E11, review-an-agent-pr.E14 | removed | Phase labels. |
| review-an-agent-pr.E4 | conductor/SKILL.md §8. Authority, budget and confidentiality | Plan stated; wait where needed. |
| review-an-agent-pr.E6-E10, review-an-agent-pr.D1 | conductor/guidance/software.md §Reviewing an agent's change | Baseline on the base commit; suite on the change and every difference accounted for; break under each new test; each requirement met, partly or not, with file and line; exercise the interface by hand. |
| review-an-agent-pr.E12, review-an-agent-pr.D4, review-an-agent-pr.D5 | conductor/SKILL.md §10. Reporting | One sentence first on whether it does what it says; what was verified, what could not be, and what was found. |
| review-an-agent-pr.E13, review-an-agent-pr.E15 | conductor/guidance/quality.md §Reviewing work | The review posted where the project reviews work. |
| review-an-agent-pr.D6, review-an-agent-pr.D7 | conductor/SKILL.md §10. Reporting | Counts at the end. |

## security-review-agent-code

| IDs | Where it lands | How |
|---|---|---|
| security-review-agent-code.O1, security-review-agent-code.C1, security-review-agent-code.R1-R4 | conductor/guidance/software.md §Security of agent-written code | The shortest route to a green build removes the thing objecting; report with file, line and what an attacker gains; rate by gain; state what was not examined. |
| security-review-agent-code.C2 | conductor/guidance/software.md §Security of agent-written code | The change under review. |
| security-review-agent-code.C3 | removed | Heading only. |
| security-review-agent-code.C4-C6, security-review-agent-code.E2, security-review-agent-code.E3 | conductor/guidance/software.md §Security of agent-written code | The diff, CI, manifests and lockfiles, and fixtures, examples and docs where invented credentials land; the parts on input, credential or permission paths. |
| security-review-agent-code.G1-G7, security-review-agent-code.D2-D4 | conductor/guidance/software.md §Security of agent-written code | A check that cannot fail is the defect; switched-off verification (`verify=False` and kin); credentials in anything the change created, including the history; where each new dependency came from, name checked character by character, lockfile consistent; permissions that widened; a swallowed exception around authorisation; injection wherever a string was built. |
| security-review-agent-code.E1, security-review-agent-code.E5, security-review-agent-code.E11, security-review-agent-code.E14 | removed | Phase labels. |
| security-review-agent-code.E4 | conductor/SKILL.md §8. Authority, budget and confidentiality | Plan stated; wait where needed. |
| security-review-agent-code.E6-E10 | conductor/guidance/software.md §Security of agent-written code | Walk each principle with file and line; make each new check fire; record each dependency's name, version and source; determine whether each credential is live and in history; run the project's scanners and report verbatim. |
| security-review-agent-code.E12, security-review-agent-code.D1, security-review-agent-code.D5 | conductor/SKILL.md §10. Reporting | Findings ordered by what an attacker gains, each with the smallest fix; what was not examined. |
| security-review-agent-code.E13, security-review-agent-code.E15 | conductor/guidance/quality.md §Reviewing work | The review posted where the project reviews work. |
| security-review-agent-code.D6, security-review-agent-code.D7 | conductor/SKILL.md §10. Reporting | Verified means attacked or made to fire and it held; failed means it did not; not verified means not examined, with why. |

## run-the-error-paths

| IDs | Where it lands | How |
|---|---|---|
| run-the-error-paths.O1, run-the-error-paths.C1, run-the-error-paths.C2, run-the-error-paths.R1, run-the-error-paths.R2, run-the-error-paths.G1 | conductor/guidance/software.md §Error paths | Find every handler, cause each failure for real, record what the caller sees; one that cannot be caused is marked unreachable, which is a finding. |
| run-the-error-paths.C3 | removed | Connective sentence. |
| run-the-error-paths.C4-C8, run-the-error-paths.R3-R6, run-the-error-paths.G2-G5 | conductor/guidance/software.md §Error paths | Broad catches narrowed or justified; swallow-and-continue; retries capped, reasoned and safe to repeat; the failure direction written down and safe (an unreadable permission reads as no); tests assert what the caller sees, not that a handler ran; laundered exit codes; the second call; messages that name the thing, the input and the next action. The physical form (failure toward the safe state) is in physical.md §Safety states and irreversible actions. |
| run-the-error-paths.C9 | removed | Heading only. |
| run-the-error-paths.C10-C13, run-the-error-paths.E1, run-the-error-paths.D1 | conductor/guidance/software.md §Error paths | Where to look: every catch and `if err`, retries, fallbacks and defaults, boundaries where others' failures arrive, and what the tests do not cover. |
| run-the-error-paths.E2-E4, run-the-error-paths.D2, run-the-error-paths.D3 | conductor/guidance/software.md §Error paths | Cause, judge (cause kept, caller told the truth, safe direction, retries sound), fix with a test seen to fail first. |
| run-the-error-paths.R7, run-the-error-paths.E5, run-the-error-paths.D4, run-the-error-paths.D5 | conductor/SKILL.md §10. Reporting | Handlers found, executed, unreachable, wrong; verified means executed and correct. |

## verify-a-migration

| IDs | Where it lands | How |
|---|---|---|
| verify-a-migration.O1, verify-a-migration.C1-C4 | conductor/guidance/software.md §Data migrations | What a migration does at real row counts, on the production engine and version, what it locks, whether the rollback works, and the safe deploy order; the dev database hides every one of these. |
| verify-a-migration.C5 | removed | Heading only. |
| verify-a-migration.C6-C9, verify-a-migration.E2, verify-a-migration.E3 | conductor/guidance/software.md §Data migrations | Where to look, and the statements, tables, engine version and row counts. |
| verify-a-migration.R1-R6, verify-a-migration.G1-G7 | conductor/guidance/software.md §Data migrations | Production engine and row counts (or say what is unknown); run the rollback and diff schema dumps; locks per statement; never touch production; re-measure a changed migration; constraints tested against the data; batched backfills killed halfway; the safe deploy order proved both ways; an applied migration is never edited. |
| verify-a-migration.E1, verify-a-migration.E5, verify-a-migration.E13, verify-a-migration.E16 | removed | Phase labels. |
| verify-a-migration.E4 | conductor/SKILL.md §8. Authority, budget and confidentiality | Plan stated; wait where needed. |
| verify-a-migration.E6-E12, verify-a-migration.D1-D5 | conductor/guidance/software.md §Data migrations | The copy on the same engine, seeded; timed statements with locks; the round trip diffed; violating-row counts; interrupted backfill; old and new code against both schemas; the copy destroyed and production untouched; what could not be measured, named. |
| verify-a-migration.E14 | conductor/SKILL.md §4. Procedures and evidence | Numbers reported with the row counts they rest on. |
| verify-a-migration.E15 | conductor/guidance/quality.md §Reviewing work | Review by someone other than the author. |
| verify-a-migration.E17 | conductor/guidance/software.md §Delivery: review, CI, deploy, rollback | The change proposed with what was verified. |
| verify-a-migration.D6, verify-a-migration.D7 | conductor/SKILL.md §10. Reporting | Counts at the end. |

## prove-the-docs

| IDs | Where it lands | How |
|---|---|---|
| prove-the-docs.O1, prove-the-docs.C1, prove-the-docs.C2, prove-the-docs.R1, prove-the-docs.G1 | conductor/guidance/software.md §Documentation that matches the code | Extract every checkable claim and check it by running it; the quickstart is the most important and least tested. The general form (a document, manual or listing is a set of claims about the actual output) is in quality.md §Reviewing work. |
| prove-the-docs.C3 | conductor/guidance/software.md §Documentation that matches the code | Documentation written from names and comments restates intent and is exactly as false; execute the claim. |
| prove-the-docs.C4, prove-the-docs.G2-G6 | conductor/guidance/software.md §Documentation that matches the code | The tells (removed flags, drifted defaults, promised exceptions, old example output, stale version tables, moved links); suspect every number and name; intent verbs first; check every link; every code block is a promise run in order from the documented state; a disagreement may be a code bug, reported rather than papered over. |
| prove-the-docs.C5 | removed | Heading only. |
| prove-the-docs.C6-C9, prove-the-docs.E2, prove-the-docs.E3 | conductor/guidance/software.md §Documentation that matches the code | Where claims live, and the claim list with source lines, grouped by how each will be checked. |
| prove-the-docs.R2-R5, prove-the-docs.E6-E10, prove-the-docs.D1, prove-the-docs.D3-D5 | conductor/guidance/software.md §Documentation that matches the code | The quickstart run literally from cold; do not polish unchecked prose; do not drop hard claims; generated examples produced by running; fix the false claims; re-run the suite and the quickstart. |
| prove-the-docs.E1, prove-the-docs.E5, prove-the-docs.E11, prove-the-docs.E14 | removed | Phase labels. |
| prove-the-docs.E4 | conductor/SKILL.md §8. Authority, budget and confidentiality | Plan stated; wait where needed. |
| prove-the-docs.E12, prove-the-docs.R6, prove-the-docs.D2, prove-the-docs.D6, prove-the-docs.D7 | conductor/SKILL.md §10. Reporting | Claims examined, verified, false, unverifiable; the denominator. |
| prove-the-docs.E13 | conductor/guidance/quality.md §Reviewing work | Review by someone other than the author. |
| prove-the-docs.E15 | conductor/guidance/software.md §Delivery: review, CI, deploy, rollback | The change proposed with what was verified. |

## translate-the-docs

| IDs | Where it lands | How |
|---|---|---|
| translate-the-docs.O1, translate-the-docs.C1-C3, translate-the-docs.R1, translate-the-docs.R2, translate-the-docs.G1, translate-the-docs.G2, translate-the-docs.G5 | conductor/guidance/software.md §Translations | A translation is a fork with no drift signal; record the source revision in every translated file and ship a staleness check that names which are behind and by how much; a stale translation is worse than a missing one. The non-software form (a translated manual or label set records its source version) is in service.md §Brief and acceptance. |
| translate-the-docs.C4, translate-the-docs.C5, translate-the-docs.R5, translate-the-docs.E1, translate-the-docs.D3 | conductor/guidance/software.md §Translations | Overlay builds versus copies decide what an untranslated page does; pages left untranslated on purpose, each with its reason. |
| translate-the-docs.C6 | removed | Heading only. |
| translate-the-docs.C7-C10 | conductor/guidance/software.md §Translations | Where to look: the docs build, the assembly script, existing translations, contribution rules. |
| translate-the-docs.R3, translate-the-docs.R7, translate-the-docs.G3, translate-the-docs.E2 | conductor/guidance/software.md §Translations | Never translate what a reader types or a machine reads; the same structure, headings, anchors and file names. |
| translate-the-docs.R4, translate-the-docs.R8, translate-the-docs.E5 | conductor/guidance/software.md §Translations | Links resolved from where the translated file sits, against the built output; build and look at the switcher, navigation, search and a page. |
| translate-the-docs.R6, translate-the-docs.G4, translate-the-docs.D4 | conductor/guidance/software.md §Translations | Reviewable by someone who does not read the language: what was mechanical, what is prose, what a native reader must check. |
| translate-the-docs.E3, translate-the-docs.E4, translate-the-docs.D1, translate-the-docs.D2 | conductor/guidance/software.md §Translations | The source revision recorded; the staleness check in CI seen failing on a changed source page. |
| translate-the-docs.E6, translate-the-docs.D5, translate-the-docs.D6 | conductor/SKILL.md §10. Reporting | Counts at the end. |

## update-dependencies

| IDs | Where it lands | How |
|---|---|---|
| update-dependencies.O1-O7, update-dependencies.C1 | conductor/guidance/software.md §Dependencies | Runtime, base images, CI actions and build tools included; each update its own verified step; tests against what the lockfile names, from cold; majors read against the code; nothing new unexamined; unused removed; pins with reason and date. |
| update-dependencies.C2 | removed | Connective sentence. |
| update-dependencies.C3-C8, update-dependencies.G1-G4 | conductor/guidance/software.md §Dependencies | Everything at once; green against the old versions; a major taken unread; pinned forever; something new arrived; updating what nothing uses. Small steps; the lockfile is the truth; read the changelog; everything added is new to trust. |
| update-dependencies.C9 | removed | Heading only. |
| update-dependencies.C10-C13 | conductor/guidance/software.md §Dependencies | Where to look: every ecosystem's manifests and lockfiles, runtime and tool version files, changelogs and advisories (from the local mirror when offline), the product's licence. **Replaced**: "the ledger" by the project's records. |
| update-dependencies.R1, update-dependencies.E1 | conductor/guidance/software.md §Dependencies | Baseline from cold, failures named before anything moves. |
| update-dependencies.R2, update-dependencies.E2, update-dependencies.E3 | conductor/guidance/software.md §Dependencies | Stock: outdated, vulnerable, unused; the unused removed as changes. |
| update-dependencies.R3, update-dependencies.E4, update-dependencies.D1 | conductor/guidance/software.md §Dependencies | One step per change (patch and minor per ecosystem; each major alone; the runtime alone), lockfile regenerated by the tool, installed from cold with no cache, full suite; a breaking step reverted. |
| update-dependencies.R4, update-dependencies.E5, update-dependencies.D2 | conductor/guidance/software.md §Dependencies | Each major's breaking changes searched in the code and handled, with a test that fails on the old behaviour where none covered it. |
| update-dependencies.R5, update-dependencies.E6, update-dependencies.D3 | conductor/guidance/software.md §Dependencies | Every new or changed-hands package: licence against the product's, maintainer and source, install scripts, vulnerability scan; one that fails gets another route. |
| update-dependencies.R6, update-dependencies.E7, update-dependencies.D4 | conductor/guidance/software.md §Dependencies | Every pin has a reason and a revisit date; an old unexplained pin is tried or explained. |
| update-dependencies.R7 | conductor/guidance/autonomy.md §Choices on the owner's behalf | A major that cannot be taken yet is recorded with its blocker and route; the rest proceeds without waiting. |
| update-dependencies.G5 | conductor/guidance/operations.md §Upkeep | Dependency updates run on a cadence for anything kept running, so no update is ever large. |
| update-dependencies.R8, update-dependencies.E8, update-dependencies.D5, update-dependencies.D6 | conductor/SKILL.md §10. Reporting | One row per step and per major; counts at the end. |

## template-master-prompt (the Skill Template for authors)

| IDs | Where it lands | How |
|---|---|---|
| template-master-prompt.O1-O4, template-master-prompt.C1-C6, template-master-prompt.R1, template-master-prompt.G1, template-master-prompt.E1, template-master-prompt.E2, template-master-prompt.D1-D3 | removed | The authoring template for a standalone skill. The conductor replaces standalone skills with guidance sections, so there is no skill to author from this shape. Its lasting authoring rules are kept in the three rows below; the rest (section order, placeholders, the denominator line) described the retired format. |
| template-master-prompt.R2 | conductor/SKILL.md §Guidance to load | **Replaced**: guidance sections refer to each other by `file §Heading` rather than repeating a method. |
| template-master-prompt.R3 | conductor/guidance/product.md §Alternative routes | A blocked route gets another route; no guidance concludes that an idea cannot be done. |
| template-master-prompt.R4 | conductor/SKILL.md §10. Reporting | Do not claim what was not checked. |

## workflow.json

The fixed path is replaced by the control loop (decision 3 above). Each step's "done when" is
kept as the gate of the responsibility or guidance section that now does that work; each entry
state becomes an input to classification, and where to start is decided by the first unmet
acceptance, with an incident always first.

| IDs | Where it lands | How |
|---|---|---|
| workflow.step1 | conductor/guidance/autonomy.md §What a harness must do; conductor/guidance/autonomy.md §Briefing: ask once | Gate kept: the briefing answered with its standing limits; sandbox, checkpoints and gates in place. **Replaced**: "the harness passes conformance.py" applies only to a harness built for the project; a stock harness is checked against the same requirements. |
| workflow.step2 | conductor/guidance/product.md §What it takes; conductor/guidance/planning.md §Milestones as usable slices | Gate kept: the owner agreed the path and its first step; the walking skeleton ran end to end and was rolled back once. "The ledger passes the trace check" **replaced** by the records reviewed against the decisions checklist. |
| workflow.step3 | conductor/guidance/software.md §Setup that runs from cold | Gate kept: one command installs and runs the tests from a clean checkout, and breaking a step makes it fail. The non-software form is SKILL.md §4 (the procedure reproduces from a clean start). |
| workflow.step4 | conductor/guidance/design.md §What design covers | Gate kept: each critical journey a flow with every state and word, operable by person and agent with the same limits, threaded to the architecture with no empty cell, tested with people or labelled stand-ins until its target holds. |
| workflow.step5 | conductor/guidance/decisions.md §Recording and superseding decisions | Gate kept: the ADR passes the review checklist, with the owner's approval where it is costly to reverse. |
| workflow.step6 | conductor/SKILL.md §7. Changes | Gate kept: every claim accounted for, every change linked to its work item and evidence (**replaced**: trailers), the measure moved, nothing left detached. |
| workflow.step7 | conductor/guidance/quality.md §Write the bar first | Gate **changed**: every bar row verified, or failed or not verified with its reason and its next step; a bar with open failures supports a completed assessment, not a ready-to-release claim. |
| workflow.step8 | conductor/guidance/quality.md §Reviewing work; conductor/guidance/software.md §Reviewing an agent's change | Gate kept: every claim the change makes is checked, and every new test has been seen to fail. |
| workflow.step9 | conductor/guidance/product.md §Releasing to people | Gate kept: every way in works from a clean device, listings and legal texts match, staged rollout with pause threshold and tried rollback, a help route answered, channel measures taken. |
| workflow.step10 | conductor/guidance/operations.md §Periodic review | Gate kept for anything handed to operations: every measure from its source this run, the next improvements ranked, the records committed. "Then it starts again" **changed**: it repeats on the operator's cadence while the thing runs; a finite project closes (SKILL.md §9). |
| workflow.step11 | conductor/guidance/operations.md §After an incident | Gate kept: restored by a tried action, every person, record and device put right and checked, cause proved by a failing test, each class closed. |
| workflow.step12 | conductor/guidance/software.md §Dependencies | Gate kept: each update its own verified change, the suite passing on the new versions. |
| workflow.entry1 | conductor/SKILL.md §2. The control loop; conductor/guidance/operations.md §Incidents: restore first | Harm to people now interrupts everything: restore first, then the cause, on a copy. |
| workflow.entry2, workflow.entry3 | conductor/SKILL.md §1. Classify the project | **Replaced**: "only a model" versus "an agent that works" becomes the operator part of classification (autonomy.md is loaded when the agent needs a harness or will run unattended). |
| workflow.entry4 | conductor/SKILL.md §1. Classify the project | An existing project in any state has its records written from what is there, its decisions recorded with the evidence they had, then starts at its first unmet acceptance. |
| workflow.entry5, workflow.entry6 | conductor/SKILL.md §1. Classify the project; conductor/guidance/operations.md §Periodic review | Live, or stalled, or drifting: the review re-measures and finds the blocked route and the next one. "For as long as it serves anyone" and "nothing is declared dead" kept as: the owner's goal is not abandoned, and a blocked route gets another route. |
| workflow.entry7 | conductor/guidance/product.md §Requests, however they are worded | A request of any wording enters as a change. |
| workflow.entry8 | conductor/guidance/decisions.md §Which decisions need evidence | A choice enters as a decision. |
| workflow.entry9 | conductor/guidance/quality.md §Reviewing work | Work an agent produced enters as a review. |
| workflow.throughout1 | conductor/SKILL.md §1. Classify the project; conductor/guidance/confidentiality.md §Classes and where they may go | Classification loads confidentiality whenever anything must not leave. |
| workflow.throughout2 | conductor/SKILL.md §1. Classify the project; conductor/guidance/physical.md §Commands and observed outcomes | Classification loads physical whenever the output moves, heats, dispenses, spends or sends. |

## harness/AGENTS.md (the standing rules fragment)

The fragment stays as a short block of standing rules a project copies into its own agent
instructions (`autonomy.md §Standing rules for the project`). Each rule's full method lives in
the section named below; the block itself is rewritten in the new terms.

| IDs | Where it lands | How |
|---|---|---|
| agents.verdicts.1-5 | conductor/SKILL.md §10. Reporting | **Replaced** terms: verified, failed, not verified (with reason); not applicable and authorised exceptions never reported as passes; every report ends with what was judged and what was not. |
| agents.prove-it-can-fail.1-4 | conductor/SKILL.md §6. Gates: verification and validation; conductor/guidance/software.md §Tests that can fail; conductor/guidance/software.md §Pipelines that can fail | A test or a check nobody has seen fail is a claim; no swallowed exit codes; no skipped test to make a suite green. |
| agents.do-not-guess.1-4 | conductor/guidance/software.md §Scoping a vague issue; conductor/guidance/software.md §Documentation that matches the code; conductor/guidance/software.md §Architecture from what runs | Unreproduced is unreproduced; documented paths and flags are claims; scope before fixing; prefer what runs over names. |
| agents.what-not-to-do.1-3 | conductor/guidance/software.md §Tests that can fail | No shape-only assertions, no mocking the unit, no captured expected values. |
| agents.what-not-to-do.4 | conductor/guidance/software.md §Pipelines that can fail | Never remove a failing check to go green. |
| agents.what-not-to-do.5 | conductor/guidance/software.md §Setup that runs from cold | Install, verify, exit. |
| agents.what-not-to-do.6 | conductor/guidance/quality.md §Complexity budget | Add machinery only when you can name what breaks without it. |
| agents.every-change-has-a-reason.1, agents.every-change-has-a-reason.2 | conductor/SKILL.md §3. Work records; conductor/SKILL.md §7. Changes | **Replaced**: the ledger files and trailers by the project's own records, ADRs, and each change linked to its work item and evidence; a change that serves nothing is a question for the owner. |
| agents.every-change-has-a-reason.3 | conductor/guidance/product.md §Alternative routes | Nothing asked for is dismissed; a blocked route gets another, costed honestly. |
| agents.every-change-has-a-reason.4 | conductor/guidance/product.md §Requests, however they are worded | Translate, measure first; a met target is a no with the number. |
| agents.every-change-has-a-reason.5 | conductor/SKILL.md §7. Changes | Contradicting an accepted decision takes new evidence and a superseding record first. |
| agents.every-change-has-a-reason.6 | conductor/guidance/software.md §Complete changes, nothing detached | Wired through every layer; what it replaced is gone. |
| agents.every-change-has-a-reason.7 | conductor/guidance/decisions.md §Evidence | Two backings by kind, one verified; more for a costly-to-reverse decision. |
| agents.every-change-has-a-reason.8 | conductor/SKILL.md §4. Procedures and evidence | **Replaced**: every stage a reproducible procedure anyone responsible can run; nothing only in one agent's memory or tools. |
| agents.confidential-projects.1-5 | conductor/guidance/confidentiality.md §Classes and where they may go; conductor/guidance/confidentiality.md §Agents and models; conductor/guidance/confidentiality.md §Working offline; conductor/guidance/confidentiality.md §Using the internet without revealing the work | Kept as standing rules. |
| agents.working-on-your-own-for-long-stretches.1-4 | conductor/guidance/autonomy.md §Context and state; conductor/guidance/autonomy.md §Choices on the owner's behalf | The records are the memory; look up, do not remember; never wait on what can be decided; apply overrides at once. |
| agents.working-on-your-own-for-long-stretches.5, agents.working-on-your-own-for-long-stretches.6 | conductor/SKILL.md §6. Gates: verification and validation | Nothing done until its gates pass; a failed gate means another attempt or route, never a lower gate; own work reviewed by a fresh context. |
| agents.acting-on-the-world.1-6 | conductor/guidance/physical.md §Commands and observed outcomes; conductor/guidance/physical.md §Safety states and irreversible actions; conductor/guidance/physical.md §Simulation and what it can establish | Kept as standing rules. |
| agents.when-to-load-a-skill.1-18 | conductor/SKILL.md §Guidance to load | **Replaced**: "load the matching skill" is the cause H1 names; the router becomes the conductor's own table of which guidance to load for which classification, and the agent always starts at the conductor. |

## harness/check_trace.py

The checker enforced a home-made format. Its rules protect real behaviours, so each one is
kept as an item on the review checklist of the record it belonged to, and the file itself is a
step 4 decision (retained, replaced or retired, in `docs/migration/checks.md`).

| IDs | Where it lands | How |
|---|---|---|
| trace.L127, trace.L136, trace.L148, trace.L154, trace.L157, trace.L161, trace.L313 | conductor/guidance/product.md §Objective, outcomes and measures | **Replaced**: the project's records state one objective, measures each with what, target, date and method tied to the objective, milestones that move a measure, and no measure nothing moves or serves; checked at review instead of by ID parsing. |
| trace.L165 | conductor/guidance/planning.md §Resources and their sources | Each resource names the decision that chose its source, or that it is owned. |
| trace.L180, trace.L185, trace.L188, trace.L200, trace.L250 | conductor/guidance/decisions.md §Recording and superseding decisions | **Replaced**: ADR numbering, a unique id per ADR, a status from the standard set (proposed, accepted, rejected, superseded, deprecated), and a superseded ADR naming a real successor. |
| trace.L202 | conductor/guidance/decisions.md §Which decisions need evidence | Whether reversing is costly is stated in the ADR, as plain words rather than a required field. |
| trace.L207, trace.L210 | conductor/guidance/decisions.md §Which decisions need evidence | A decision states what it serves; serving nothing means it is not needed. |
| trace.L216, trace.L219, trace.L226, trace.L232, trace.L236 | conductor/guidance/decisions.md §Evidence | Options counted (two, or three for costly-to-reverse); at least two backings, each labelled by kind, at least one verified; two different kinds for a costly decision. |
| trace.L239 | conductor/guidance/decisions.md §A way out and a reopening condition | An accepted decision has a condition that reopens it. |
| trace.L242, trace.L245 | conductor/guidance/decisions.md §A way out and a reopening condition; conductor/guidance/decisions.md §Asking the owner | A costly-to-reverse decision has its exit written and a named approver. |
| trace.L261, trace.L270, trace.L272, trace.L276, trace.L280, trace.L282 | conductor/SKILL.md §7. Changes; conductor/guidance/quality.md §Reviewing work | **Replaced**: each change is linked to its work item and to its evidence in the project's tool; a change that serves a rejected or superseded decision is drift; a review over no changes is not a pass. Checked at review. |

## harness/conformance.py

| IDs | Where it lands | How |
|---|---|---|
| conformance.1-10, conformance.13-16, conformance.19-22 | conductor/guidance/autonomy.md §What a harness must do | Kept as the requirements any harness must meet, stock or built: a loop that ends on done, one request per action, a fresh context each step with the task in it, reads and command output shown next step, writes only inside the project, survives unreadable replies, state kept as written, prompts inside the window (including a small one), a checkpoint after each step with recovery, restarts from the state note, a person's stop honoured before acting, a step limit. |
| conformance.11, conformance.12, conformance.17, conformance.18 | conductor/guidance/autonomy.md §Choices on the owner's behalf | Choices recorded without waiting; the owner's override lines left to the owner and shown next step. |
| conformance.23 | conductor/guidance/autonomy.md §Context and state | **Replaced**: "the short form of a skill" becomes loading one guidance file at a time, and only the sections needed, when the window is small. |
| conformance.24, conformance.25 | conductor/guidance/confidentiality.md §Agents and models | Remote requests through the egress proxy; a remote endpoint refused unless explicitly allowed. The test file itself stays available for a harness built for a project; its home is decided in step 4. |

## harness/ledger-example

| IDs | Where it lands | How |
|---|---|---|
| ledger-example.PROJECT.md, ledger-example.D0001-store-bookings-in-sqlite.md, ledger-example.D0002-host-on-the-shop-pi.md | conductor/templates/adr.md | **Replaced**: the worked example becomes a filled example ADR (the SQLite decision, with its options, evidence by kind, exit and reopening condition) inside the template; the `PROJECT.md` format it illustrated is retired with the ledger. |

## What the owner asked for (QUALITY.md)

These are requirements, not procedures; each is traced to where the conductor meets it.

| IDs | Where it lands | How |
|---|---|---|
| owner.1 | conductor/SKILL.md §1. Classify the project; conductor/SKILL.md §9. Closure and handover | Any project in any state enters by classification and its first unmet acceptance. "Kept there" is met by the handover to a named operator with review triggers, not by an endless loop for every project. |
| owner.2 | conductor/guidance/product.md §What it takes; conductor/guidance/decisions.md §Which decisions need evidence; conductor/guidance/planning.md §Milestones as usable slices | The floor that later stages do not regret: costly decisions with evidence, a procedure for every stage, a walking skeleton. |
| owner.3 | conductor/SKILL.md §4. Procedures and evidence; conductor/guidance/design.md §Every operator | Every procedure has a responsible actor, person, agent or automation; operation by person or agent with the same limits. |
| owner.4 | conductor/SKILL.md §7. Changes; conductor/guidance/decisions.md §Evidence | Every change has a reason and a verification; decisions have two kinds of evidence. **Replaced mechanism**: review against the work record, not the trace check. |
| owner.5 | conductor/guidance/product.md §Requests, however they are worded; conductor/guidance/software.md §Complete changes, nothing detached | Requests translated and shown with numbers; nothing left detached. |
| owner.6 | conductor/guidance/product.md §Journeys and threads; conductor/guidance/design.md §Threads to the architecture | One design seen from flow, architecture and data. |
| owner.7 | conductor/guidance/product.md §Areas and owners; conductor/guidance/design.md §What design covers | Every area founded or explicitly not applicable. |
| owner.8 | conductor/guidance/quality.md §Craft standard; conductor/guidance/quality.md §Complexity budget | Finished, dependable, no useless complexity. |
| owner.9 | conductor/guidance/decisions.md §Options; conductor/guidance/planning.md §Resources and their sources | Options studied widely; portfolios and sequences. |
| owner.10 | conductor/guidance/product.md §Alternative routes; conductor/guidance/operations.md §Periodic review; conductor/SKILL.md §9. Closure and handover | "Nothing is impossible" and "money never stops a project" kept: constraints get routes. "Continuous optimisation" **qualified** per the finalisation proposal: continuous for whatever keeps running, under its operator; a finite project closes on accepted delivery, and closing it does not abandon the owner's broader goal. |
| owner.11 | conductor/guidance/product.md §Areas and owners; conductor/guidance/planning.md §Responsibilities | Each area with an owner, working through shared records; RACI where handoffs get ambiguous. |
| owner.12 | conductor/guidance/autonomy.md §Choosing the agent and harness; conductor/guidance/autonomy.md §Building a missing tool | Stock tools first; built when none fits. |
| owner.13 | conductor/guidance/confidentiality.md §Classes and where they may go | Kept in full. |
| owner.14 | conductor/guidance/autonomy.md §Briefing: ask once; conductor/guidance/autonomy.md §What a harness must do | Ask once, then do not wait. "The model builds its own harness" **qualified**: when no existing harness meets the requirements (H2: do not reinvent). |
| owner.15 | conductor/SKILL.md §How to use this | Harness-agnostic and service-agnostic by construction. How it is found and installed (site, discovery index, plugin, MCP) is decided in step 4. |
| owner.16 | conductor/guidance/physical.md §Hybrid versions and compatibility | Software, physical and hybrid, with service and creative work added. |
| owner.17 | docs/trials/protocol.md | Tested in step 3: real runs of fresh agents through whole cases, inspected on their outputs. |
| owner.18 | repository practice | Not part of the conductor: every commit in this repository is authored and committed by the owner alone, with no co-author lines. |

## Planted defects in the fixtures

Every fixture stays as a retained failure case for step 3: the conductor, given the fixture,
must still catch each defect. Each defect is mapped to the guidance section whose instruction
catches it; step 2 is checked by confirming that section, read alone, would lead an agent to
name the defect.

| IDs | Where it lands | How |
|---|---|---|
| fixture.bumped-everything.everything-at-once, fixture.bumped-everything.lockfile-not-regenerated, fixture.bumped-everything.major-read-against-nothing, fixture.bumped-everything.unexplained-vulnerable-pin, fixture.bumped-everything.unused-updated, fixture.bumped-everything.agpl-arrived | conductor/guidance/software.md §Dependencies | One step per change; lockfile regenerated and installed from cold; majors read against the code; pins with reason and date; unused removed; everything new examined, licence included. |
| fixture.command-accepted.trusts-the-ack, fixture.command-accepted.retries-a-dispense, fixture.command-accepted.units-mismatch | conductor/guidance/physical.md §Commands and observed outcomes | Independent observation; no retry of an action that may have happened; units at every boundary. |
| fixture.command-accepted.fails-hot, fixture.command-accepted.no-watchdog | conductor/guidance/physical.md §Safety states and irreversible actions | Failure goes to the safe state; a watchdog on anything that runs until told to stop. |
| fixture.command-accepted.real-by-default | conductor/guidance/physical.md §Simulation and what it can establish | The simulator is the default target. |
| fixture.designed-by-default.flow-by-build-order, fixture.designed-by-default.developer-words | conductor/guidance/design.md §Flows, states and words | Shortest flow, every field used; every word designed. |
| fixture.designed-by-default.undo-without-history | conductor/guidance/design.md §Threads to the architecture | Every promise has the data model to keep it. |
| fixture.designed-by-default.taste-as-evidence | conductor/guidance/design.md §Taste and evidence | Taste is the owner's call between rendered directions; the rest is measured. |
| fixture.designed-by-default.stand-ins-as-people | conductor/guidance/design.md §Testing with people | Stand-ins labelled as simulation, never as people. |
| fixture.designed-by-default.values-outside-the-system | conductor/guidance/design.md §One system of look and behaviour | A value outside the tokens is a defect. |
| fixture.designed-by-default.contrast | conductor/guidance/design.md §Accessible and inclusive | Contrast computed against WCAG 2.2 AA. |
| fixture.designed-by-default.limit-only-in-the-page, fixture.designed-by-default.agent-path-missing | conductor/guidance/design.md §Every operator | Limits enforced in one place every path passes; a machine interface for every action. |
| fixture.error-path-never-run.bare-except, fixture.error-path-never-run.untested-failure | conductor/guidance/software.md §Error paths | Broad catches narrowed; every failure caused for real. |
| fixture.finished-looking-pr.claim-unverified, fixture.finished-looking-pr.send-commented-out, fixture.finished-looking-pr.test-cannot-fail | conductor/guidance/software.md §Reviewing an agent's change | Every claim checked by running it; each new test broken to see it fail. |
| fixture.fixed-before-tested.suite-already-red, fixture.fixed-before-tested.red-for-the-wrong-reason, fixture.fixed-before-tested.test-and-fix-in-one-commit, fixture.fixed-before-tested.paraphrased-input, fixture.fixed-before-tested.fix-bundled, fixture.fixed-before-tested.sibling-missed | conductor/guidance/software.md §Fixing a bug, failing test first | Baseline named; red for the reported reason; test committed alone; the report's exact input; smallest change; siblings found. |
| fixture.green-pipeline.paths-never-match, fixture.green-pipeline.wrong-test-dir, fixture.green-pipeline.pipe-to-tee, fixture.green-pipeline.continue-on-error | conductor/guidance/software.md §Pipelines that can fail | Filters that match nothing, discovery that collects nothing, pipes that discard status, swallowed failure. |
| fixture.looks-finished.loses-work | conductor/guidance/quality.md §Failures caused on purpose | What must never be lost, tested by reloading and killing mid-write. |
| fixture.looks-finished.script-injection | conductor/guidance/software.md §Standards to apply | Untrusted input never becomes HTML; each attack tried. |
| fixture.looks-finished.chromium-only | conductor/guidance/quality.md §Every platform and environment, for real | Every platform run; capabilities detected. |
| fixture.looks-finished.blank-error, fixture.looks-finished.phone-overflow, fixture.looks-finished.focus-hidden, fixture.looks-finished.no-empty-state | conductor/guidance/quality.md §Craft standard | Errors that say what to do; 320 px with no sideways scroll; visible focus; every state designed. |
| fixture.looks-finished.dead-weight | conductor/guidance/quality.md §Complexity budget | Everything added names what breaks without it. |
| fixture.map-from-folders.layers-do-not-hold, fixture.map-from-folders.not-a-separate-service, fixture.map-from-folders.unused-is-loaded, fixture.map-from-folders.two-writers-one-table, fixture.map-from-folders.no-provenance | conductor/guidance/software.md §Architecture from what runs | Imports resolved; boundaries that fail separately; configuration-driven loading named; follow the data; provenance per claim. |
| fixture.migrated-on-empty.wrong-engine-empty-tables, fixture.migrated-on-empty.guessed-row-count, fixture.migrated-on-empty.rollback-read-not-run, fixture.migrated-on-empty.locks-not-measured, fixture.migrated-on-empty.constraint-violations-uncounted | conductor/guidance/software.md §Data migrations | Production engine and row counts; the round trip run and diffed; locks measured; violating rows counted. |
| fixture.optimise-it.unmeasured-cache, fixture.optimise-it.real-slowness-missed | conductor/guidance/product.md §Requests, however they are worded | Measure first, find where the feeling comes from. |
| fixture.optimise-it.contradicts-decision | conductor/SKILL.md §7. Changes | A change that contradicts an accepted decision reopens it first. |
| fixture.optimise-it.never-wired, fixture.optimise-it.two-sources-of-truth, fixture.optimise-it.config-never-read | conductor/guidance/software.md §Complete changes, nothing detached | Everything reached, one source per fact, every key read. |
| fixture.optimise-it.untraced | conductor/SKILL.md §7. Changes | **Replaced**: a change not linked to a work item and a measure is untraced; the fixture's `Serves:` wording is read as that link missing. |
| fixture.premature-start.no-need-evidence, fixture.premature-start.no-money | conductor/guidance/product.md §What it takes | Need with sources; cost, price and funding routes worked out. |
| fixture.premature-start.unmeasurable-goal | conductor/guidance/product.md §Objective, outcomes and measures | A measurable objective and a switch condition. |
| fixture.premature-start.battery-arithmetic | conductor/guidance/planning.md §Estimates and arithmetic | Every number redone with units. |
| fixture.premature-start.assumes-wifi, fixture.premature-start.first-option-taken | conductor/guidance/decisions.md §Options | Real options compared; the first found is not the answer. |
| fixture.premature-start.premature-scale | conductor/guidance/quality.md §Complexity budget | Nothing built that no need asks for yet. |
| fixture.premature-start.layered-milestones | conductor/guidance/planning.md §Milestones as usable slices | Vertical slices, not layers. |
| fixture.premature-start.agent-only-pipeline | conductor/SKILL.md §4. Procedures and evidence | Every stage a procedure anyone responsible can run. |
| fixture.premature-start.no-certification | conductor/guidance/product.md §Areas and owners; conductor/guidance/physical.md §Certification | Every area founded; radio certification for a device sold to the public. |
| fixture.private-by-accident.plaintext-remote, fixture.private-by-accident.editor-telemetry, fixture.private-by-accident.crash-reports-leave | conductor/guidance/confidentiality.md §Every channel that can carry the work out | Every channel mapped and closed or controlled. |
| fixture.private-by-accident.cloud-agent-whole-repo | conductor/guidance/confidentiality.md §Agents and models | Least excerpt, released classes, local model where required. |
| fixture.private-by-accident.name-leaks-to-registry | conductor/guidance/confidentiality.md §Working offline | Installs that refuse the public index; internal names never reach it. |
| fixture.private-by-accident.offline-never-tested | conductor/guidance/confidentiality.md §Working offline | Offline proved by blocking egress. |
| fixture.private-by-accident.research-names-the-work | conductor/guidance/confidentiality.md §Using the internet without revealing the work | Ask about the technique, never the project. |
| fixture.restored-last.debugged-before-restoring, fixture.restored-last.unsafe-retries, fixture.restored-last.alert-silenced-by-agent, fixture.restored-last.nobody-told, fixture.restored-last.evidence-rotated | conductor/guidance/operations.md §Incidents: restore first | Tried restore first; stop unsafe retries; agents within limits never silence alerts; tell people early; keep evidence. |
| fixture.restored-last.hotfix-skipped-gates, fixture.restored-last.not-everyone-put-right, fixture.restored-last.blame-not-system | conductor/guidance/operations.md §After an incident | Fix through the gates; everyone put right from the data; the system changes, not the person. |
| fixture.security-check-removed.check-deleted, fixture.security-check-removed.shell-injection | conductor/guidance/software.md §Security of agent-written code | A check that cannot fail is the defect; injection wherever a string was built. |
| fixture.setup-succeeds-while-failing.swallowed-install, fixture.setup-succeeds-while-failing.blocking-server, fixture.setup-succeeds-while-failing.no-set-e | conductor/guidance/software.md §Setup that runs from cold | True exit codes; nothing blocks; failures visible. |
| fixture.shipped-to-nobody.dead-download-link, fixture.shipped-to-nobody.first-run-on-the-builders-phone, fixture.shipped-to-nobody.listing-contradicts-product, fixture.shipped-to-nobody.wrong-place-wrong-words | conductor/guidance/product.md §Releasing to people | Way in walked from a clean device; listings true to the product; channels where people are, in their words. |
| fixture.shipped-to-nobody.everyone-at-once | conductor/guidance/software.md §Delivery: review, CI, deploy, rollback | Staged rollout with a pause threshold. |
| fixture.shipped-to-nobody.nobody-listening | conductor/guidance/product.md §Hearing back | A help route that someone answers. |
| fixture.shipped-to-nobody.quiet-launch-read-as-verdict | conductor/guidance/product.md §Alternative routes | A quiet channel switches to the next route. |
| fixture.silent-backup.check-left-of-pipe, fixture.silent-backup.not-verified-by-effect, fixture.silent-backup.copy-failure-swallowed, fixture.silent-backup.deletes-before-it-has-a-new-one, fixture.silent-backup.log-says-nothing, fixture.silent-backup.restore-check-dropped | conductor/guidance/software.md §Automations that report their own failure | No check left of a pipe; verified by effect; no swallowed status; safe to interrupt; the log says what it read; say what it will not do. The restore check is also operations.md §Backups and restore. |
| fixture.six-months-in.measure-missed-quietly, fixture.six-months-in.superseded-still-running, fixture.six-months-in.ghost-dependency, fixture.six-months-in.manual-path-broken, fixture.six-months-in.cost-over-budget | conductor/guidance/operations.md §Periodic review | Measures from their source; what nothing serves; both paths run; spend against budget. |
| fixture.six-months-in.trigger-fired | conductor/guidance/decisions.md §A way out and a reopening condition | Reopening conditions evaluated each review. |
| fixture.six-months-in.restore-never-tried | conductor/guidance/operations.md §Backups and restore | Restores on schedule. |
| fixture.skipped-to-green.silent-module-skip, fixture.skipped-to-green.assertion-weakened, fixture.skipped-to-green.default-still-needs-redis, fixture.skipped-to-green.integration-run-deleted, fixture.skipped-to-green.collection-not-reconciled | conductor/guidance/software.md §Tests that do not need services | No silent skips; assertions unchanged; the default run isolated; the full run kept; counts reconciled. |
| fixture.stale-docs.missing-path, fixture.stale-docs.wrong-flag, fixture.stale-docs.python-requirement | conductor/guidance/software.md §Documentation that matches the code | Every path, flag and number run or checked. |
| fixture.translated-once.no-source-revision, fixture.translated-once.stale-with-no-check, fixture.translated-once.machine-text-translated, fixture.translated-once.image-path-broken, fixture.translated-once.anchor-broken, fixture.translated-once.half-translated | conductor/guidance/software.md §Translations | Source revision and staleness check; machine text untranslated; links from where the file sits; structure kept; untranslated on purpose, never half. |
| fixture.unattended-run.context-overflow, fixture.unattended-run.invented-api | conductor/guidance/autonomy.md §Context and state | Fresh context under half the window; look up, do not remember. |
| fixture.unattended-run.waited-on-the-person, fixture.unattended-run.asked-what-it-could-look-up | conductor/guidance/autonomy.md §Choices on the owner's behalf | Never wait on what can be looked up or reversibly chosen. |
| fixture.unattended-run.no-sandbox, fixture.unattended-run.no-checkpoints | conductor/guidance/autonomy.md §Sandbox, checkpoints and stop | A sandbox holding only the project; a checkpoint after every step. |
| fixture.unattended-run.self-review, fixture.unattended-run.done-unverified | conductor/SKILL.md §6. Gates: verification and validation | Review by a fresh context; gates run after the last change. |
| fixture.unfailable-tests.shape-assertion, fixture.unfailable-tests.mocks-the-unit, fixture.unfailable-tests.reconstructed-expected, fixture.unfailable-tests.no-exception | conductor/guidance/software.md §Tests that can fail | The four tells, each found by mutating the code. |
| fixture.vague-issue.unscoped-issue, fixture.vague-issue.three-readings, fixture.vague-issue.no-fix | conductor/guidance/software.md §Scoping a vague issue | Name the gaps, enumerate the readings, produce no fix. |
| fixture.vendor-comparison.criteria-not-from-measures | conductor/guidance/decisions.md §Criteria before scores | Criteria from the objective and measures, hard limits as pass or fail. |
| fixture.vendor-comparison.missing-options | conductor/guidance/decisions.md §Options | Doing nothing, what exists, combining. |
| fixture.vendor-comparison.egress-arithmetic | conductor/guidance/decisions.md §Redo every number | Recompute with units. |
| fixture.vendor-comparison.vendor-claim-only, fixture.vendor-comparison.unrepresentative-test | conductor/guidance/decisions.md §Evidence | A vendor claim is a claim; the test shaped like the use. |
| fixture.vendor-comparison.door-misclassified | conductor/guidance/decisions.md §Which decisions need evidence | Holding the public URLs makes it costly to reverse. |

