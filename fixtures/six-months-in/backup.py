"""Nightly backup to SafeBox (D0005)."""
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("--restore-to")
args = parser.parse_args()
if args.restore_to:
    shutil.copy("safebox/latest.sqlite3", args.restore_to)
else:
    shutil.copy("bookings.sqlite3", "safebox/latest.sqlite3")
