import requests


product_id = input('What is the product id to delete?')
try:
    product_id = int(product_id)
except:
    print('invalid product id')

endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"

get_response = requests.delete(endpoint)
print(get_response.status_code)
