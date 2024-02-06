import ormar
from ormar import fields
from uuid import UUID
from database import BaseMeta
from app.models.products import Products
from app.models.transaction import Transaction
from typing import Optional

class items(ormar.Model):
    class Meta(BaseMeta):
        tablename = "items"

    uuid: UUID = ormar.UUID(primary_key=True, editable=False, unique=True)
    total_amount: int = ormar.Integer()
    product: Optional[Products] = ormar.ForeignKey(Products)
    transaction: Optional[Transaction] = fields.ForeignKey(Transaction, related_name='itens')
