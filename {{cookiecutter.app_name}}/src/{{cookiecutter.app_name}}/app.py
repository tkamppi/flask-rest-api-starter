from {{cookiecutter.app_name}} import authentication, restapi
from {{cookiecutter.app_name}}.apiflask import ApiFlask, ApiException
from {{cookiecutter.app_name}}.extensions import jwt
from {{cookiecutter.app_name}} import configuration


def create_app(config_object=configuration):
    """Application factory. See: http://flask.pocoo.org/docs/patterns/appfactories/."""
    app = ApiFlask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)
    return app

def register_extensions(app):
    jwt.init_app(app)

def register_blueprints(app):
    app.register_blueprint(authentication.views.blueprint)
    app.register_blueprint(restapi.views.blueprint)

def register_error_handlers(app):
    app.register_error_handler(
        ApiException, lambda err: err.to_result())
