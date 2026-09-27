#!/bin/sh
# Run a command with every file system read-only except one writable directory, in a private
# mount namespace (util-linux unshare). Nothing it changes outside that directory can persist.
#
#   sh contain.sh <writable-dir> <command> [args...]
#
# Verified on 2026-09-27: writes to /, /tmp, /root, /home and /Users were refused and a write
# inside the directory succeeded (docs/trials/protocol.md, amendment 3).
dir=$(cd "$1" && pwd) || exit 2; shift
exec unshare -m --propagation private sh -c '
  dir=$1; shift
  mount --bind "$dir" "$dir" || exit 3
  for m in $(findmnt -rn -o TARGET | grep -v -e "^/proc" -e "^/sys" -e "^/dev" | sort -r); do
    mount -o remount,bind,ro "$m" 2>/dev/null
  done
  mount -o remount,bind,rw "$dir" || exit 3
  cd "$dir" && exec "$@"
' contain "$dir" "$@"
