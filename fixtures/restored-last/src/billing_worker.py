"""Charges each subscriber for the month. Runs every morning from 09:00."""
import payments

TIMEOUT = 2  # seconds; was 30 before 2.14


def charge(subscriber):
    for attempt in range(3):
        try:
            return payments.create_charge(subscriber.customer_id, subscriber.amount, timeout=TIMEOUT)
        except payments.Timeout:
            continue  # the provider may still have taken the payment
    raise RuntimeError("charge failed after 3 attempts")
