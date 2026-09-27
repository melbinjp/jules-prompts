#!/bin/sh
# Runner check before a run: list absolute paths, hosts and devices named in a workspace, so a
# hard-coded target outside it is known before any code there runs.
#
#   sh paths.sh <workspace>
grep -rnoE --exclude-dir=.git --exclude-dir=node_modules \
  '(/(Users|home|root|etc|var|opt|mnt|media|srv|dev)/[A-Za-z0-9._/-]+|https?://[A-Za-z0-9.-]+|[0-9]{1,3}(\.[0-9]{1,3}){3}(:[0-9]+)?)' \
  "$1" 2>/dev/null | sort -u
