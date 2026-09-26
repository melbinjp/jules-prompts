from decimal import Decimal

from src.split import split_bill


def test_split_is_even():
    assert split_bill(Decimal("9.00"), 3) == [Decimal("3.00")] * 3


def test_split_one_person():
    assert split_bill(Decimal("12.40"), 1) == [Decimal("12.40")]
