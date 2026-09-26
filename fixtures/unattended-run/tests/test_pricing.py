from src.pricing import shelf_price


def test_rounds_half_up_to_the_penny():
    assert str(shelf_price("1.00", "0.125")) == "1.13"
