def create_product(client):
    payload = {'name': 'test', 'description': 'test', 'price': 1.55, 'quantity': 2, 'img': 'test'}
    return client.post('/products/', json=payload)
