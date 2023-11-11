import json


def create_product(client):
    payload = {'name': 'test', 'description': 'test', 'price': 1.55, 'quantity': 2, 'img': 'static/products/default.png'}
    return client.post('/products/', data={'payload': json.dumps(payload)}, files=None)
