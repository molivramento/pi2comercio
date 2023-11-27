import ormar
from uuid import UUID
from database import BaseMeta


class Products(ormar.Model):
    class Meta(BaseMeta):
        tablename = "products"

    uuid: UUID = ormar.UUID(primary_key=True, editable=False)
    name: str = ormar.String(max_length=64, unique=True)
    description: str = ormar.Text()
    price: float = ormar.Float()
    quantity: int = ormar.Integer()
    img: str = ormar.String(max_length=256, server_default=f'static/products/default.png')
