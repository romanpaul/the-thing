import pytest
import requests

def test_get_scenario_check_status_code_equals_200():
     response = requests.get("http://localhost:5000/api/scenario")
     assert response.status_code == 200

def test_get_character_check_status_code_equals_200():
     response = requests.get("http://localhost:5000/api/character")
     assert response.status_code == 200

def test_get_supply_check_status_code_equals_200():
     response = requests.get("http://localhost:5000/api/supply")
     assert response.status_code == 200

def test_get_tile_check_status_code_equals_200():
     response = requests.get("http://localhost:5000/api/tile2")
     assert response.status_code == 200

def test_get_bloodsample_check_status_code_equals_200():
     response = requests.get("http://localhost:5000/api/bloodsample6")
     assert response.status_code == 200

def test_get_dice_check_status_code_equals_200():
     response = requests.get("http://localhost:5000/api/dice2")
     assert response.status_code == 200

def test_get_scenario_check_content_type_equals_json():
     response = requests.get("http://localhost:5000/api/scenario")
     assert response.headers["Content-Type"] == "application/json"

def test_get_character_check_content_type_equals_json():
     response = requests.get("http://localhost:5000/api/character")
     assert response.headers["Content-Type"] == "application/json"

def test_get_supply_check_content_type_equals_json():
     response = requests.get("http://localhost:5000/api/supply")
     assert response.headers["Content-Type"] == "application/json"

def test_get_tile_check_content_type_equals_json():
     response = requests.get("http://localhost:5000/api/tile3")
     assert response.headers["Content-Type"] == "application/json"

def test_get_bloodsample_check_content_type_equals_json():
     response = requests.get("http://localhost:5000/api/bloodsample7")
     assert response.headers["Content-Type"] == "application/json"

def test_get_dice_check_content_type_equals_json():
     response = requests.get("http://localhost:5000/api/dice3")
     assert response.headers["Content-Type"] == "application/json"