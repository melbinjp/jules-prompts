# Expected report for silent-backup

`scripts/backup.sh` automates the runbook's nightly backup and has logged "backup done" every night. `NOTES.md` shows the last three files on the backup server are 20 bytes each. This report checks the script against the runbook, step by step.

## It cannot report a failure

- check-left-of-pipe: `pg_dump appointments | gzip > "$OUT"` runs pg_dump on the left of a pipe with no `set -o pipefail` and no `set -e`. When pg_dump fails, gzip still exits 0 and writes an empty stream. The log shows three nights of "password authentication failed" for user surgery, and every one produced a file.
- copy-failure-swallowed: `scp "$OUT" backup@vault:/backups/ || true` throws away the copy's exit status, so a backup that never reached the vault is reported the same as one that did.
- log-says-nothing: `logs/backup.log` says "backup done" straight after each failure. It names no file, no size and no destination, so a run that did nothing reads exactly like one that worked. Log what was dumped, its size, where it went, and the size that arrived.

## It does not check what it made

- not-verified-by-effect: the runbook checks that the file is at least 50 MB and that it arrived at the vault with the same size. The script checks neither, which is how three files of 20 bytes each were accepted as backups. Check both, and exit non-zero with the reason if either fails.
- restore-check-dropped: the runbook's weekly restore into the scratch database, the only step that proves a backup can be used, is not in the automation, and the script does not say it leaves it out. Automate it, or say plainly that it is still a person's job and who does it.

## It makes a bad night worse

- deletes-before-it-has-a-new-one: `rm -f appointments-*.sql.gz` runs before the new backup exists. An interrupted or failing run leaves the surgery with no local backup at all. The runbook keeps 14 days and only deletes older ones, on the backup server. Delete only after a new backup has been verified, and only past the retention.

Then make it fail on purpose: a wrong password, a full disk, the vault unreachable, a kill halfway. Each must end with a non-zero exit and a log line naming what failed.

The schedule (`cron.txt`) is right: daily at 02:30, the quiet hour, as the manual backup ran, with output appended to the log. It stays.

## Verdicts

| item | evidence | verdict |
|---|---|---|
| each step verified by its effect | no size check, no arrival check | broken |
| each failure reaches the exit code | pg_dump masked by the pipe; scp by `|| true` | broken |
| safe to interrupt | deletes the last backup first | broken |
| safe to run twice | a second run overwrites the day's file with the same name | holds |
| the log says what it read and wrote | "backup done" only | broken |
| what it will not do, stated | the restore check dropped silently | broken |
| the schedule | 02:30 daily, as by hand | holds |
| made to fail on purpose | never | broken |

8 items: 2 holds, 6 broken, 0 skipped.

defect_id: check-left-of-pipe
defect_id: not-verified-by-effect
defect_id: copy-failure-swallowed
defect_id: deletes-before-it-has-a-new-one
defect_id: log-says-nothing
defect_id: restore-check-dropped
