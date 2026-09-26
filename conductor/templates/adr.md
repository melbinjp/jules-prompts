# Decision record (ADR) template

One file per decision, numbered in order (`0001-store-bookings-in-sqlite.md`), kept where the
project keeps its documents (often `docs/decisions/`). The layout follows MADR (Markdown
Architectural Decision Records); the review checklist is in `../guidance/decisions.md §Recording
and superseding decisions`.

```markdown
# <short title, as the decision>

- Status: <proposed | accepted | rejected | deprecated | superseded by NNNN>
- Date: <YYYY-MM-DD>
- Decided by: <name; the approver, for a decision that is costly to reverse>
- Serves: <the objective, measure, journey, requirement or constraint it exists for>
- Costly to reverse: <yes or no, and why in one line>
- Supersedes: <NNNN, if any>

## Question

<The job to be done, not the product: what must be true, for whom, within which limits.>

## Criteria

<Recorded before any option was scored. Hard limits as pass or fail; the rest with weights, each
taken from a named measure, journey, constraint or risk.>

## Options

- <Doing nothing, or keeping what exists>
- <Using or configuring what the project already has>
- <Building or making it>
- <Each serious thing to buy or use>
- <Combinations>

## Evidence

Each item starts with its kind: Measured, Calculation, Simulation, Proof, Prototype, Test or
Source. At least two, at least one run, worked out or built; two different kinds if costly to
reverse.

- <Kind>: <what was found, with units, and where it can be checked>

## Decision

<What was chosen: one option, a portfolio, a sequence with its switch condition, or a timed
experiment. The seam that keeps it reversible. The assumption that would flip it.>

## Exit

<What leaving would cost, and how it would be done. Required if costly to reverse.>

## Reopen when

<The measurable condition that reopens it: a measure, a price, a date, a count of incidents.>
```

## A filled example

```markdown
# Store bookings in one SQLite file

- Status: accepted
- Date: 2026-09-12
- Decided by: R. Okafor, shop secretary
- Serves: no double bookings (0 a month by 2027-01-31); members book a slot on a phone; the
  journey "a member cancels and the slot is free again at once"
- Costly to reverse: yes; it holds every booking, and the identifiers others will depend on
- Supersedes: none

## Question

Where do bookings live, so that two people can never hold the same slot, within £5 a month?

## Criteria

- Hard limits: never two bookings for one machine and slot; running cost within £5 a month.
- Weighted: effort to operate for a volunteer (50%); effort to move away later (30%); time to
  build (20%).

## Options

- The shared calendar the shop already has: no way to stop an overlapping event (tried in 2025).
- A hosted Postgres: correct, and £7 to £15 a month, over the budget on its own.
- One SQLite file beside the app, with a unique index on (machine, slot).

## Evidence

- Calculation: 60 members, at most 30 bookings a day, is 11,000 rows a year; SQLite's documented
  limits are many orders above that.
- Measured: 200 concurrent booking attempts for one slot against the unique index gave exactly 1
  success and 199 clean refusals (tests/test_race.py, run 20 times).
- Source: the hosting price lists for the two Postgres providers considered, checked 2026-09-10.

## Decision

SQLite, with the unique index doing the refusing, not application code. The app reaches the
database through one module, `store.py`, which is the seam. It would flip if bookings needed more
than one server writing at once.

## Exit

Moving to Postgres is a schema dump and a changed connection string behind `store.py`; estimated
at a day's work.

## Reopen when

There are more than 50 bookings a day, or two servers are needed.
```
