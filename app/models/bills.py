import ormar
from uuid import UUID
from datetime import date
from database import BaseMeta
from enum import Enum


class Bill(ormar.Model):
    class Meta(BaseMeta):
        tablename = "bills"

    uuid: UUID = ormar.UUID(primary_key=True, editable=False)
    reference: str = ormar.String(max_length=128)
    business: str = ormar.String(max_length=128)
    value: float = ormar.Float()
    febraban: str = ormar.String(max_length=128, nullable=True, server_default=None)
    description: str = ormar.String(max_length=255, nullable=True, server_default=None)
    due_date: date = ormar.Date()
    is_paid: bool = ormar.Boolean(default=False)
    payment_method: str = ormar.String(max_length=128, nullable=True, server_default=None)
    payment_date: date = ormar.Date(nullable=True, server_default=None)
