import importlib

import yaml

from pantry.db import connection

with open("config/plugins.yaml") as handle:
    PLUGINS = yaml.safe_load(handle)

payment = importlib.import_module(PLUGINS["payment_adapter"])


def place_order(order):
    with connection() as db:
        total = sum(line["price"] * line["qty"] for line in order["lines"])
        db.execute("INSERT INTO orders (customer_id, total) VALUES (%s, %s)", (order["customer"], total))
    return payment.charge(order["customer"], total)
