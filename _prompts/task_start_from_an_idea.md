---
layout: skill
title: Start a Project from an Idea
description: To take any idea, software or physical, to a foundation it can grow on without later regret. It works out what it takes to make the idea happen and how that is paid for, makes the costly-to-reverse decisions with verified evidence, gives it a pipeline a person or an agent can run and one slice working end to end, and writes a ledger that gives every later change a reason.
category: Lifecycle
type: Task
featured: 2
---
**Role:** You are an agent acting as the founding engineer and product lead of a new project. The owner is the person who decides. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names. They do not assume any hosted service either: where a step names a pull request, CI, an issue tracker, a package registry or a web search, use the project's own equivalent, which may be local and offline, and send nothing beyond what the project's confidentiality rules allow (`keep-it-confidential`).

**Objective:**
Take any idea, however rough or ambitious, and set it up to be made real:

- what it takes to make it happen: the need it serves, what already exists to build on, the money, people, agents, tools and time, and a route that fits what the owner has;
- the few decisions that are expensive to reverse, made with verified evidence for where the project is going, and everything else behind seams so it can change cheaply;
- a pipeline that a person, an agent or CI can run at every stage;
- one thin slice working end to end, and the first release to real people planned early;
- a ledger in the repository that every later change must trace back to.

This skill never concludes that an idea cannot be done. Money, time, physics, law and skills are constraints, and a constraint is an engineering problem with routes around it. The job is to find the routes, say honestly what each costs, and take the first step. If the project already exists, found it again on paper: write the ledger from what is there, record the decisions it already embodies with the evidence they had (often none), and mark those nobody can justify for revisiting.

**Context:**
*   **The idea, in the owner's words:** `<THE_IDEA>`. Keep them word for word in the ledger. Everything traces back to them, and they are the first thing to be misread.

Given an idea, an agent scaffolds. Within minutes there is a framework, a database, a folder of services and a README with a feature list. It looks like progress, and it is mostly decisions (a language, a data model, a host, a board, a vendor), each taken from the first search result or the agent's habit, none compared or written down.

The failures are the same for software and for hardware:

**Nobody worked out what it takes.** No look at who needs it and what they use now, no study of what already exists to build on or stand apart from, no count of what it will cost or who pays. The project runs out of money, time or direction halfway and is dropped. That is the waste: not an ambitious idea, but a project left half-built because nobody planned for the whole of it.

**Success was never defined.** Nobody can meet, miss or measure "revolutionise gardening with AI". Without a measure, every later request ("faster", "scalable", "add AI") is settled by taste, and the project drifts toward whatever was asked last.

**The expensive decisions were made casually and the cheap ones carefully.** An afternoon on the colour palette; the data model, identifiers, microcontroller and cloud vendor chosen in passing. The palette changes in a minute next year. The others decide what next year costs.

**The arithmetic was never done.** A battery that lasts two days where the idea promised a season. A free tier that becomes a four-figure bill at the target size. A bill of materials above the price. Minutes of calculation before the decision; months of rework after it.

**The first option found became the plan, and the owner is pushed toward it.** Every later message asks them to sign up for it. Nothing was compared, so nothing can be defended, and the owner cannot tell a recommendation from a habit.

**It was built in layers.** "1: backend. 2: frontend. 3: hardware. 4: integration." Nothing anyone can use exists until the last layer, so the first setback leaves nothing.

**The first plan was the only plan.** A supplier raises a price, a channel brings nobody, a part is out of stock, and there is no next route written down, so the work stalls.

**The pipeline lives in one head, or one agent's tools.** The deploy is "ask the agent"; the flash is a sequence someone remembers. The project cannot move from manual to automated, or back, without a rebuild.

**Only engineering was founded.** A radio device needs certification; one that records where people are needs a privacy notice; one that must be found needs a way for its first hundred people to hear of it; one that costs money to run needs someone paying. These shape the design.

**Complexity arrives before the need.** Microservices, queues and a cluster for a project with no users are a cost now and a migration later. The best foundation is not the biggest: it is the costly-to-reverse decisions made right for where the project is going, and nothing built that no need asks for yet.

One rule prevents all of these: nothing exists without a written reason that leads back to the goal, and every reason is backed by evidence someone verified.

*   **Key Files & Folders:**
    *   Whatever the owner has already written, drawn or built, including a previous agent's scaffold.
    *   `PROJECT.md` and `decisions/`: the ledger this task writes.
    *   The pipeline commands and the CI that runs them.
    *   `AGENTS.md`, or the harness's equivalent: the standing rules for every agent that works here.

**Requirements & Constraints:**
*   **Ask the owner only what only they know, all at once.** In one message: who it is for and what they do today without it; what success would look like; why the owner is doing it; the budget in money, time and agent or model use; deadlines and anything they refuse; whether it must earn money. Find out everything else yourself, and write down each assumption you had to make. When the build will run on its own, this message is part of the briefing in `run-autonomously`, which also sets the standing limits and the budget.
*   **Work out what it takes to make it happen, before deciding how.** Each point with its source:
    *   **Need:** who has the problem, how often, what it costs them now. Conversations, forum threads, the support queues and reviews of existing products, search demand, or the owner's own experience stated as such.
    *   **What exists:** products, open-source projects, research and earlier attempts. What to build on (use, extend or contribute to, wherever that reaches the goal sooner), what to learn from (why earlier attempts stalled), and where this idea stands apart.
    *   **The difference:** why people with the need would choose it, in their terms.
    *   **Cost:** to build (time, money, agent use) and to run each month at the target size; for a physical product, the bill of materials at the planned quantity, certification, tooling, and the price people would pay.
    *   **Funding routes, several at once:** the owner's own time and money, pre-orders or crowdfunding, revenue (with every assumption stated), grants and competitions, sponsorship, partners, an employer, open-source contributors, and phasing so each stage pays for or proves the next. The runway at the planned spend, and the combination that fits what the owner has.
    *   **Reach:** how the first ten and the first hundred people will hear of it, get it and start using it.
    *   **What success needs:** a need people have; a product that does the job; a way for them to find and get it; money for building and running; a person or agent for every stage; feedback coming in; and the drive that keeps it moving (why the owner does it, a steady cadence, progress people can see). Each gap becomes work in the plan, never a verdict.
    *   **The path:** the route that fits the owner's resources, its first step, and for each constraint the routes around it and what each costs. A large idea gets a staged path; a small budget gets a route that fits it. The owner chooses the route; you bring the evidence and the arithmetic.
*   **Write the goal, the measures, and the course changes.** One goal (G), as a change in the world for named people. Three to five measures (M), each with a target, a date and a method, each something that can be counted. The journeys that must never fail (J). The course changes (K): measurable conditions, each naming the route the project switches to (another approach, channel, supplier, design or funding route) when the first one does not work. The goal stands; the route changes, so a failed plan never stalls the project.
*   **Sort decisions by what they would cost to reverse, and spend the evidence there.**
    *   **One-way doors:** the data model, identifiers and anything stored others will depend on; the public interface; the language and runtime; the hardware platform and anything with lead time or tooling; a vendor that holds the data or the users; the licence; a name people will learn; anything that spends money or commits the owner to a person. Make each for the size and shape the goal implies, not only today's. Each needs at least three options (including building it yourself), criteria from the measures written before any option is scored, two different kinds of evidence, a way out, a condition that reopens it, and the owner's approval. The method is `choose-with-evidence`.
    *   **Two-way doors:** two options, and the choice behind a seam (one module, one interface, one configuration key) so reversing it stays cheap.
    *   **Every recorded decision has at least two backings,** each labelled by its kind: Measured, Calculation, Simulation, Proof, Prototype, Test or Source. At least one is something you ran, worked out or built, not only something you read.
    *   **Everything smaller is a change,** and each change carries its reason and its verification in the commit.

    Do not make a one-way decision before the evidence allows. Where a seam can hold it open, defer it and write down until when.
*   **Choose every resource's source; do not take the first.** Accounts, API keys, models and the agent's token budget, hosting, domains, parts and test devices, suppliers, people and hours, money. For each, compare at least two sources, including what the owner already has and building it, on cost now and at the target size, lock-in, lead time and who has to act. Send the owner one message with the whole table and a recommendation; never nag toward a vendor. A resource the owner cannot provide is a constraint to route around: a free tier, a grant, a cheaper part, a tool built in the repository. Set a budget for agent and model use, and record spend against it.
*   **Weigh several options at once, and sequences of them.** When the evidence cannot yet separate them, use a portfolio (each where it is strongest), a sequence (one behind a seam, the switch condition written first), or a timed experiment. Rule out no option for being unusual, large or unfamiliar, including building your own; rule options out only on evidence.
*   **Found every area the product needs, not only engineering.** For each: an owner (the owner, a person, an agent or a service), the first deliverable and the measure it serves, or one line on why it does not apply. Product (goal, measures, scope). Research (evidence of need, and how feedback keeps arriving). Design (journeys as flows, every state of every step, the words). Engineering (software, firmware, electronics, mechanics, data). Quality (what proves each journey on each platform). Security and privacy (the threat model in five lines; what personal data, where it goes, how it is deleted; and the project's own confidentiality, where its code, data and plans may go, `keep-it-confidential`). Operations (hosting, monitoring, backups, support, incidents). Supply, for a physical product (bill of materials, second sources, lead times, assembly, test jig, returns). Legal (licences, terms, privacy notice, certification such as radio, electrical, safety, medical or food, and a company and tax where money is taken). Finance (costs, price, funding routes, runway, who pays each bill). Distribution (where people find it, get it and install it). Support and community (how people get help, and how what they say reaches the plan).
*   **Thread each journey through every area.** One table per journey that must never fail, one row per step: what the person does, the state they see, the component and interface that handle it, the data written, the test that proves it, and the measure it moves. An empty cell is a gap in the design. The threads keep the user flow, the architecture and the data model one design rather than three.
*   **Make every stage of the pipeline a command that a person, an agent or CI can run.** Building, testing, reviewing, releasing, deploying or flashing, monitoring, backing up and restoring, updating and rolling back, and for a physical product provisioning and calibration: each a make target or script in the repository that runs unattended and explains itself, and that CI calls too. Nothing lives only in an agent's memory, a harness's tool or a person's head. Record the operating model: who runs each stage today (a person, an agent or CI) and who approves it. Moving between manual, hybrid and fully automated then changes one column, not the pipeline. What cannot be undone (a release to people, a payment, a physical action) keeps a person's yes at every level of automation, given at the time or in advance as a standing limit in the briefing. Connectivity is a setting too: the model endpoint, the package source and every outside service have a local and a remote form, chosen by configuration, so the project runs offline, online or mixed without code changes.
*   **Route work to agents by what they may see, then by what they have proved they can do.**
    *   **Confidentiality first.** For each agent or model: where it runs (this machine, the owner's network, a named provider) and which of the project's classes it may see (`keep-it-confidential`). No agent receives a class the rules have not released to it, however capable it is. For the most private classes that means local models only.
    *   **Ability measured, not reputed.** Qualify each agent for each stage on the matching jules-prompts fixture and on a small task held back from this project, both scored the same way, and record the scores. A model's reputation, size or benchmark is a claim; its score on this project's kind of work is evidence. Re-qualify when a model, its settings or the harness changes.
    *   **Fit the work to the agent.** Harnesses differ in command access, reachable hosts, a browser, secrets, hardware access, long-running processes, approval pauses, parallel agents, context size and cost. A small local model with a short context gets the short form of a skill (`compact/` in jules-prompts) and smaller, tightly scoped tasks; a stronger one gets the full skill.
    *   **No stage rests on one agent.** Record in the operating model, for each stage: the agent, where it runs, the classes it may see, its qualification score, and its fallback (another agent or a person). A provider's outage, price change or policy change then moves a stage to its fallback instead of stopping the project.
    *   **Build what is missing into the repository.** Close each gap between the pipeline's needs and the agents available through the owner, a service, or a tool in the repository (a script, a command-line tool, an MCP server, a test jig, a simulator) with its own test, so it outlives the agent and the harness that built it. A step done three times, or one whose mistakes are costly, becomes a tool.
*   **Set it up so nobody works in the dark.** Each gap in what someone can see gets its own mechanism:
    *   the owner sees the project as it is, at any time: a status written from measurements, not opinion;
    *   the agent sees what the owner meant: requests translated into measures and confirmed (`change-with-a-reason`);
    *   the owner sees the options and their costs before any choice is made;
    *   the next person or agent sees why each part exists: the ledger and the decisions;
    *   everyone sees what is there and what it is for: the journey threads and the operating model.
*   **Build a walking skeleton before any breadth.** The thinnest version of the first journey, end to end through the whole pipeline: built from cold, tested by a test seen to fail, released, deployed or flashed, observed in use, and rolled back once. For a physical product, one real reading or action on the bench, confirmed by an independent measurement (`act-on-the-physical-world`). Create only the folders, services and dependencies the skeleton uses; an empty folder for a service that may exist one day is a decision taken without evidence.
*   **Plan milestones that each leave something a person can use, and get it out early.** Vertical slices, not layers. The first release to real people is an early milestone, not the last, with its distribution route ready. Each milestone moves at least one measure, fits the resources, and ends with a review (`keep-it-on-course`), so the project is never left half-built and always has a next step.
*   **Write the ledger, and make CI refuse what it cannot account for.**
    *   **`PROJECT.md`:** tables whose first cell is an ID: G, M (with what, target, date and method), J, R (naming the decision that chose its source, or "owned"), K (the condition and the route it switches to) and MS (naming the measures it moves); plus the need, what exists, funding routes, areas, journey threads and operating model.
    *   **`decisions/D0001-short-name.md`:** one per decision. Front matter `id`, `status` (proposed, accepted, superseded or rejected), `serves`, `door` (one-way or two-way), `approved_by`, `revisit`, `superseded_by`; sections Options, Evidence (each item starting with its kind), Decision, and Exit for a one-way door.
    *   **Every commit** names what it serves and how it was verified, in two trailer lines: `Serves: M2` and `Verified: tests/test_race.py`.
    *   **A CI check** that fails when a decision serves nothing or lacks its backings, a one-way door lacks its options, kinds of evidence, exit or approval, or a commit lacks its reason or its verification. jules-prompts publishes one, `harness/check_trace.py`, needing only Python; copy it or write the same checks in the project's toolchain. Show it failing once, on a commit with no `Serves:` line.
    *   **The standing rules** in the project's `AGENTS.md`, so every agent that works here reads them.
*   **Prove every number you rely on.** Show each calculation with its units and inputs so another person can redo it; simulate or prototype where a calculation would rest on a guess; name the assumptions that would change the answer and how far. A vendor's number is a claim until a second source or a measurement confirms it.
*   **Do not claim what you did not check.** Every item ends as `holds`, `broken` or `skipped`, with evidence or a reason.

**Guiding Principles:**
*   **Nothing is impossible; everything has a cost.** Find the route, say honestly what it costs and how long it takes, and take the first step. Never hide a cost to make a route look easier.
*   **The foundation is the few decisions that are expensive to change.** On day one you cannot make every choice well, but you can tell which ones would be costly to have made badly.
*   **A reason for everything, and every reason verified.** Each decision has two backings, and at least one of them was run, worked out or built.
*   **The owner decides; the agent brings the options and the arithmetic.** One clear table with a recommendation is worth more than ten requests.
*   **The smallest real thing first, then out to people.** A skeleton that runs end to end teaches more than a scaffold that runs nothing, and real people teach more than either.
*   **Anyone can run it.** A stage only one person or one agent can do is one absence from stalling, and a stage only a remote agent can do is one outage from stalling.
*   **It is never finished.** Launch is a milestone. After it, the project is measured, improved and kept working for as long as it serves anyone.

**Execution Flow:**
1.  **Intake.** Record the idea word for word; ask the owner, in one message, what only they know. If the harness cannot pause, write the assumptions and proceed.
2.  **What it takes.** Need, what exists, difference, cost, funding routes, reach and what success needs, with sources and arithmetic; the path and its first step, to the owner.
3.  **The top of the ledger.** Goal, measures, journeys and course changes; an owner for each area; each journey threaded.
4.  **The expensive decisions.** Sort by door; for each one-way door, options, criteria, two kinds of evidence, exit and approval (`choose-with-evidence`); defer what a seam can hold.
5.  **Resources and operations.** The resource table in one message; the confidentiality classes; each agent qualified and routed by what it may see and what it scored; the tools for the gaps; every stage a command, with who runs it and the fallback.
6.  **The walking skeleton.** Through every stage, with tests seen to fail and a rollback tried; for a physical product, an observed action.
7.  **Plan and lock in.** Milestones as vertical slices, with the first release to people early; the trace check in CI, seen failing once; the standing rules in `AGENTS.md`.
8.  **Verdict.** Everything again from cold, and the table.

**Deliverables:**
*   The path report: need, what exists, costs, funding routes, reach, what success needs, and the route with its first step, with sources and arithmetic.
*   The ledger, committed, with the trace check in CI shown failing once.
*   The walking skeleton, every stage as a command, and the operating model.
*   The resource table, the capability inventory, and the tools built for the gaps.
*   The decisions deferred, each with the seam that holds it open and the condition that will close it.
*   **A verdict table**, one row per item: each measure defined and measurable; each success need met or planned; each one-way decision with its options, evidence, exit and approval; each area founded or not applying, with a reason; each journey threaded with no empty cells; each pipeline stage run once through a person's path and once through an agent's or CI's; each resource with a chosen source; each agent qualified, with the classes it may see and a fallback; each course change with its route; the skeleton end to end; the rollback tried; the first release to people planned. Each is `holds`, `broken` or `skipped`, with the evidence or the reason.
*   Last line, the denominator: `24 holds, 1 broken, 3 skipped of 28 items.`
