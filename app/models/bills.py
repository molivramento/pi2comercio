from datetime import date
from typing import Union
from uuid import UUID

import ormar

from app.models.financial_resources import BankAccount, CreditCard, Wallet
from database import BaseMeta


class Bill(ormar.Model):
    class Meta(BaseMeta):
        tablename = "bills"

    uuid: UUID = ormar.UUID(primary_key=True, editable=False)
    name: str = ormar.String(max_length=128)
    business_name: str = ormar.String(max_length=128)
    Febraban_code: str = ormar.String(max_length=128, unique=True)
    description: str = ormar.String(max_length=255, nullable=True, server_default=None)
    qr_code: str = ormar.String(max_length=128, nullable=True, server_default=None)
    amount: float = ormar.Float()
    due_date: date = ormar.Date()
    is_paid: bool = ormar.Boolean(default=False)
    payment_date: date = ormar.Date(nullable=True, server_default=None)
