# Machine bookings for the Eastside Woodshop

## Goal

| id | the change in the world |
|---|---|
| G1 | Members book the bandsaw, lathe and planer themselves, without the group-chat scramble or two people turning up for one machine. |

## Success measures

| id | what | target | by | how it is measured |
|---|---|---|---|---|
| M1 | double bookings | 0 a month | 2027-01-31 | `logs/double-bookings.txt`: every overlapping pair in the booking log |
| M2 | bookings made without asking for help | 90% | 2027-01-31 | `logs/help-and-bookings.txt`: help messages in the chat against bookings |
| M3 | running cost | £5 a month or less | from launch | `invoices/`: every bill for the month |

## Journeys that must never fail

| id | journey |
|---|---|
| J1 | A member books a free slot on a phone and gets a confirmation. |
| J2 | A member cancels, and the slot is free again for everyone at once. |
| J3 | The evening before, a member is reminded of tomorrow's booking. |

## Resources

| id | resource | source |
|---|---|---|
| R1 | hosting | D0002 |
| R2 | off-site backup storage | D0005 |

## Stop or change course

| id | condition | then |
|---|---|---|
| K1 | fewer than 20 bookings a month by 2027-03-31 | stop, export the bookings, go back to the paper sheet |

## Operating model

Every stage is a command in this repository, so a person, an agent or CI can run it.

| stage | command | run by |
|---|---|---|
| test | `make test` | CI on every push; a person or an agent before pushing |
| release | `make release` | a person, or the maintenance agent |
| back up | `make backup` | nightly, from `crontab` |
| restore | `make restore-check` | a person, on the first Saturday of each month |

## Milestones

| id | what a person can use when it is done | moves |
|---|---|---|
| MS1 | Every machine bookable and cancellable. Done 2026-10-20. | M1, M2, M3 |
| MS2 | Reminder emails the evening before. Done 2026-12-01. | M2 |
| MS3 | A members' help page, from the questions asked in the chat. | M2 |
