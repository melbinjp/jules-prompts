"""Runs every evening: reminds members of tomorrow's bookings, and lists what is still free."""
import app
import emails
import store

MACHINES = ("bandsaw", "lathe", "planer")


def send_reminders(tomorrow):
    conn = store.connect()
    for machine in MACHINES:
        free = app.slots_free(machine, tomorrow)
        for (slot, member) in conn.execute(
            "SELECT slot, member FROM bookings WHERE machine = ? AND day = ?", (machine, tomorrow)
        ):
            emails.remind(member, machine, tomorrow, slot, still_free=free)
