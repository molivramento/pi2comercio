from uuid import UUID
from typing import Optional
from pydantic import BaseModel

from app.models.products import Product

ProductIn = Product.get_pydantic(
    exclude={
        "id"
    }
)


class ProductUniqueField(BaseModel):
    name: str


class GetProduct(BaseModel):
    id: Optional[UUID] = None
    name: Optional[str] = None
    name__icontains: Optional[str] = None
    description__icontains: Optional[str] = None
    price__gte: Optional[float] = None
    price__lte: Optional[float] = None
    quantity__gte: Optional[int] = None
    quantity__lte: Optional[int] = None


# Multipart data and file
# class ProductIn(BaseModel):
#     id: Optional[UUID] = None
#     name: str
#     description: str
#     price: float
#     quantity: int
#     img: Optional[str] = None
#
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate_to_json
#
#     @classmethod
#     def validate_to_json(cls, v):
#         if isinstance(v, str):
#             return cls(**json.loads(v))
#         return v


