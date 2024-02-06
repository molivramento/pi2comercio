import requests

url = "https://api.pagar.me/core/v5/orders/"

payload = {
    "customer": {
        "name": "David Vinicius Do Nascimento Bezerra",
        "email": "david.bezerra@ufrpe.br"
    },
    "items": [
        {
            "amount": 1990,
            "description": "Chaveiro do Tesseract",
            "quantity": "1"
        }
    ],
    "closed": "false",
    "poi_payment_settings": {
        "visible": "true",
        "print_order_receipt": "false",
        "devices_serial_number": ["123456789"],
    "payment_setup": {
          "type": "credit",
          "installments": 1,
          "installment_type": "merchant"
    },
    "display_name": "Pedido #1"
    }
}

headers = {
    "accept": "application/json",
    "ServiceRefererName": "64d67ba05a4d5d6d0d6a43f5",
    "Authorization": "Basic c2tfbnhMMm94bWMxaFk3WHJENzo=",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers, verify=True)

print(response.text)