from app.products.models import Product

ProductIn = Product.get_pydantic(
    exclude={
        "id"
    }
)
