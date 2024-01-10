
import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/products/"

get_response = requests.post(endpoint, json={
                             'title': 'Hello world', 'price': 15.50})
print(get_response.json())
