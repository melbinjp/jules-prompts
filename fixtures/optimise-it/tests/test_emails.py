import os
import time

import emails


def test_confirmation_uses_the_shop_time_even_when_the_server_is_on_utc():
    os.environ["TZ"] = "UTC"
    time.tzset()
    # The bug was times converted to the server's UTC: an hour early all summer. June is on
    # British Summer Time and November is not, so this fails if either season is wrong.
    assert emails.when("2026-06-20", 14) == "Sat 20 Jun, 14:00"
    assert emails.when("2026-11-07", 14) == "Sat 7 Nov, 14:00"
