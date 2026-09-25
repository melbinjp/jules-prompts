# Machine bookings for the Eastside Woodshop

## Goal

| id | the change in the world |
|---|---|
| G1 | Members book the bandsaw, lathe and planer themselves, without the group-chat scramble or two people turning up for one machine. |

## Success measures

| id | what | target | by | how it is measured |
|---|---|---|---|---|
| M1 | double bookings | 0 a month | 2027-01-31 | the booking log, every overlapping pair counted |
| M2 | bookings made without asking for help | 90% | 2027-01-31 | help messages in the chat against bookings in the log |
| M3 | running cost | £5 a month or less | from launch | the hosting invoice |
| M4 | booking page ready on a phone | 2 s or less | 2026-12-31 | `make pageload`: a mid-range phone profile on throttled 4G, median of 5 |

## Journeys that must never fail

| id | journey |
|---|---|
| J1 | A member books a free slot on a phone and gets a confirmation. |
| J2 | A member cancels, and the slot is free again for everyone at once. |
| J3 | The evening before, a member is reminded of tomorrow's booking. |

## Change course

The goal stands. When a condition is measured, the project switches to the route it names.

| id | condition | then |
|---|---|---|
| K1 | fewer than 20 bookings a month by 2027-03-31 | ask ten members what stops them, and fix what they name first |

## Milestones

| id | what a person can use when it is done | moves |
|---|---|---|
| MS1 | Every machine bookable and cancellable, with reminders. Done 2026-10-20. | M1, M2, M3 |
| MS2 | The booking page fast on members' phones. | M4 |

## Measurements

Taken 2026-11-02, before the change described in `CHANGES.md`.

- Availability query: 4 ms at the 95th percentile over 1,000 requests (`bench/availability.txt`).
- Booking page: 6.1 s to ready, median of 5 (`bench/pageload.txt`). 2.6 MB transferred,
  2.4 MB of it `static/hero.jpg`, shown 360 px wide.
- Load: 38 bookings a day at the busiest. The Pi at 1% CPU and 58 MB of memory.
