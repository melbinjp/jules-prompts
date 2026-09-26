# Decisions: choosing with evidence, and recording it

Load for any choice that matters: a platform, supplier, part, provider, library, venue, design,
route or tool; any decision that would be costly to reverse; and whenever a recorded decision's
reopening condition fires. Decisions are recorded as ADRs (`../templates/adr.md`).

Asked to choose, an agent searches, takes the first result with a free tier, and then writes a
comparison that supports it. It looks researched, and it is a habit with a table attached. The
same failures appear whether the choice is a database, a board, a caterer or a model provider.

## Which decisions need evidence

1. **State the question as the job, not the product.** "Where do 1,000 GB of audio live, so that
   listeners can download 5,000 GB a month for under $60?", not "should we use CloudA?". If the
   question names an answer, the real question is what that answer was meant to do, and it
   becomes one option among several.
2. **Name what it serves:** the objective, a measure, a journey, a requirement or a constraint. A
   choice that serves none of them is not needed; say so and stop.
3. **Set the stakes first, and let them set the effort.** What would a wrong choice cost, and how
   long would it take to reverse?
   - **Costly to reverse** ("a one-way door"): it holds the data or the people; it fixes
     identifiers, a public interface or public URLs; it has lead time or tooling; it is built
     into firmware or hardware in people's hands; it is the language, runtime or platform; it is
     the licence or a name people will learn; it spends money or commits the owner to a person
     or supplier. Make it for the size and shape the objective implies, not only today's.
   - **Cheap to reverse** ("a two-way door"): everything else. Two options, two backings (at
     least one verified by you), and the choice behind a seam. An hour's work, not a week's.
4. **Match the effort to the stakes.** Spending costly-decision effort on a cheap choice is how a
   project spends its budget on trivia; an irreversible choice made quickly is how it ends up
   rebuilt.
5. **Defer what a seam can hold.** Do not make a costly decision before the evidence allows;
   where one module, interface or configuration key can hold it open, defer it and write down
   until when.
6. **Read the earlier decisions this one depends on or contradicts** before starting.

## Options

- **Generate widely before narrowing.** The list includes at least:
  - doing nothing, or keeping what exists;
  - configuring or reusing something the project or owner already has;
  - building or making it (a script, a module, a tool, a circuit, a jig);
  - each serious thing to buy or use, commercial, open-source or community-run;
  - combinations of these.
- **For hardware and parts:** part families, and a second source for each part.
- **No free passes:** include the option the owner suggested and the one found first, and give
  neither a pass.
- **Nothing is excluded for being unusual, large or unfamiliar.** An option is excluded by
  evidence, and the reason is written down.
- **If every option fails a hard limit, the limit is the problem to solve:** find what would
  move it (a funding route, a phased approach, a different design, a tool built for the job) and
  cost that route. The answer is never that the choice cannot be made.
- **Choose one, several, or a sequence:**
  - **one**, when it passes the hard limits and wins clearly on the weighted criteria;
  - **a portfolio**, each option where it is strongest (one place keeps the masters, another
    serves them);
  - **a sequence**: start with one behind a seam, and write now the condition that triggers a
    switch (a measure, a price, a date, a count of incidents) and the plan for switching;
  - **an experiment**, when evidence cannot separate two options and trying is cheap: run both
    for a fixed period, measure them on the criteria, decide on a date set in advance.

## Criteria before scores

1. **Write the criteria and their weights before looking at any candidate, and record them** so
   the order shows in the history.
2. **Take every criterion from something named:** a measure, a journey, a constraint (the budget,
   a licence, a lead time, the skills of whoever will maintain it) or a risk. Popularity, stars,
   "modern" and "developer experience" are easy to score and connected to nothing.
3. **Hard limits** (under the budget, an open licence, available within the lead time) are pass
   or fail, not weights.
4. **Build the comparison table:** options as rows, criteria as columns, each cell with its
   evidence and source, hard limits marked. Never adjust the weights after scoring until the
   favourite wins.

## Evidence

- **Primary sources:** price lists, datasheets, licences, documentation, status and incident
  history, changelogs, open issues that match this use, and the terms on data ownership, export
  and limits. A vendor's claim, a vendor's benchmark, or a vendor's comparison with its
  competitors is marketing until a second source or a measurement agrees.
- **Your own measurement, shaped like the use:** a spike or prototype on the project's own data
  and target hardware; a benchmark at the target scale; a calculation with its units; a
  simulation with its model and assumptions stated. A benchmark on 100 rows says nothing about
  ten million; a laptop on office fibre says nothing about phones on 4G; a demo board on the
  bench says nothing about a field.
- **Label every piece of evidence by its kind:** Measured, Calculation, Simulation, Proof,
  Prototype, Test or Source.
- **Every decision has at least two backings, and at least one is something you ran, worked out
  or built** rather than read.
- **A costly-to-reverse decision needs two different kinds of evidence** (a calculation and a
  measurement; a primary source and a prototype), three or more options, a way out, a reopening
  condition, and the owner's approval. Two articles quoting the same benchmark are one piece of
  evidence.
- **Gather the real numbers:** current and expected usage, sizes and rates, measured wherever
  possible; and find where the choice plugs into the code, circuit or process, which is where
  the seam goes.

## Redo every number

- **Recompute every cost, capacity and rate yourself, with units,** at today's size, at the
  target size and at ten times the target.
- **Look for the usual slips:** gigabytes read as terabytes, a monthly price as a yearly one,
  microamps as milliamps; a term left out (egress, a per-seat fee, a per-request charge, the
  standby current, delivery, tax).
- **Name the term that dominates,** which is often not the headline price.
- **Name the assumption that would flip the decision,** and how far it would have to move.

## A way out and a reopening condition

- **Keep the way out cheap:** put the choice behind a seam (one module, one interface, one
  configuration key, one purchase order); own the identifiers and the data format; keep public
  URLs on a domain the project controls; test an export once.
- **Write the exit down:** what leaving would cost, and how it would be done.
- **Write the condition that reopens it** (a measure, a price, a date, a count of incidents).
  Nothing else reopens it: not a newer article, and not a change of mood.
- **At every review, evaluate each accepted decision's reopening condition** with today's numbers.
  For each that has fired, reopen the decision, or record why it stands, with the number. A
  condition that could never fire is itself a finding: rewrite it.
- **Deferred decisions** are recorded with the seam that holds them open and the condition that
  will close them.
- **Between two close options, take the one that is easier to leave.**

## Recording and superseding decisions

- **One ADR per decision** (`../templates/adr.md`, in MADR form): the question and what it
  serves; whether it is costly to reverse, and why; the criteria; the options; the evidence, each
  labelled by kind; the decision; the exit; the reopening condition; the status (proposed,
  accepted, rejected, deprecated, superseded); who approved it, for a costly one.
- **Number ADRs in order and keep each file's number unique.** A superseded ADR names the ADR that
  replaced it, and the replacement names the one it supersedes.
- **Record a decision before, or with, the change that needs it.**
- **Design decisions are decisions like any other:** the flow chosen, the interaction model, the
  information architecture, the design tokens, the name and the voice. The product's name,
  anything people learn by habit, and a machine interface others will build on are costly to
  reverse; a colour is not.
- **Review checklist for an ADR** (applied by a verifier who is not its author):
  - it states what it serves, and that thing exists in the records;
  - it lists two options, or three or more if it is costly to reverse, including doing nothing,
    building and combining where they apply;
  - it has at least two backings, labelled by kind, at least one verified; two different kinds
    for a costly one;
  - the criteria were recorded before the scoring;
  - the numbers were redone, and the flipping assumption is named;
  - for a costly one: the exit is written and the approver is named;
  - an accepted decision has a reopening condition;
  - a superseded one names a real successor;
  - no current work serves a rejected or superseded decision.

## Asking the owner

- **When the choice needs the owner to pay, sign up, approve or accept a risk, send one message**
  with: the comparison; the recommendation and its cost now and at the target size; the
  runner-up and why it lost; and what happens if they say no.
- **Then stop asking.** A no is a constraint; plan around it. Present the alternatives and the
  cost of each; recommend once, and never nag toward an option.
- **A decision the briefing delegated** is made without asking, within its standing limits, and
  recorded with how to undo it (`autonomy.md §Choices on the owner's behalf`); only what the
  briefing kept for the owner goes to them, and the work carries on meanwhile.
- **For a costly decision, wait for approval where the harness can pause.** Where it cannot,
  record the decision as proposed and do not act on it.
