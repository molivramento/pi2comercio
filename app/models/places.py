import ormar
from uuid import UUID
from database import BaseMeta


class Place(ormar.Model):
  class Meta(BaseMeta):
    tablename = 'places'
  
  uuid: UUID = ormar.UUID(primary_key=True, editable=False)
  name: str = ormar.String(max_length=64)
  