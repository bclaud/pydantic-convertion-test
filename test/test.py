#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p "python3.withPackages(ps: [ ps.pydantic ps.pytest])"

from typing import Annotated
from pydantic import AfterValidator, BaseModel
from decimal import Decimal, ROUND_UP
from test_data import cents_to_reais_data, reais_to_cents_data

def normalize_to_reais(v: int) -> float:
    assert v > 0, f'{v} must be a positive amount'
    reais = float((Decimal(v) / Decimal(100)).quantize(Decimal('0.01'), rounding=ROUND_UP))
    return reais

def normalize_to_cents(v: float) -> int:
    assert v > 0.00, f'{v} must be a positive amount'
    cents = int((Decimal(v) * Decimal(100)).quantize(Decimal('0.01'), rounding=ROUND_UP))

    return cents

Cents = Annotated[float, AfterValidator(normalize_to_cents)]
Reais = Annotated[float, AfterValidator(normalize_to_reais)]


class IncomingPayload(BaseModel):
    amount: Cents

class OutgoingPayload(BaseModel):
    amount: Reais

import pytest

def test_incoming_payload():
    amount_in_reais = 10.00
    incoming_payload = IncomingPayload(amount=amount_in_reais)
    assert incoming_payload.amount == 1000

def test_outgoing_payload():
    amount_in_cents = 1000
    outgoing_payload = OutgoingPayload(amount=amount_in_cents)
    assert outgoing_payload.amount == 10.00

@pytest.mark.parametrize('cents, expected_reais', cents_to_reais_data)
def test_normalize_to_reais(cents, expected_reais):
    outgoing_payload = OutgoingPayload(amount=cents)

    assert outgoing_payload.amount == expected_reais

@pytest.mark.parametrize('reais, expected_cents', reais_to_cents_data)
def test_normalize_to_cents(reais, expected_cents):
    incoming_payload = IncomingPayload(amount=reais)
    assert incoming_payload.amount == expected_cents


if __name__ == '__main__':
    pytest.main([__file__])
