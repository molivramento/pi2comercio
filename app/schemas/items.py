from uuid import UUID
from typing import Optional
from pydantic import BaseModel

from app.models.items import items

itenIn = items.get_pydantic(
    exclude={
        "uuid"
    }
)


class itenFilter(BaseModel):
    product: str = None
    transaction: str = None
    total_amount: Optional[int] = 1000