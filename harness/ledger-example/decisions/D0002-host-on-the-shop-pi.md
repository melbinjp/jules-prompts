---
id: D0002
status: accepted
serves: [M3]
door: two-way
revisit: when the shop's internet has two outages in a month
decided: 2026-09-12
---
# Host on the Raspberry Pi already in the shop

## Options

- A small cloud instance at £4 a month.
- The Raspberry Pi 4 that already runs the shop's door sensor, behind a free tunnel.

## Evidence

- Measured: the app at 30 bookings an hour uses 60 MB of memory and under 2% of one core on
  the Pi (a one-hour load test, `make load`).

## Decision

The Pi, costing nothing. The nightly backup goes off the Pi to the shop's cloud drive, so
losing the Pi loses at most a day.
