# Nightly backup, by hand

1. `pg_dump appointments | gzip > appointments-YYYY-MM-DD.sql.gz`
2. Check the file is at least 50 MB (the database is about 380 MB; compressed, about 70 MB).
3. Copy it to the backup server: `scp appointments-*.sql.gz backup@vault:/backups/`
4. Check it arrived with the same size: `ssh backup@vault ls -l /backups/`
5. Once a week, restore last night's file into the scratch database and open one patient's
   appointments. A backup nobody has restored is not a backup.
6. Keep 14 days on the backup server; delete older ones there by hand.
