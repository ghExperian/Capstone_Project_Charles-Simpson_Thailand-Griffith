from fastapi.testclient import TestClient

from src.backend.main import app

client = TestClient(app)

HEADERS = {"x-api-key": "thailand&charlesdeserveagoodgrade"}


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Climate Change API is running"}


def test_get_all_data():
    response = client.get("/data", headers=HEADERS)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_data():
    new_data = {
        "country": "Testland",
        "month": "January",
        "element": "Temperature",
        "year": 2026,
        "value": 25.5,
    }

    response = client.post("/data", json=new_data, headers=HEADERS)

    assert response.status_code == 200
    assert response.json()["message"] == "Data added successfully"


def test_get_data_by_country_found():
    new_data = {
        "country": "Testland",
        "month": "January",
        "element": "Temperature",
        "year": 2026,
        "value": 25.5,
    }

    client.post("/data", json=new_data, headers=HEADERS)
    response = client.get("/data/Testland", headers=HEADERS)

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["country"] == "Testland"


def test_get_data_by_country_not_found():
    response = client.get("/data/UnknownCountry123", headers=HEADERS)

    assert response.status_code == 404
    assert response.json()["detail"] == "Country not found"


def test_add_data_missing_field():
    bad_data = {
        "country": "Testland",
        "month": "January",
        "element": "Temperature",
        "year": 2026,
    }

    response = client.post("/data", json=bad_data, headers=HEADERS)

    assert response.status_code == 422


def test_add_data_wrong_type():
    bad_data = {
        "country": "Testland",
        "month": "January",
        "element": "Temperature",
        "year": "wrong",
        "value": 25.5,
    }

    response = client.post("/data", json=bad_data, headers=HEADERS)

    assert response.status_code == 422


def test_delete_data_not_found():
    response = client.delete("/data/999999", headers=HEADERS)

    assert response.status_code == 404
    assert response.json()["detail"] == "Data not found"


def test_data_response_has_required_keys():
    response = client.get("/data", headers=HEADERS)

    assert response.status_code == 200

    data = response.json()

    if data:
        row = data[0]
        assert "id" in row
        assert "country" in row
        assert "month" in row
        assert "element" in row
        assert "year" in row
        assert "value" in row


def test_country_endpoint_limit():
    response = client.get("/data/Testland", headers=HEADERS)

    if response.status_code == 200:
        assert len(response.json()) <= 10000
    else:
        assert response.status_code == 404
