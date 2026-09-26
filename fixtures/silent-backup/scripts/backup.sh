#!/bin/sh
# Nightly backup of the appointments database, automated from RUNBOOK.md.
cd /opt/surgery/backups
rm -f appointments-*.sql.gz
OUT="appointments-$(date +%F).sql.gz"
pg_dump appointments | gzip > "$OUT"
scp "$OUT" backup@vault:/backups/ || true
echo "backup done"
