# The migration copy

Every night at 03:00 the latest production backup is restored to `pg-copy`, a separate
PostgreSQL 15.8 host with the same settings as production. Row counts match production as of
the backup. Use it for anything that must be measured before it meets real data:
`psql "$PG_COPY_URL"`. It is rebuilt from scratch each night, so nothing done there survives.
