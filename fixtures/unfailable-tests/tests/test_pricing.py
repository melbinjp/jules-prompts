"""Tests an agent wrote while looking at pricing.py."""
from unittest.mock import patch

import pricing


def test_discount_returns_something():
    # Shape assertion. Survives every real defect in discount().
    result = pricing.discount(100.0, 10.0)
    assert result is not None


def test_discount_is_called():
    # Mocks the unit under test. Passes on an empty implementation.
    with patch.object(pricing, "discount", return_value=90.0) as mocked:
        assert mocked(100.0, 10.0) == 90.0
        mocked.assert_called_once()


def test_discount_formula():
    # Expected value reconstructed from the implementation, including its bug.
    price, percent = 100.0, 10.0
    expected = price * (1 - percent / 10)
    assert pricing.discount(price, percent) == expected


def test_discount_does_not_raise():
    pricing.discount(100.0, 10.0)


def test_zero_percent_leaves_price():
    # Control: this one can fail. Mutating the body to `return 0` turns it red.
    assert pricing.discount(100.0, 0.0) == 100.0
