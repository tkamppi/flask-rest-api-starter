from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from {{cookiecutter.app_name}}.apiflask import ApiFlask, ApiException, ApiResult

blueprint = Blueprint('authentication',
                      __name__,
                      url_prefix='/authentication')

@blueprint.route('/v1/login', methods=['POST'])
def login():
    if not request.is_json:
        raise ApiException("Content type must be application/json", 415)

    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username:
        raise ApiException("username missing from body", 422)
    if not password:
        raise ApiException("password missing from body", 422)
    
    # Replace this with your preferred authentication
    if username != 'test' or password != 'test':
        raise ApiException("Incorrect password", 401)

    response = {
        'access_token': create_access_token(identity=username),
        'token_type': 'Bearer'
    }

    return ApiResult(response)