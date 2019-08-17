import unittest

from flask import Response

from {{cookiecutter.app_name}}.apiflask import ApiFlask, ApiResult, ApiException

class TestApiFlask(unittest.TestCase):

    def test_apiflask_response_with_apiresult(self):
        response = ApiFlask(__name__).make_response(ApiResult({'key1': 'value1'}))
        #Remove. Add test for key1 / value1 in Response object (json) and for mimetype
        self.assertIsInstance(response, Response)
