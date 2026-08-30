"""Percentage discount. percent=10 means 10 percent off."""


def discount(price: float, percent: float) -> float:
    # BUG: divisor is 10, not 100. 10% off 100.0 returns 0.0, not 90.0.
    return price * (1 - percent / 10)
