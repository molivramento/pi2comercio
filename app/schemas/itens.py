from uuid import UUID
from typing import Optional
from pydantic import BaseModel

from app.models.itens import itens

itenIn = itens.get_pydantic(
    exclude={
        "uuid"
    }
)


class itenFilter(BaseModel):
    product: Optional[dict] = {'uuid': None}
    transaction: Optional[dict] = {'uuid': None}
    total_amount: Optional[int] = None