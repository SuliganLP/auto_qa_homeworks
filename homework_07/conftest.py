import pytest

from api.auth_api import AuthApi


@pytest.fixture
def booking_data():
    return {
        "firstname": "Alexander",
        "lastname": "Suligan",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-09-01",
            "checkout": "2026-09-10"
        },
        "additionalneeds": "Breakfast"
    }


@pytest.fixture
def auth_token():
    auth_api = AuthApi()

    response = auth_api.create_token()

    assert response.status_code == 200

    token = response.json()["token"]

    return token
