# Fixture: designed-by-default

Skill: `design-the-experience`. Prompt: `task_design_the_experience`.

Slot books physiotherapy appointments for a small clinic. Patients book on their phones, the
receptionist works at the desk, and a reminder agent reschedules missed appointments through the
command line. It has a ledger (`PROJECT.md`, `decisions/`), a design note (`DESIGN.md`), a
usability study (`research/`), the first-booking numbers (`metrics/`), and the code.

It was redesigned in August and looks tidy. Nine things about how it was designed mean the
people it is for, and the agent that works beside them, cannot do the job it exists for as well
as the ledger says they can.

The empty state of the bookings list (`web/list.html`) is designed right. It is the control.

```bash
python scripts/score_fixture.py fixtures/designed-by-default REPORT.md
python scripts/score_fixture.py fixtures/designed-by-default --self-check
```
