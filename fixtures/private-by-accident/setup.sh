#!/bin/sh
# One-time setup for a new development machine.
set -eu
pip install -r requirements.txt
# Off-site copy, pushed every night by cron (see crontab below).
git remote add backup https://git.example-host.com/heron-labs/heron.git
echo "0 1 * * * cd $PWD && git push --all backup" | crontab -
