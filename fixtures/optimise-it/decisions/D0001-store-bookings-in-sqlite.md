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

## Options

- The shared calendar the shop already has: nothing stops an overlapping event.
- A hosted Postgres: £7 to £15 a month, over M3 on its own.
- One SQLite file beside the app, with a unique index on (machine, slot).

## Evidence

- Calculation: at most 50 bookings a day is 18,000 rows a year, far inside SQLite's limits.
- Measured: 200 concurrent attempts on one slot gave exactly 1 booking and 199 refusals.

## Decision

SQLite, with the unique index doing the refusing, through `store.py` alone.

## Exit

- Postgres is a schema dump and a new connection string behind `store.py`: about a day.
