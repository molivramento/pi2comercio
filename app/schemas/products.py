from app.models.products import Product

ProductIn = Product.get_pydantic(
    exclude={
        "id"
    }
)

