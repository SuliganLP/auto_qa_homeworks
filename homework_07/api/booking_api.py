import requests


class BookingApi:
    BASE_URL = "https://restful-booker.herokuapp.com"

    def __init__(self):
        self.session = requests.Session()

        self.session.headers.update({"Content-Type": "application/json", "Accept": "application/json"})

    def create_booking(self, booking_data):
        return self.session.post(f"{self.BASE_URL}/booking", json=booking_data)

    def get_booking(self, booking_id):
        return self.session.get(f"{self.BASE_URL}/booking/{booking_id}")

    def partial_update_booking(self, booking_id, booking_data, token=None):
        headers = {}

        if token:
            headers["Cookie"] = f"token={token}"

        return self.session.patch(f"{self.BASE_URL}/booking/{booking_id}", json=booking_data, headers=headers)

    def delete_booking(self, booking_id, token):
        headers = {"Cookie": f"token={token}"}

        return self.session.delete(f"{self.BASE_URL}/booking/{booking_id}", headers=headers)
