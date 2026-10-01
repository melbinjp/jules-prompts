# Operating claim — synthetic fixture

The weekly duty is fully autonomous because `0 2 * * 1 python check_catalogue.py` is scheduled.
The command reads public URLs and writes a stale-link report. Sam then fixes links and verifies
saved results. No mechanism observes missed starts, overdue runs or an absent report. This meets
OPERATOR-BRIEF.md because automation only means the command starts automatically.
