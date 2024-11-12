# Datos de usuario
def get_user_body():
    return {
        "firstName": "Max",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
    }

# Headers sin Authorization, se agrega dinámicamente en el código
headers = {
    "Content-Type": "application/json"
}

# Función para obtener el cuerpo del kit
def get_kit_body(name):
    return {
        "name": name
    }

# Datos de prueba para los kits
one_letter = "a"
special_chars = "№%@"
name_with_spaces = " A Aaa "
name_with_numbers = "123"
empty_name = ""
no_name = None
non_string_name = 123
