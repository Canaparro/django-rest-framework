import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/products/1/update/"


data = {
    'title': 'Hello world my old friend!',
    'price': 13.99
}
get_response = requests.put(endpoint, json=data)
print(get_response.json())
