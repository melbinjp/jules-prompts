"""Confirmation and reminder emails. Times are shown in the shop's time zone."""
from datetime import datetime
from zoneinfo import ZoneInfo

SHOP = ZoneInfo("Europe/London")


def when(day, slot):
    """'Sat 7 Nov, 14:00', in the shop's time, whatever the server's clock is set to."""
    start = datetime.fromisoformat(f"{day}T{slot:02d}:00").replace(tzinfo=SHOP)
    return start.strftime("%a %-d %b, %H:%M")


def confirm(member, machine, day, slot):
    return send(member, f"Booked: the {machine}, {when(day, slot)}")


def remind(member, machine, day, slot, still_free):
    return send(member, f"Tomorrow: the {machine}, {when(day, slot)}")


def send(to, subject):
    print(f"to {to}: {subject}")
    return subject
