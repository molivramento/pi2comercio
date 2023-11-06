from uuid import uuid4

from fastapi.testclient import TestClient
from tests.products.utils import create_product


class TestProduct:
    def test_create_product(self, client: TestClient) -> None:
        response = create_product(client)
        assert response.status_code == 200
        assert response.json()['name'] == 'test'
        assert response.json()['description'] == 'test'
        assert response.json()['price'] == 1.55
        assert response.json()['quantity'] == 2

    def test_get_all_products(self, client: TestClient) -> None:
        create_product(client)
        response = client.get('/products/')
        assert response.status_code == 200
        assert len(response.json()) == 1

    def test_get_product_by_id(self, client: TestClient) -> None:
        product = create_product(client).json()
        pk = product['id']
        response = client.get(f'/products/{pk}')
        assert response.status_code == 200
        assert response.json()['name'] == 'test'
        assert response.json()['description'] == 'test'
        assert response.json()['price'] == 1.55
        assert response.json()['quantity'] == 2

    def test_get_product_by_name(self, client: TestClient) -> None:
        create_product(client)
        response = client.get('/products/name/test')
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]['name'] == 'test'
        assert response.json()[0]['description'] == 'test'
        assert response.json()[0]['price'] == 1.55
        assert response.json()[0]['quantity'] == 2

    def test_update_products(self, client: TestClient) -> None:
        product = create_product(client).json()
        product['name'] = 'test modified'
        response = client.put('/products/', json=product)
        assert response.status_code == 200
        assert response.json()['name'] == 'test modified'
        assert response.json()['description'] == 'test'

    def test_delete_product(self, client: TestClient) -> None:
        product = create_product(client).json()
        pk = product['id']
        response = client.delete(f'/products/{pk}')
        assert response.status_code == 200

    def test_delete_product_not_found(self, client: TestClient) -> None:
        response = client.delete(f'/products/{uuid4()}')
        assert response.status_code == 404
        assert response.json()['detail'] == 'Product not found'

    def test_get_product_by_id_not_found(self, client: TestClient) -> None:
        response = client.get(f'/products/{uuid4()}')
        assert response.status_code == 404
        assert response.json()['detail'] == 'Product not found'

    def test_get_product_by_name_not_found(self, client: TestClient) -> None:
        response = client.get('/products/name/not_found')
        assert response.status_code == 404
        assert response.json()['detail'] == 'Product not found'

    def test_update_product_not_found(self, client: TestClient) -> None:
        product = create_product(client).json()
        product['id'] = str(uuid4())
        response = client.put('/products/', json=product)
        assert response.status_code == 404
        assert response.json()['detail'] == 'Product not found'
