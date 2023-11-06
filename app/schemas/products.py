import json

from pydantic import BaseModel

from app.models.products import Product


class ProductIn(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    img: str = None

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value
