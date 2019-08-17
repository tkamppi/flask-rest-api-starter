from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from {{cookiecutter.app_name}}.apiflask import ApiResult

blueprint = Blueprint('restapi',
                      __name__,
                      url_prefix='/api')

@blueprint.route('/v1/example-route', methods=['POST'])
@jwt_required
def example():
    '''Example route which requires a valid jwt from this application
    and displays the username of the calling user'''
    calling_user = get_jwt_identity()
    response = {}
    response['calling_user'] = calling_user
    return ApiResult(response, 200)
