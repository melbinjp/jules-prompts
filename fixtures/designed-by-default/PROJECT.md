# Slot: appointments for Riverside Physio

## Goal

| id | the change in the world |
|---|---|
| G1 | Patients book, move and cancel their own appointments, so the front desk stops spending its mornings on the phone. |

## Success measures

| id | what | target | by | how it is measured |
|---|---|---|---|---|
| M1 | first-time patients who finish a first booking unaided within 3 minutes | 80% | 2026-12-31 | the booking funnel in `metrics/first-booking.csv`, weekly |
| M2 | booking calls to the desk | half of July's 140 a week | 2027-03-31 | the desk's call log |
| M3 | missed appointments rebooked within a day | 90% | 2026-12-31 | the reminder agent's log |

## Journeys that must never fail

| id | journey |
|---|---|
| J1 | A first-time patient books an appointment on a phone. |
| J2 | A patient cancels, and can take it back if they tapped by mistake. |
| J3 | A missed appointment is rebooked by the reminder agent, within the clinic's rules. |

## Rules the owner set

- A patient holds at most two upcoming appointments, so nobody block-books the Monday evening slots. (Dr A. Mensah, 2026-06-02)

## Journey thread: J1

| step | the person does | they see | handled by | data written | proved by | moves |
|---|---|---|---|---|---|---|
| 1 | chooses a time | the free times this week | `web/book.html`, `GET /slots` | nothing | `tests/test_slots.py` | M1 |
| 2 | gives name, phone and date of birth | a short form | `web/book.html`, `POST /bookings` | a booking | `tests/test_book.py` | M1 |
| 3 | sees it confirmed | the time, the address, how to cancel | `web/book.html` | nothing | `tests/test_book.py` | M1, M2 |

## Operating model

| stage | who runs it | how |
|---|---|---|
| booking | the patient | the web app |
| front desk | the receptionist | the web app |
| rebooking missed appointments | the reminder agent (a local model) | `cli/slot.py`, every evening at 18:00 |
| release | the owner | `make release` |
