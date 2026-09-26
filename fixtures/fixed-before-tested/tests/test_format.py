from src.money import format_gbp


def test_format_gbp():
    assert format_gbp(1000.5) == "£1,000.50"
