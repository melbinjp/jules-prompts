---
id: D0005
status: accepted
serves: [M3, M1]
door: two-way
revisit: when SafeBox's free tier changes, or the backup passes 1 GB
decided: 2026-09-20
---
# Nightly backups to SafeBox's free tier

## Options

- SafeBox, free up to 2 GB.
- A USB drive in the shop, rotated by the secretary each week.

## Evidence

- Measured: the whole database, compressed, is 3 MB; a year of bookings at the planned rate
  stays under 50 MB.

## Decision

SafeBox, nightly, with a restore check on the first Saturday of each month.
