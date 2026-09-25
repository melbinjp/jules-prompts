"""The booking app: one process on the shop's Pi (D0002)."""
import sqlite3

import availability_client
import emails
import store

SLOTS = range(9, 21)  # one-hour slots, 09:00 to 20:00


def slots_free(machine, day):
    """Free slots, straight from the database."""
    conn = store.connect()
    return [s for s in SLOTS if s not in store.booked_slots(conn, machine, day)]


def booking_page(machine, day):
    free = availability_client.free_slots(machine, day)
    return {"template": "book.html", "machine": machine, "day": day, "free": free}


def book(machine, day, slot, member):
    conn = store.connect()
    try:
        store.add(conn, machine, day, slot, member)
    except sqlite3.IntegrityError:
        return {"ok": False, "message": "Someone booked that slot a moment ago. Pick another."}
    emails.confirm(member, machine, day, slot)
    return {"ok": True}


def cancel(machine, day, slot, member):
    store.remove(store.connect(), machine, day, slot, member)
    return {"ok": True}
