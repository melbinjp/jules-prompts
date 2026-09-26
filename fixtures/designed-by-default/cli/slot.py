"""slot: the command line the reminder agent uses each evening.

    slot list DATE
    slot book PHONE SLOT
"""
import sys

sys.path.insert(0, "server")
import store  # noqa: E402


def main(argv):
    command = argv[1]
    if command == "list":
        rows = store.db.execute("SELECT slot, first_name, last_name, phone FROM bookings "
                                "WHERE slot LIKE ?", (argv[2] + "%",)).fetchall()
        print(f"{'SLOT':<18}{'PATIENT':<28}PHONE")
        for slot, first, last, phone in rows:
            print(f"{slot:<18}{first + ' ' + last:<28}{phone}")
    elif command == "book":
        store.create({"phone": argv[2], "slot": argv[3]})
        print("booked")
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv)
