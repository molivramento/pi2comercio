from typing import Optional
from uuid import UUID

from fastapi import Query
from pydantic import BaseModel


class BaseFilter(BaseModel):
    uuid: Optional[UUID] = None
