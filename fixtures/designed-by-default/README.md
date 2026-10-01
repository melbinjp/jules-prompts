# Fixture: designed-by-default

Written for the retired skill `design-the-experience`, whose guidance is now in `conductor/guidance/design.md`.

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

## October 1 extension

The original case and positive control remain. This case now has 11 planted defects; the dated extension adds 2. All new data are synthetic fixture evidence, not observations of a live project or cloud service. The existing request covers the extension; historical trial reports retain their original scope.
