#!/bin/sh
# Runner check: list the files changed outside the allowed places since a marker was touched.
#
#   touch MARK; <run the agent>; sh outside.sh MARK <allowed-dir>...
#
# Pass the run's own directory and the agent's transcript directory as allowed. System temp files
# and caches are still listed: the runner judges each line and records the judgement.
mark=$1; shift
prune="-path /proc -o -path /sys -o -path /dev -o -path /run -o -path /root/.claude -o -path /var/log"
for d in "$@"; do prune="$prune -o -path $d"; done
find / \( $prune \) -prune -o -type f -newer "$mark" -print 2>/dev/null
