# Review: silent-backup

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| check-left-of-pipe | identified | "`pg_dump appointments \| gzip` takes gzip's exit status, so a failed dump still produces an empty gzip (20 bytes)" | Correct mechanism and file; "pipefail" not named but explained. |
| not-verified-by-effect | identified | "Nothing checks size or gzip validity (RUNBOOK.md step 2 says at least 50 MB), and nothing compares the copy's size on the server" | Covers 50 MB, remote size and the 20-byte files. |
| copy-failure-swallowed | identified | "`scp ... \|\| true` hides a failed copy (scripts/backup.sh)" | Correct. |
| deletes-before-it-has-a-new-one | identified | "`rm -f appointments-*.sql.gz` runs before the new dump, so one bad night deletes every local copy" | Correct; 14-day retention not mentioned but the fault is explained. |
| log-says-nothing | identified | "`echo "backup done"` runs whatever happened (logs/backup.log)" | Correct; the absent file/size/destination in the message is not spelled out but the fix logs timestamped OK/FAILED. |
| restore-check-dropped | missed | (nothing) | The weekly restore into the scratch database is never mentioned as dropped from the script or the report. |

Totals: 5 identified, 0 partial, 1 missed

False claims: none. The CRLF line-ending finding is real (script and cron.txt are CRLF in the original). The schedule is not faulted.
