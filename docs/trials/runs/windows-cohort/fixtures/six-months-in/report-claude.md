The booking app is doing its core job, but it misses two of its three targets, and the committee status file was wrong about it. Desk review of the project folder only; code ran in the network-less Docker container.

How it is doing:
- Double bookings: none in Jan, Feb, Mar per logs/double-bookings.txt (not re-derived from the database).
- Use: 212 bookings in March, up 26% since January. The "fewer than 20 a month" switch condition has not fired.
- Booking without asking for help: FAILED. 58% Jan, 61% Feb, 62% Mar against a 90% target due 2027-01-31. Help messages still rising (70 to 81).
- Running cost: FAILED. March £11.83 against a £5 target; the SafeBox free tier ended 2027-01-15. The backup is only about 1 to 3 MB.
- Hosting decision D0002: its reopening condition has fired (February had three internet outages totalling 3 h 50 min; log ends 2027-02-26).
- Backup decision D0005: its reopening condition has fired too, and nobody recorded it.
- Reminder emails: not verified; no code, cron entry or dependency for sending email anywhere in the folder although MS2 says done on 2026-12-01.
- Booking and cancelling: not verified (no app code or booking log in the folder).

Other faults found:
- `make release` pointed at release.sh, renamed to ship.sh on 2027-01-09; run in Docker: exit 127. The maintenance agent had been bypassing make.
- No tests/ directory; `make test` has never had anything to run; the monthly restore check named a test file that did not exist.
- Only one restore check recorded (2026-10-03); five later ones are missing.
- backup.py only copies the database to a local safebox/ folder; nothing uploads anywhere and nothing alerts if a night fails.
- Calendar sync was still scheduled in crontab with code and dependencies present although D0004 said removed.
- STATUS.md said "All measures on track. No incidents", which the evidence contradicts.

Changes made: Makefile release now runs scripts/ship.sh; removed calendar_sync.py, its crontab line and the google-calendar-lite and pandas dependencies; added tests/test_restored.py (needs a restored file); corrected STATUS.md and AGENT_NOTES.md; full record in REVIEW-2027-04.md.

Not checked: make/pytest/ship.sh end to end (no make or pytest in the image, no network); what is running on the Pi.

Next steps: read the 81 March help messages and fix the most common questions; decide the backup (free tier or USB drive) and make it a real off-site backup with a size check and failure alert (needs the owner's yes); test whether reminder emails arrive; run a restore check now; put the Pi's real crontab in the repository; formally reopen D0002 and D0005 with these numbers.

Counts: 3 verified, 2 failed, 5 not verified, 0 not applicable of 10 items.
