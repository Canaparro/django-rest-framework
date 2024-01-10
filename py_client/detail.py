import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/products/1"

# get_response = requests.post(endpoint, json={'title': 'Hello world'})
get_response = requests.get(endpoint)
# print(get_response.text)
print(get_response.json())
# print(get_response.status_code)
