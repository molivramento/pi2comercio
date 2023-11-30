import ormar
from uuid import UUID
from database import BaseMeta
from datetime import datetime, date
from sqlalchemy import func, text



class Transaction(ormar.Model):
    class Meta(BaseMeta):
        tablename = "transaction"

    uuid: UUID = ormar.UUID(primary_key=True, editable=False, unique=True)
    date: date = ormar.DateTime(server_default=func.now())
