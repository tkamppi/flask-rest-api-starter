import unittest
import json

from flask import Response

from {{cookiecutter.app_name}}.apiflask import ApiFlask, ApiResult, ApiException

class TestApiFlask(unittest.TestCase):

    def test_apiflask_response_with_apiresult(self):
        response = ApiFlask(__name__).make_response(ApiResult({"key1": "value1"}))
        json_response = json.loads(response.get_data())
        self.assertIsInstance(response, Response)
        self.assertEqual(response.mimetype, "application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response["key1"], "value1")

    def test_apiexception(self):
        api_exception = ApiException("message")
        api_result = api_exception.to_result()
        response = api_result.to_response()
        json_response = json.loads(response.get_data())
        self.assertIsInstance(response, Response)
        self.assertEqual(response.mimetype, "application/json")
        self.assertEqual(response.status_code, 500)
        self.assertEqual(json_response["error"], "message")

    def test_apiflask_make_response(self):
        app = ApiFlask(__name__)
        with app.test_request_context():
            response = app.make_response("any response")
            self.assertTrue(response.mimetype, "text/html") #defaults to text/html
