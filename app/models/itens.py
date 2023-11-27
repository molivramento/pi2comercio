import ormar
from uuid import UUID
from database import BaseMeta
from typing import Optional, Union, List
from app.models.products import Products
from app.models.transation import Transation

class Itens(ormar.Model):
    class Meta(BaseMeta):
        tablename = "itens"

    uuid: UUID = ormar.UUID(primary_key=True, editable=False)
    product = ormar.ForeignKey(Products)
    transation = ormar.ForeignKey(Transation)
    quantidade = ormar.Integer()
    preco_unitario = ormar.Float()