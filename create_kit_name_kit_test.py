import pytest
from sender_stand_request import  post_new_client_kit
import data



# Pruebas positivas
def test_kit_name_1_char():
    response = post_new_client_kit(data.get_kit_body(data.one_letter))
    assert response.status_code == 201
    assert response.json()["name"] == data.one_letter

def test_kit_name_511_chars():
    name = "a" * 511
    response = post_new_client_kit(data.get_kit_body(name))
    assert response.status_code == 201
    assert response.json()["name"] == name

def test_kit_name_special_chars():
    name = "№%@"
    response = post_new_client_kit(data.get_kit_body(data.special_chars))
    assert response.status_code == 201
    assert response.json()["name"] == data.special_chars

def test_kit_name_with_spaces():
    name = " A Aaa "
    response = post_new_client_kit(data.get_kit_body(data.name_with_spaces))
    assert response.status_code == 201
    assert response.json()["name"] == data.name_with_spaces

def test_kit_name_with_numbers():
    name = "123"
    response = post_new_client_kit(data.get_kit_body(data.name_with_numbers))
    assert response.status_code == 201
    assert response.json()["name"] == data.name_with_numbers

# Pruebas negativas
def test_kit_name_empty():
    response = post_new_client_kit(data.get_kit_body(data.empty_name))
    assert response.status_code == 400

def test_kit_name_exceeds_512_chars():
    name = "a" * 512
    response = post_new_client_kit(data.get_kit_body(name))
    assert response.status_code == 400

def test_kit_name_not_passed():
    kit_body = data.get_kit_body(data.no_name)
    response = post_new_client_kit(kit_body)
    assert response.status_code == 400

def test_kit_name_different_type():
    response = post_new_client_kit(data.get_kit_body(data.non_string_name))
    assert response.status_code == 400

