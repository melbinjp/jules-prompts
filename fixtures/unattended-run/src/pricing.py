"""Shelf prices from supplier costs and Sam's margin rules."""
from decimal import ROUND_HALF_UP, Decimal

from src import store


def shelf_price(cost, margin):
    price = Decimal(str(cost)) * (1 + Decimal(str(margin)))
    return price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def price_all(products, margins):
    prices = {p["sku"]: str(shelf_price(p["cost"], margins[p["category"]])) for p in products}
    store.save_all(prices)
    return prices
