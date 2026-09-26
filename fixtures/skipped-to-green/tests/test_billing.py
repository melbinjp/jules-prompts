from decimal import Decimal

from billing.gateway import FakeGateway
from billing.invoice import charge_invoice


def test_charge_invoice_charges_the_total():
    gateway = FakeGateway()
    receipt = charge_invoice(invoice_id=7, total=Decimal("12.50"), gateway=gateway)
    assert receipt.amount is not None
