from pantry.api.schemas import PriceView
from pantry.db import connection


def reprice_offers(discount):
    with connection() as db:
        db.execute("UPDATE prices SET price = price * %s WHERE on_offer", (1 - discount,))
        rows = db.execute("SELECT sku, price, on_offer FROM prices WHERE on_offer").fetchall()
    return [PriceView(*row) for row in rows]
