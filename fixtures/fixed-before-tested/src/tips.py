"""Splitting the tip between people."""
from decimal import Decimal, ROUND_HALF_UP


def split_tip(tip: Decimal, people: int) -> list[Decimal]:
    share = (tip / people).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return [share] * people
