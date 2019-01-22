from functools import wraps
import jwt
from flask import request, jsonify
from .validation import Valid

token_valid = Valid()

my_secret_key = "Zoe"


def token_required(my_function):
    @wraps(my_function)
    def decorate(*args, **kwargs):

        try:

            headers = request.headers.get('Authorization')
            
            try:
                token = token_valid.strip_token_of_bearer(headers)

        # print(token)
                data = jwt.decode(token, my_secret_key)
                print(data)

            except (jwt.InvalidTokenError, jwt.InvalidSignatureError, jwt.ExpiredSignatureError):
                return jsonify({
                'error': "Unauthorized! Invalid Token!",
                "status": 401
            }), 401


        except KeyError:
            return jsonify({
                'error': "Unauthorized! Token is missing.",
                'status': 401
            }), 401

        # if not data:
        #     return jsonify({
        #         'error': "Unauthorized! Invalid Token!",
        #         "status": 401
        #     }), 401

        return my_function(*args, **kwargs)
    return decorate


def user_identity():
    """Get a user identity from token.
    """
    auth = request.headers['Authorization']
    token = auth.lstrip('Bearer').strip(' ')
    return jwt.decode(token, my_secret_key)


def admin_route(my_route):
    @wraps(my_route)
    def only_admin(*args, **kwargs):
        is_admin = user_identity().get("is_admin")
        if is_admin is False:
            return jsonify({
                'error': "Forbidden! This is an Admin ONLY route, and sadly you are not Admin.",
                'status': 403
            }), 403
        return my_route(*args, **kwargs)
    return only_admin
