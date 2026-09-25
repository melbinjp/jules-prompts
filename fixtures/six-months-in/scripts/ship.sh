#!/bin/sh
# Renamed from release.sh on 2027-01-09.
set -eu
git pull --ff-only
python -m pytest -q
sudo systemctl restart woodshop
