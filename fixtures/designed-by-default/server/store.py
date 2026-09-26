"""Bookings, in one SQLite file."""
import sqlite3

db = sqlite3.connect("slot.db")
db.execute("""CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY, slot TEXT UNIQUE, first_name TEXT, last_name TEXT, dob TEXT,
    email TEXT, phone TEXT, address TEXT, postcode TEXT, heard_from TEXT, fax TEXT)""")


def create(fields):
    columns = ("slot", "first_name", "last_name", "dob", "email", "phone", "address", "postcode",
               "heard_from", "fax")
    db.execute(f"INSERT INTO bookings ({', '.join(columns)}) VALUES ({', '.join('?' for _ in columns)})",
               [fields.get(c) for c in columns])
    db.commit()


def upcoming(phone):
    return db.execute("SELECT id, slot FROM bookings WHERE phone = ?", (phone,)).fetchall()


def cancel(booking_id):
    # Frees the slot at once so another patient can take it.
    db.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
    db.commit()
