import unittest
import json

from {{cookiecutter.app_name}}.app import create_app

# Username / Password for authentication tests.
TEST_USERNAME = "test"
TEST_PASSWORD = "test"
LOGIN_ENDPOINT = "/authentication/v1/login"


class TestAuthentication(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_login(self):
        payload = {"username": TEST_USERNAME, "password": TEST_PASSWORD}
        headers = {"Content-Type": "application/json"}
        login = self.client.post(LOGIN_ENDPOINT, json=payload, headers=headers)

        self.assertEqual(login.status_code, 200)

        json_response = login.get_json()
        self.assertIn("access_token", json_response)

    def test_login_wrong_password(self):
        payload = {"username": TEST_USERNAME, "password": "wrong_password"}
        headers = {"Content-Type": "application/json"}
        login = self.client.post(LOGIN_ENDPOINT, json=payload, headers=headers)

        self.assertEqual(login.status_code, 401)

    def test_wrong_content_type(self):
        login = self.client.post(LOGIN_ENDPOINT, headers={"Content-Type": "text/plain"})
        self.assertEqual(login.status_code, 415)

    def test_missing_username(self):
        login = self.client.post(
            LOGIN_ENDPOINT,
            headers={"Content-Type": "application/json"},
            json={"password": "does not matter"},
        )
        self.assertEqual(login.status_code, 422)

    def test_missing_password(self):
        login = self.client.post(
            LOGIN_ENDPOINT,
            headers={"Content-Type": "application/json"},
            json={"username": "does not matter"},
        )
        self.assertEqual(login.status_code, 422)
