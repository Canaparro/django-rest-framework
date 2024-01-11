import json
import requests
from getpass import getpass

endpoint = "http://127.0.0.1:8000/api/products/"

auth_endpoint = "http://127.0.0.1:8000/api/auth/"

password = getpass()

auth_response = requests.post(
    auth_endpoint, json={"username": "admin", "password": password}
)
if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    print(token)
    headers = {"Authorization": f"Bearer {token}"}
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
