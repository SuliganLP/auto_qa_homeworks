import requests


class AuthApi:
    BASE_URL = "https://restful-booker.herokuapp.com"

    def create_token(self):
        data = {"username": "admin", "password": "password123"}

        return requests.post(f"{self.BASE_URL}/auth", json=data)
