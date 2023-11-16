import ormar
from uuid import UUID
from database import BaseMeta


class itens(ormar.Model):
    class Meta(BaseMeta):
        tablename = "itens"

    id: UUID = ormar.UUID(primary_key=True, editable=False)
    date: datetime = ormar.DateTime()
    total_amount: float = ormar.Float()