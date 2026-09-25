---
id: D0002
status: accepted
serves: [M3, M1]
door: two-way
revisit: when the Pi passes 50% CPU at the busiest hour, or bookings pass 50 a day
decided: 2026-09-12
---
# Run as one process on the Raspberry Pi already in the shop

## Options

- A small cloud instance at £4 a month.
- The shop's Raspberry Pi 4, one process, behind a free tunnel.

## Evidence

- Measured: a one-hour load test at 30 bookings an hour used 60 MB and under 2% of one core.
- One process means one writer to the SQLite file and one place where availability is
  decided, which is what keeps M1 at zero without locking between services.

## Decision

One process on the Pi. Nothing else to run, pay for or keep in step.
