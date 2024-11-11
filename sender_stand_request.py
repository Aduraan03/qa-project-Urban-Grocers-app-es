import requests
from configuration import URL_SERVICE, CREATE_USER_PATH, KITS_PATH
from data import get_user_body

def get_new_user_token():
    url = f"{URL_SERVICE}{CREATE_USER_PATH}"
    headers = {"Content-Type": "application/json"}
    user_body = get_user_body()  # Asegúrate de que este cuerpo esté bien definido en data.py

    response = requests.post(url, headers=headers, json=user_body)
    response.raise_for_status()  # Verifica que la solicitud sea exitosa
    return response.json().get("authToken")  # Obtén el authToken si la respuesta es exitosa

def post_new_client_kit(kit_body):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(f"{URL_SERVICE}{KITS_PATH}", json=kit_body, headers=headers)
    return response

# Función para crear un nuevo kit (POST)
def create_kit(token, kit_data):
    url = f"{URL_SERVICE}/kits"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, json=kit_data, headers=headers)
    response.raise_for_status()
    return response.json()

# Función para obtener un kit existente (GET)
def get_kit(token, kit_id):
    url = f"{URL_SERVICE}/kits/{kit_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

# Función para actualizar un kit existente (PUT)
def update_kit(token, kit_id, kit_data):
    url = f"{URL_SERVICE}/kits/{kit_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.put(url, json=kit_data, headers=headers)
    response.raise_for_status()
    return response.json()

# Función para eliminar un kit (DELETE)
def delete_kit(token, kit_id):
    url = f"{URL_SERVICE}/kits/{kit_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    return response.status_code  # Código de respuesta: 200 si la eliminación fue exitosa