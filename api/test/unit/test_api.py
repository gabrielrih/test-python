import os
import sys

from fastapi.testclient import TestClient

HERE = os.path.dirname(os.path.realpath(__file__))
root_path = f'{HERE}/../../..'
sys.path.insert(0, root_path)

from api.main import app

client = TestClient(app)
def test_get_one_device():
    device_id = 1
    expected_status_code = 200
    expected_body = {
        "id": "1",
        "name": "device one",
        "hardware_version": "1.5.6",
        "software_version": "0.0.1"
    }
    response = client.get(f"/devices/{device_id}")
    assert response.status_code == expected_status_code
    assert response.json() == expected_body

def test_get_one_device_not_found():
    device_id = 10
    expected_status_code = 404
    response = client.get(f"/devices/{device_id}")
    assert response.status_code == expected_status_code

def test_get_all_devices():
    expected_status_code = 200
    expected_body = {
        "1": {
            "id": "1",
            "name": "device one",
            "hardware_version": "1.5.6",
            "software_version": "0.0.1"
        },
        "2": {
            "id": "2",
            "name": "device two",
            "hardware_version": "1.5.6",
            "software_version": "0.0.1"
        },
        "3": {
            "id": "3",
            "name": "device three",
            "hardware_version": "1.5.6",
            "software_version": "0.0.1"
        },
    }
    response = client.get(f"/devices")
    assert response.status_code == expected_status_code
    assert response.json() == expected_body

def test_create_device_with_id():
    expected_status_code = 201
    body = {
        "id": "12345678910",
        "name": "device created",
        "hardware_version": "1.5.6",
        "software_version": "0.0.1"
    }
    response = client.post("/devices", json=body)
    assert response.status_code == expected_status_code
    assert response.json() == body

def test_create_device_without_id():
    expected_status_code = 201
    body = {
        "name": "device created",
        "hardware_version": "1.5.6",
        "software_version": "0.0.1"
    }
    response = client.post("/devices", json=body)
    assert response.status_code == expected_status_code
    assert response.json() != None
