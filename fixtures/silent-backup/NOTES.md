# Backup automation notes

The last three nightly files on the backup server are each 20 bytes (`ssh backup@vault ls -l`
on 2026-09-25): an empty gzip stream. The script has logged "backup done" every night.
