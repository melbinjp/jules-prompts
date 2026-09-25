# Machine bookings for the Eastside Woodshop

A worked example of a ledger, small on purpose. Every row below has an ID, every decision in
`decisions/` says which IDs it serves and what backs it, and every commit says what it serves
and how it was verified, in `Serves:` and `Verified:` lines. `python check_trace.py --root .`
passes on it.

## Goal

| id | the change in the world |
|---|---|
| G1 | Members book the bandsaw, lathe and planer themselves, without the group-chat scramble or two people turning up for one machine. |

## Who it is for, and the evidence they need it

Sixty members, most on phones, a third over sixty. The shop's chat had 41 booking messages
and 3 double bookings in August 2026 (the chat export, counted). They use a shared paper
sheet and the chat today. Alternatives checked: a shared calendar (tried in 2025, abandoned:
anyone could delete anyone's slot), and three booking products at £20 to £45 a month, more
than the shop's whole software budget.

## Success measures

| id | what | target | by | how it is measured |
|---|---|---|---|---|
| M1 | double bookings | 0 a month | 2027-01-31 | the booking log, every overlapping pair counted |
| M2 | bookings made without asking for help | 90% | 2027-01-31 | help messages in the chat against bookings in the log |
| M3 | running cost | £5 a month or less | from launch | the hosting invoice |

## Journeys that must never fail

| id | journey |
|---|---|
| J1 | A member books a free slot on a phone and gets a confirmation. |
| J2 | A member cancels, and the slot is free again for everyone at once. |

## Resources

| id | resource | source |
|---|---|---|
| R1 | hosting | D0002 |
| R2 | the member list | owned: the shop's existing membership spreadsheet |

## Funding

Built by a member for free; running cost paid from the shop's £60 a year software budget,
which M3 keeps it inside.

## Change course

The goal stands. When a condition is measured, the project switches to the route it names.

| id | condition | then |
|---|---|---|
| K1 | fewer than 20 bookings a month by 2027-03-31 | ask ten members what stops them, and fix what they name first, starting with the booking flow on a phone |
| K2 | the Pi down for more than a day | move to the £4 cloud instance from the nightly backup (D0002's fallback) |

## Operating model

Every stage is a command in this repository, so a person, an agent or CI can run it.

| stage | command | run by |
|---|---|---|
| test | `make test` | CI on every push; a person or an agent before pushing |
| release | `make release` | a person |
| back up | `make backup` | nightly timer; restored once a month by a person |

## Milestones

| id | what a person can use when it is done | moves |
|---|---|---|
| MS1 | The bandsaw is bookable end to end, used by five members for two weeks. | M1, M2 |
| MS2 | Every machine, cancellations and reminders. | M1, M2, M3 |
