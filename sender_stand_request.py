
import requests
import data
from configuration import URL_SERVICE, KITS_PATH, CREATE_USER_PATH


def post_new_client_kit(kit_body):
    token = get_new_user_token()
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {token}"
    response = requests.post(f"{URL_SERVICE}{KITS_PATH}", json=kit_body, headers=headers)
    return response

def get_new_user_token():
    url = f"{URL_SERVICE}{CREATE_USER_PATH}"
    headers = data.headers.copy()
    user_body = data.get_user_body()

    response = requests.post(url, headers=headers, json=user_body)
    response.raise_for_status()
    return response.json()["authToken"]