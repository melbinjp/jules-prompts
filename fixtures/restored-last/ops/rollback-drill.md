# Rollback drill, 2026-09-18

Rolled production back from 2.13 to 2.12 with `make rollback VERSION=2.12`, then forward again.
Time from command to all journeys passing their checks: 2 minutes 10 seconds. The billing worker
drains its queue and restarts cleanly on the previous version. Next drill: 2026-10-16.
