---
id: D0001
status: accepted
serves: [M1, J1, J2]
door: one-way
approved_by: R. Okafor, shop secretary
revisit: when there are more than 50 bookings a day, or two servers are needed
decided: 2026-09-12
---
# Store bookings in one SQLite file

## Question

Where do bookings live, so that two people can never hold the same slot?

## Options

- The shared calendar the shop already has: no way to stop an overlapping event (tried in 2025).
- A hosted Postgres: correct, and £7 to £15 a month, over the M3 budget on its own.
- One SQLite file beside the app, with a unique index on (machine, slot).

## Evidence

- Calculation: 60 members, at most 30 bookings a day, is 11,000 rows a year; SQLite's
  documented limits are many orders above that.
- Measured: 200 concurrent booking attempts for one slot against the unique index gave
  exactly 1 success and 199 clean refusals (tests/test_race.py, run 20 times).

## Decision

SQLite, with the unique index doing the refusing, not application code.

## Exit

- Moving to Postgres is a schema dump and a changed connection string; the app reaches the
  database through one module, `store.py`. Estimated at a day's work.
