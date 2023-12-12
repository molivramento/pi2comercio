from app.models.places import Place
from uuid import UUID
from typing import Optional
from pydantic import BaseModel

PlaceIn = Place.get_pydantic(
  exclude = {
    'uuid'
  }
)


class PlaceFilter(BaseModel):
  uuid: Optional[UUID]
  name: Optional[str]
