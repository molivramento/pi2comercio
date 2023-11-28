import ormar
from uuid import UUID
from database import BaseMeta


class Transation(ormar.Model):
    class Meta(BaseMeta):
        tablename = "transation"

    uuid: UUID = ormar.UUID(primary_key=True, editable=False, unique=True)
    date: date = ormar.DateTime()
    total_amount: float = ormar.Float()
