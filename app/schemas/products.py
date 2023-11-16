from uuid import UUID
from typing import Optional
from pydantic import BaseModel

from app.models.products import Product
from app.schemas.base import BaseFilter

ProductIn = Product.get_pydantic(
    exclude={
        "uuid"
    }
)


class ProductFilter(BaseFilter):
    name: Optional[str] = None
    name__icontains: Optional[str] = None
    description__icontains: Optional[str] = None
    price__gte: Optional[float] = None
    price__lte: Optional[float] = None
    quantity__gte: Optional[int] = None
    quantity__lte: Optional[int] = None
