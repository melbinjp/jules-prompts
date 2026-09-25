---
id: D0002
status: accepted
serves: [M3]
door: two-way
revisit: when the shop's internet has two or more outages in a month
decided: 2026-09-12
---
# Host on the Raspberry Pi already in the shop

## Options

- A small cloud instance at £4 a month.
- The shop's Raspberry Pi 4, behind a free tunnel.

## Evidence

- Measured: 60 MB of memory and under 2% of one core at 30 bookings an hour.
- Calculation: the £4 instance is £48 a year; the Pi the shop already runs costs nothing extra.

## Decision

The Pi. If the shop's connection proves unreliable, the £4 instance is the fallback.
