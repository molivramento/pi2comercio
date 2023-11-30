import ormar
from ormar import fields
from uuid import UUID
from database import BaseMeta
from app.models.products import Product
from app.models.transaction import Transaction
from typing import Optional

class items(ormar.Model):
    class Meta(BaseMeta):
        tablename = "items"

    uuid: UUID = ormar.UUID(primary_key=True, editable=False, unique=True)
    total_amount: int = ormar.Integer()
    product: Optional[Product] = ormar.ForeignKey(Product)
    transaction: Optional[Transaction] = fields.ForeignKey(Transaction, related_name='itens')
