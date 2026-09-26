from dataclasses import dataclass
from decimal import Decimal


@dataclass
class PriceView:
    sku: str
    price: Decimal
    on_offer: bool
