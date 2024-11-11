import pytest
from sender_stand_request import create_kit, get_kit, update_kit, delete_kit, post_new_client_kit
from data import get_kit_body, kit_data, updated_kit_data



# Pruebas positivas
def test_kit_name_1_char():
    response = post_new_client_kit(get_kit_body("a"))
    assert response.status_code == 201
    assert response.json()["name"] == "a"

def test_kit_name_511_chars():
    name = "a" * 511
    response = post_new_client_kit(get_kit_body(name))
    assert response.status_code == 201
    assert response.json()["name"] == name

def test_kit_name_special_chars():
    name = "№%@"
    response = post_new_client_kit(get_kit_body(name))
    assert response.status_code == 201
    assert response.json()["name"] == name

def test_kit_name_with_spaces():
    name = " A Aaa "
    response = post_new_client_kit(get_kit_body(name))
    assert response.status_code == 201
    assert response.json()["name"] == name

def test_kit_name_with_numbers():
    name = "123"
    response = post_new_client_kit(get_kit_body(name))
    assert response.status_code == 201
    assert response.json()["name"] == name

# Pruebas negativas
def test_kit_name_empty():
    response = post_new_client_kit(get_kit_body(""))
    assert response.status_code == 400

def test_kit_name_exceeds_512_chars():
    name = "a" * 512
    response = post_new_client_kit(get_kit_body(name))
    assert response.status_code == 400

def test_kit_name_not_passed():
    response = post_new_client_kit({})
    assert response.status_code == 400

def test_kit_name_different_type():
    response = post_new_client_kit(get_kit_body(123))
    assert response.status_code == 400

