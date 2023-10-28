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
