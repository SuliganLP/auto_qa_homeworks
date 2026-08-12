from api.booking_api import BookingApi


def test_create_booking(booking_data):
    api = BookingApi()

    response = api.create_booking(booking_data)

    assert response.status_code == 200

    response_data = response.json()

    assert "bookingid" in response_data
    assert response_data["booking"] == booking_data


def test_partial_update_booking(booking_data, auth_token):
    api = BookingApi()

    create_response = api.create_booking(booking_data)

    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    update_data = {"firstname": "Alex", "totalprice": 700}

    update_response = api.partial_update_booking(booking_id, update_data, auth_token)

    assert update_response.status_code == 200

    updated_booking = update_response.json()

    assert updated_booking["firstname"] == "Alex"
    assert updated_booking["totalprice"] == 700

    assert (updated_booking["lastname"] == booking_data["lastname"])


def test_delete_booking(booking_data, auth_token):
    api = BookingApi()

    create_response = api.create_booking(booking_data)

    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    delete_response = api.delete_booking(booking_id, auth_token)

    assert delete_response.status_code == 201

    get_response = api.get_booking(booking_id)

    assert get_response.status_code == 404


def test_partial_update_without_auth(booking_data):
    api = BookingApi()

    create_response = api.create_booking(booking_data)

    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    update_data = {"firstname": "Mamkin_Hacker"}

    update_response = api.partial_update_booking(booking_id, update_data)

    assert update_response.status_code == 403

    get_response = api.get_booking(booking_id)

    assert get_response.status_code == 200

    booking = get_response.json()

    assert (booking["firstname"] == booking_data["firstname"])
