import ormar
from uuid import UUID
from database import BaseMeta


class Product(ormar.Model):
    class Meta(BaseMeta):
        tablename = "products"

    id: UUID = ormar.UUID(primary_key=True, editable=False)
    name: str = ormar.String(max_length=64, unique=True)
    description: str = ormar.String(max_length=256)
    price: float = ormar.Float()
    quantity: int = ormar.Integer()
    img: str = ormar.String(max_length=256, nullable=True)
