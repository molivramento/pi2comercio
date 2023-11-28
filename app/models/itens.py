import ormar
from ormar import fields
from uuid import UUID
from database import BaseMeta
from app.models.products import Product
from app.models.transation import Transation
from typing import Optional

class itens(ormar.Model):
    class Meta(BaseMeta):
        tablename = "itens"

    uuid: UUID = ormar.UUID(primary_key=True, editable=False, unique=True)
    total_amount: int = ormar.Integer()
    product: Optional[Product] = ormar.ForeignKey(Product)
    transation: Transation = fields.ForeignKey(Transation, related_name='itens')
