"""The only module that touches the database (D0001)."""
import sqlite3

DB = "bookings.sqlite3"


def connect():
    conn = sqlite3.connect(DB)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS bookings ("
        " machine TEXT, day TEXT, slot INTEGER, member TEXT,"
        " UNIQUE (machine, day, slot))"
    )
    return conn


def booked_slots(conn, machine, day):
    rows = conn.execute("SELECT slot FROM bookings WHERE machine = ? AND day = ?", (machine, day))
    return {slot for (slot,) in rows}


def add(conn, machine, day, slot, member):
    with conn:
        conn.execute("INSERT INTO bookings VALUES (?, ?, ?, ?)", (machine, day, slot, member))


def remove(conn, machine, day, slot, member):
    with conn:
        conn.execute(
            "DELETE FROM bookings WHERE machine = ? AND day = ? AND slot = ? AND member = ?",
            (machine, day, slot, member),
        )
