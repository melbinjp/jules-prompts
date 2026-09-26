"""The one place billing talks to the payment provider. Tests pass a FakeGateway instead."""
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Receipt:
    invoice_id: int
    amount: Decimal


class SandboxGateway:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def charge(self, invoice_id: int, amount: Decimal) -> Receipt:
        raise NotImplementedError("calls the provider's API")


class FakeGateway:
    """Records every charge and returns a receipt for exactly what was asked."""

    def __init__(self):
        self.charges = []

    def charge(self, invoice_id: int, amount: Decimal) -> Receipt:
        self.charges.append((invoice_id, amount))
        return Receipt(invoice_id, amount)
