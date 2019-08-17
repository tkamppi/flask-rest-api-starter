# flask-rest-api-starter
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Overview
This is a cookiecutter templated REST API Flask application.
The starter provides a scaffold to get going quickly with writing application logic instead of spending time on everything else around it.

Included:
* Dockerized Flask application
* Gunicorn web-server.
* JWT generation/validation with Bearer tokens.
* Unit-tests for the components included in the starter.

The flask app is using an app-factory pattern: https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/  
With blueprints: https://flask.palletsprojects.com/en/1.1.x/blueprints/  
It implements concepts for JSON API's described by Armin Ronacher (creator of flask) in his talk "Flask for Fun and Profit". https://www.youtube.com/watch?v=1ByQhAM5c1I

## Getting started

### Generate the application
```
pip install cookiecutter
```

```
cookiecutter https://github.com/tkamppi/flask-rest-api-starter.git
```
When you have answered the cookiecutter questions, an app has been generated in a folder with the name you selected for `app_name`.

### Run unit tests
Using Docker 
```
docker build -f Dockerfile.test -t your-preferred-test-imagename .
```

### Run your application
The gunicorn web-server inside the container listens to port 5000 by default.
Build the docker image and run it forwarding your local port 5000 to port 5000 inside the container.
```
docker build -f Dockerfile -t your-app .
docker run -d -p 5000:5000 your-app 
```

### User authentication

The started comes with users with a test user
```
username: test
password: test
```
Authenticate using the authentication endpoint, sending the credentials in the JSON formatted Body (replace localhost if not running on the same machine):  
```
curl localhost:5000/authentication/v1/login --data '{"username":"test", "password":"test"}' -H "Content-Type: application/json"
```
Save the `access_token` value in the response, and use it in your subsequent requests in the `Authorization` HTTP header.  
Example (Replace YOUR-SAVED-access_token-VALUE with your access_token value):
```
curl localhost:5000/api/v1/example-route --data -H "Content-Type: application/json" -H "Authorization: Bearer YOUR-SAVED-access_token-VALUE"
```

Since there are many authentication providers you should re-write the authentication in `src/YOUR-APP-NAME/authentication/views.py` to use that backend instead of the local test user. See for example https://flask-jwt-extended.readthedocs.io/en/latest/complex_objects_from_token.html  
Or if you have an authentication service providing JWT already. A good guide for integrating to those types of endpoints is available here: https://auth0.com/docs/quickstart/backend/python/01-authorization

You must also replace JWT symmetric key `SECRET_KEY` in the `configuration.py` file of your new application, should you continue to use the provided jwt authentication. A good idea can be to for example fetch it from a ENV variable.
