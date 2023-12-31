from uuid import uuid4

from fastapi.testclient import TestClient

products = {'name': 'test',
            'description': 'test',
            'price': 1.55,
            'quantity': 2,
            'img': 'static/products/default.png'}


class TestProduct:
    def test_create_product(self, client: TestClient) -> None:
        response = client.post('/products/', json=products)
        assert response.status_code == 200
        assert response.json()['name'] == 'test'
        assert response.json()['description'] == 'test'
        assert response.json()['price'] == 1.55
        assert response.json()['quantity'] == 2

    def test_get_all_products(self, client: TestClient) -> None:
        client.post('/products/', json=products)
        response = client.get('/products/')
        assert response.status_code == 200
        assert len(response.json()) == 1

    def test_get_product_by_uuid(self, client: TestClient) -> None:
        product = client.post('/products/', json=products).json()
        uuid = product['uuid']
        response = client.get(f'/products/?uuid={uuid}')
        assert response.status_code == 200
        assert response.json()[0]['name'] == 'test'
        assert response.json()[0]['description'] == 'test'
        assert response.json()[0]['price'] == 1.55
        assert response.json()[0]['quantity'] == 2

    def test_get_product_by_name(self, client: TestClient) -> None:
        client.post('/products/', json=products)
        response = client.get(f'/products/?name=test')
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]['name'] == 'test'
        assert response.json()[0]['description'] == 'test'
        assert response.json()[0]['price'] == 1.55
        assert response.json()[0]['quantity'] == 2

    def test_update_products(self, client: TestClient) -> None:
        product = client.post('/products/', json=products).json()
        product['name'] = 'test modified'
        response = client.put(f'/products/', json=product)
        assert response.status_code == 200
        assert response.json()['name'] == 'test modified'
        assert response.json()['description'] == 'test'

    def test_delete_product(self, client: TestClient) -> None:
        product = client.post('/products/', json=products).json()
        uuid = product['uuid']
        response = client.delete(f'/products/{uuid}')
        assert response.status_code == 200

    def test_delete_product_not_found(self, client: TestClient) -> None:
        response = client.delete(f'/products/{uuid4()}')
        assert response.status_code == 404

    def test_get_product_by_id_not_found(self, client: TestClient) -> None:
        response = client.get(f'/products/?uuid={uuid4()}')
        assert response.status_code == 200
        assert response.json() == []

    def test_get_product_by_name_not_found(self, client: TestClient) -> None:
        response = client.get('/products/?name=error')
        assert response.status_code == 200
        assert response.json() == []

    def test_update_product_not_found(self, client: TestClient) -> None:
        product = client.post('/products/', json=products).json()
        product['uuid'] = str(uuid4())
        response = client.put(f'/products', json=product)
        assert response.status_code == 404
