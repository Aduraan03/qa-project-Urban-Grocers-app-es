# data.py
def get_user_body():
    return {
        "firstName": "Max",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
    }

def get_kit_body(name):
    return {
    "Content-Type": "application/json"
    }

# Datos de prueba para la creación de kits
kit_data = {
    "name": "Kit de prueba"
}

updated_kit_data = {
    "name": "Kit actualizado"
}

