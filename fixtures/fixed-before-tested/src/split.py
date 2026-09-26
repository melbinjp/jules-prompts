"""Splitting a bill between people."""
from decimal import Decimal, ROUND_DOWN


def split_bill(total: Decimal, people: int) -> list[Decimal]:
    """Shares that add up to the total exactly; the leftover pennies go one each to the first people."""
    base = (total / people).quantize(Decimal("0.01"), rounding=ROUND_DOWN)
    leftover = int((total - base * people) / Decimal("0.01"))
    return [base + Decimal("0.01") if i < leftover else base for i in range(people)]
