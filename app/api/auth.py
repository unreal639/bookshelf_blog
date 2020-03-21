from . import api
from flask_httpauth import HTTPTokenAuth
from flask import jsonify, make_response

api_auth = HTTPTokenAuth()


@api_auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)