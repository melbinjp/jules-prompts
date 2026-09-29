**The script did not do what it claimed. It logged "backup done" every night while producing 20-byte empty files, and I have rewritten it so it can no longer do that.** The fix is tested only against stand-in commands in Docker, not against the real database, backup server or cron.

What was wrong:
1. `pg_dump appointments | gzip` takes gzip's exit status, so a failed dump still produces an empty gzip (20 bytes) (NOTES.md).
2. `scp ... || true` hides a failed copy (scripts/backup.sh).
3. `echo "backup done"` runs whatever happened (logs/backup.log).
4. `rm -f appointments-*.sql.gz` runs before the new dump, so one bad night deletes every local copy.
5. The dump fails under cron with "password authentication failed for user surgery", so no real backup has been made since the failures began (logs/backup.log).
6. Nothing checks size or gzip validity (RUNBOOK.md step 2 says at least 50 MB), and nothing compares the copy's size on the server (step 4).
7. The script and cron.txt had CRLF line endings; a CRLF shebang fails on Linux. Converted to LF.

Changes: scripts/backup.sh rewritten to dump to a temp file and check the dump's exit status, refuse files under 50 MB, run gzip -t, copy to the server and compare the remote size, prune old local copies only after success, log timestamped OK or FAILED and exit 1 on any failure. It does not hold a password, so the sign-in problem in item 5 is untouched.

Tests in Docker with fake pg_dump, scp and ssh: authentication failure, empty dump, scp refused, remote file 20 bytes vs local 678391, missing backup directory all exit 1 with a FAILED line; success exits 0 and prunes only the 30-day-old file. The previous good local file was kept in every failure case.

Not verified: anything against the real database, backup server or cron; whether a good backup exists anywhere (the last three server files are empty; someone should check for older good files and put the password in ~/.pgpass for the cron user).

Counts: 7 verified, 0 failed, 3 not verified, 0 not applicable of 10 items.
