from typing import Optional
from pydantic import BaseModel

from app.models.itens import Itens
from app.schemas.base import BaseFilter

itensIN = Itens.get_pydantic(
    exclude={
        "uuid",
    }
)


class itensFilter(BaseFilter):
    total_amount: Optional[float] = None
    date: Optional[date] = None
    transation_id: Optional[str] = None
    produto_id: Optional[str] = None
    quantidade: Optional[int] = None
