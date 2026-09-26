# Product: what it is for, and reaching the people it is for

Load for every project. It covers the objective and how it is measured, what it takes to make
the idea happen, the areas the product needs, the journeys that must never fail, translating
requests, releasing to people, and hearing back. Design detail is in `design.md`; choices are
in `decisions.md`; planning the work is in `planning.md`.

## Intake: what only the owner knows

- **Keep the owner's words word for word** in the records: the idea, the request, the project
  as they describe it. Everything traces back to them, and they are the first thing to be
  misread.
- **Ask the owner, in one message, only what only they know:** who it is for and what those
  people do today without it; what success would look like; why the owner is doing it; the
  budget in money, time and agent or model use; deadlines and anything they refuse; whether it
  must earn money; and what must stay private. Find out everything else yourself.
- **Write down every assumption you had to make,** with the cheapest way to check it. If the
  owner cannot be reached, proceed on the assumptions and mark them for confirmation.

## Starting from nothing or a single word

When there is no idea yet, or only a word ("gardening", "an app", "something with my
workshop"):

1. **Ask what the owner brings:** their interests, skills, time, money, equipment, the people
   they know, and anything they refuse to do. If they are unavailable, work from what the
   records and their words show, and say so.
2. **Expand the word into candidate problems:** who has a problem near it, how often, and what
   it costs them now. Aim for five to ten candidates from different angles (a product, a
   service, a tool for the owner themselves, a contribution to something that exists).
3. **Check each candidate cheaply for evidence of need:** forum threads, reviews of existing
   products, support queues, search demand, conversations the owner can have, or the owner's
   own experience stated as such.
4. **Choose one with the owner, with evidence** (`decisions.md`): the criteria come from what
   the owner brings and wants, written before candidates are scored.
5. **Continue as for an idea**, from §What it takes.

## What it takes

Before deciding how, work out what it takes to make the idea happen. Give each point its
source:

- **Need.** Who has the problem, how often, and what it costs them now.
- **What exists.** Products, open-source projects, research and earlier attempts: what to build
  on (use, extend or contribute to, wherever that reaches the objective sooner), what to learn
  from (why earlier attempts stalled), and where this idea stands apart.
- **The difference.** Why people with the need would choose it, in their terms.
- **Cost.** To build (time, money, agent use) and to run each month at the target size. For a
  physical product: the bill of materials at the planned quantity, certification, tooling, and
  the price people would pay (`physical.md §Parts, suppliers and lead times`).
- **Funding routes, several at once.** The owner's own time and money, pre-orders or
  crowdfunding, revenue (with every assumption stated), grants and competitions, sponsorship,
  partners, an employer, contributors, and phasing so each stage pays for or proves the next.
  Work out the runway at the planned spend.
- **Reach.** How the first ten and the first hundred people will hear of it, get it and start
  using it.
- **What success needs.** A need people have; a result that does the job; a way for them to
  find and get it; money for building and running; a person or agent for every stage; feedback
  coming in; and the drive that keeps it moving. Each gap becomes work in the plan, never a
  verdict on the idea.
- **The path.** The route that fits the owner's resources, its first step, and for each
  constraint the routes around it and what each costs. A large idea gets a staged path; a small
  budget gets a route that fits it. The owner chooses the route; you bring the evidence and the
  arithmetic.

Show every number with its units and inputs (`planning.md §Estimates and arithmetic`). Send the
owner the path as one message with a recommendation.

Failures this prevents: nobody worked out what it takes, so the project runs out of money, time
or direction halfway; the first option found became the plan; complexity arrived before the
need; only engineering was considered.

## Objective, outcomes and measures

- **One objective:** a change in the world, for named people. "Revolutionise gardening with
  AI" cannot be met, missed or measured; "allotment holders water only when the soil needs it,
  saving a visit a week" can.
- **Three to five measures,** each with what is measured, the target, the date, and how it is
  taken (the benchmark, the log query, the invoice, the meter, the survey). A measure nobody
  can take is not a measure.
- **The journeys that must never fail** (§Journeys and threads).
- **Acceptance criteria** for each deliverable: concrete, checkable, and agreed with the
  acceptor.
- **Milestones** that each leave something a person can use and name the measures they move
  (`planning.md §Milestones as usable slices`).
- **Every measure is served by something, and everything serves a measure.** A milestone that
  moves no measure, or a measure nothing moves, is a finding.
- **Switch conditions** for the routes (§Alternative routes).
- With no records yet, write the smallest set this work needs: the objective, and the measure
  the current work moves.

## Alternative routes

- **The objective stands; the route changes.** For each route the plan depends on (a channel,
  a supplier, a design, a funding route), write the measurable condition that means it is not
  working and the route it switches to.
- **At every review, evaluate each condition with today's numbers.** When one is met, switch
  now and record the switch.
- **A blocked route with no written alternative gets the next route found** (`decisions.md`) and
  recorded.
- **Nothing is declared impossible, and no project is declared dead.** Money, time, physics,
  law and skills are constraints, and a constraint has routes around it. Say honestly what each
  costs and how long it takes. A quiet launch, a lost supplier or a missed measure is evidence
  about a route, never a verdict on the idea.

## Areas and owners

For every area the product needs, record an owner (the owner, a person, an agent or a
service), the first deliverable and the measure it serves, or one line on why it does not
apply:

- **Product:** objective, measures, scope.
- **Research:** evidence of need, and how feedback keeps arriving.
- **Design:** people and situations, journeys, states, words, one system of look and behaviour,
  operability by people and agents (`design.md`).
- **Engineering:** software, firmware, electronics, mechanics, data, construction.
- **Quality:** what proves each journey on each platform or environment (`quality.md`).
- **Security and privacy:** a threat model in five lines; what personal data, where it goes,
  how it is deleted; and the project's own confidentiality (`confidentiality.md`).
- **Operations:** hosting or running, monitoring, backups, support, incidents
  (`operations.md`).
- **Supply,** for anything physical: bill of materials, second sources, lead times, assembly,
  test jigs, packaging, returns (`physical.md`).
- **Legal:** licences, terms, privacy notice, certification (radio, electrical, safety,
  medical, food), contracts, and a company and tax where money is taken.
- **Finance:** costs, price, funding routes, runway, who pays each bill.
- **Distribution:** where people find it, get it and start it (§Releasing to people).
- **Support and community:** how people get help, and how what they say reaches the plan
  (§Hearing back).

An area nobody named is not reported as broken; it is not reported at all, and a report that
is silent about it reads exactly like one that checked it. A radio device needs certification;
one that records where people are needs a privacy notice; one that costs money to run needs
someone paying. These shape the design, so they are founded at the start.

## Journeys and threads

- **List the three to five journeys that must never fail,** in the words of the person doing
  them ("a member books a free slot on a phone and gets a confirmation").
- **Thread each one through every area:** one table per journey, one row per step, recording
  what the person does, what they see or hear, the component or procedure that handles it, the
  data or record written, the evidence that proves it (a test, an inspection, a rehearsal), and
  the measure it moves. An empty cell is a gap in the design. For a service or physical
  delivery the "component" is the procedure, person or equipment that handles the step.
- The threads keep the flow, the architecture and the data one design rather than three
  (`design.md §Threads to the architecture`).

## Requests, however they are worded

Owners ask in the words they have: "it feels slow", "make it scalable", "clean it up", "more
modern", "prettier", "add AI". The request is where the owner's view and the builder's meet,
and neither can see the other's side.

1. **Keep the request word for word, and split it into its claims.** "Slow, old-fashioned,
   doesn't scale, add AI" is four claims; handle each one.
2. **Translate each claim into its measurable meanings:**
   - "Slow": which journey, on which device, measured how (a page load on a phone, a query, a
     build, a start-up, a battery charge, a delivery time)?
   - "Scalable": more of what (people, data, requests, contributors, sites, units)?
   - "Modern": which failing of what exists (its look, what it runs on, a missed update)?
   - "Prettier", "more intuitive", "cleaner": which journey, for whom, and where do people
     hesitate, err or give up? Task success, time and errors on that journey, with people
     (`design.md §Taste and evidence`); a look the owner wants is their call between rendered
     options.
   - "AI": which job, for whom, and what is done today instead?
3. **Map each meaning to an existing measure, journey or requirement, or to none.**
4. **Show the owner the current state before changing anything:** one short paragraph per claim
   with the current value, the target, and what that means. ("The booking page takes 6.1 s to
   load on a mid-range phone on 4G. The target is 2 s. 2.4 MB of the page is one photograph.")
   Often this ends the request.
5. **Find the cause before choosing the change:** profile, trace, weigh the page, read the query
   plan, meter the current, time the process. Optimising what is easy instead of what is slow,
   and building the buzzword (a queue for "scalable", a rewrite for "modern", an unused model
   call for "AI"), are the failures this prevents.
6. **Account for every claim.** Each ends as one of four, and none as a bare no:
   - **changed**, with the value before and after;
   - **already meets its target**, with the number, and the improvement that matters instead,
     found from where the owner's feeling comes from;
   - **the owner's call**: a proposed new measure, what it would take and cost, asked once; when
     the owner is away, recorded as a proposal while the measured parts continue;
   - **redirected**: the decision it would have broken, and the route that got the owner what
     they wanted.
7. **Build each change as SKILL.md §7 says,** and record a translation table: claim, meaning,
   measure, value before, target, action, value after, evidence.

## Releasing to people

A result can pass every check and still reach nobody. Reaching people is part of delivery,
planned from the start. (For a service or creative output, the release is the delivery to the
client or audience: `service.md`.)

1. **Plan the release in the records:** which people this release is for, which measures it
   should move (people who find it, who start it, who finish the first journey, who come back),
   which channels, by when, and for each channel the condition that switches it to the next
   route.
2. **Walk every way in, as a stranger, from a clean device.** For each platform: from each place
   people find it (a search result, a store listing, a link in a post, a registry, a shop shelf)
   through getting it, installing or setting it up, and starting it, to the first journey done.
   Use a device or account that has never seen the product: no saved settings, no signed-in
   session, no cached files, no builder's tools. A step that fails blocks the release. Then
   have someone new do it with no help, and watch.
3. **Make everything that is not the product true, before release day:**
   - listings, descriptions and pictures show what it does now, in its people's words;
   - prices, payment and refunds work end to end, tested with a real small payment;
   - terms and the privacy notice say what the product actually does with data, checked against
     the code and a network log, not against intentions;
   - licences and certifications are in hand before it ships;
   - each item has an owner and a check.
4. **Stage it:** a small share of people or devices first, the critical journeys watched, a pause
   that triggers itself at a failure threshold set in advance, and a rollback that has been tried
   (`software.md §Delivery: review, CI, deploy, rollback`;
   `physical.md §Packaging, shipping, repairs and recalls`).
5. **Tell people where they already are, in their words.** Choose channels from evidence of where
   people with the need gather (communities, newsletters, shops, clubs, events, search, stores,
   word of mouth). Use more than one at once, each with its own measure. Say what it does for
   them, not what it is built with. An announcement, a price or anything sent to people is an
   action outside the working environment: within the standing limits, or with the owner's yes.
6. **A confidential project is released privately,** to the people its classes allow, through
   channels that keep it there (`confidentiality.md`).
7. **Measure after the planned period,** each measure from its source; switch any channel whose
   condition fired; record what was learned.

## Hearing back

- **A help route people can find** from inside the product and from each place they meet it,
  answered within a stated time by a person, or by an agent with a person behind it.
- **Every message, review, report and incident is mapped** to a journey or a measure. A request
  that maps to nothing goes to the owner as a proposed new measure, not onto a backlog as
  unexplained work.
- **A question asked twice becomes a change** to the product or its words, not a longer help page.
- **At each milestone, people new to the product walk the critical journeys with no help;**
  record success, time and where they got stuck (`design.md §Testing with people`).
