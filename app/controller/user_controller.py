"""File for the user controller."""
from flask import jsonify
from flask import request
import datetime
import jwt
from ..utility.validation import Valid
from ..utility.auth import my_secret_key
from ..models.model_users import (
    Base, User, Credential)
from ..db.ireporter_db import DatabaseConnection

db = DatabaseConnection()


class UserController:
    """ Class for user controller."""

    validator = Valid()

    def __init__(self):
        """ Class constructor for the User Controller.
        """
        pass

    def register_user(self):
        """ Controller logic for signup class method.
        """
        data = request.get_json()

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        other_name = data.get("other_name")
        phone_number = data.get("phone_number")
        email = data.get("email")
        user_name = data.get("user_name")
        password = data.get("password")
        is_admin = data.get("is_admin")

        user_attributes = [
            "first_name",
            "last_name",
            "other_name",
            "phone_number",
            "email",
            "user_name",
            "password",
            "is_admin"]
        user_attribute_error = self.validator.valdate_attributes(
            data,
            user_attributes)

        if user_attribute_error is not None:
            return jsonify({"status": 400,
                "error": "You have not entered this/these user attributes.",
                "missing attributes": user_attribute_error,
                }), 400

        # check if user data is valid if not return an error.
        error = self.validator.check_if_either_function_has_invalid(
            self.validator.check_user_base(
                first_name, last_name, other_name, user_name), self.validator.check_credential(
                phone_number, email, password, is_admin))
        
        if error:
            return jsonify({
                'error': error,
                "status": 400
            }), 400

        # if the username or email are already registered return error.
        username_exist = db.check_username(user_name)
        email_exist = db.check_email(email)

        if username_exist is not None or email_exist is not None: 
            return jsonify({
                "status": 401,
                "error": "Either username or email are already in registered."
            }), 401

        user = db.add_user(first_name, last_name, other_name, phone_number, email, user_name, password, is_admin)

        # after successfully adding the user
        # fetch user bse i need to use the database assigned ID 
        # to add it to the token from which i will get it to use it for 'created-BY'
        user = db.check_username(user_name)
        user_id = user.get('user_id')
        token = jwt.encode(
            { 'user_id': user_id, "user_name": user_name, "is_admin": is_admin, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=60)}, my_secret_key).decode('UTF-8')

        payload = jwt.decode(token, my_secret_key)

        return jsonify({
            "status": 201,
            'success':[{
                'token': token,
                "user": user
                # 'message': f'{user_name} successfully registered'
            }]
        }), 201

    def fetch_users(self):
        """ Administrator method to retrieve all users.
        """
        all_users = db.get_users()
        if len(all_users) < 1:
            return jsonify({
                "data":[{'message':'sorry! No App users yet.'}],
                "status": 400
            }), 400
        return jsonify({'status': 200,
            'users': [user for user in all_users]
            }), 200

    def sign_in(self):
        """ Class method to get single user by ID.
        """
        login = request.get_json()

        user_name = login.get("user_name")
        password = login.get("password")

        error = self.validator.validate_login(user_name, password)

        if error:
            return jsonify({
                'message': error,
                "status": 401
            }), 401

        user_true = db.login(password, user_name)

        if user_true is None:
            return jsonify({'status': 401,
                'error': "The log in credentials you entered are wrong."
            }), 401

        user = db.check_username(user_name)
        token = jwt.encode(
            {"user_id": user.get('user_id'), "user_name": user.get('user_name'), \
            "is_admin": user.get('is_admin'), 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=60)}, my_secret_key).decode('UTF-8')

        # payload = jwt.decode(token, my_secret_key)
        return jsonify({
            'status': 200,
            'user logged in': [{
                'token': token,
                'user': user
            }]
        }), 200

    def app_user(self, user_id):
        """ Retrieve single app user.
        """
        user = db.get_user(user_id)
        if user is None:
            return jsonify({
                'status': 400,
                'error': "No user by that ID."
            }), 400

        return jsonify({
            'status': 200,
            'single user': [user]
        }), 200
