"""Copies every booking into the shop's Google Calendar (D0003)."""
import os

import store
from google_calendar import Calendar

calendar = Calendar(os.environ["SHOP_CALENDAR_ID"], key_file=os.environ["GOOGLE_KEY_FILE"])

for machine, day, slot, member in store.connect().execute("SELECT * FROM bookings"):
    calendar.upsert(f"{machine} {day} {slot}", title=f"{member}: {machine}", day=day, hour=slot)
