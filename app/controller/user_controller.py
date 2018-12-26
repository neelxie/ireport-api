"""File for the user controller."""
from flask import jsonify
from flask import request
import datetime
import jwt
from ..utility.validation import Valid
from ..utility.auth import my_secret_key
from ..models.model_users import (
    Base, User, UserDB, Credential)


class UserController:
    """ Class for user controller."""

    user_list = UserDB()
    validator = Valid()


    def __init__(self):
        """ Class constructor for the User Controller."""
        pass

    def register_user(self):
        """ Controller logic for signup class method."""
        data = request.get_json()

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        other_name = data.get("other_name")
        phone_number = data.get("phone_number")
        email = data.get("email")
        user_name = data.get("user_name")
        password = data.get("password")
        is_admin = data.get("is_admin")
        user_id = len(self.user_list.all_users)+ 1

        # check if user data is valid if not return an error.
        error = self.validator.check_incident(
            self.validator.check_user_base(
                first_name, last_name, other_name, user_name), self.validator.check_credential(
                phone_number, email, password, is_admin))

        # if the username or email are already registered return error.
        exist = self.user_list.checking_user(user_name, email)

        user = User(
            Base(
                first_name,
                last_name,
                other_name,
                phone_number),
            Credential(
                email,
                user_name,
                password),
            is_admin,
            user_id)

        self.user_list.create_user(user)

        token = jwt.encode(
            {"user_id": user_id, "user_name": user_name, "is_admin": is_admin, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=15)}, my_secret_key).decode('UTF-8')

        payload = jwt.decode(token, my_secret_key)

        if error:
            return jsonify({
                'error': error,
                "status": 400
            }), 400

        if exist is not None: 
            return jsonify({
                "status": 401,
                "error": exist
            }), 401

        return jsonify({
            "status": 201,
            'success':[{
                'token': token,
                "payload": payload.get('user_id')
                # 'message': f'{user_name} successfully registered'
            }]
        }), 201

    def fetch_users(self):
        """ Administrator method to retrieve all users."""

        if len(self.user_list.all_users) < 1:
            return jsonify({
                "data":[{'message':'sorry! No App users yet.'}],
                "status": 200
            }), 200
        return jsonify({
            'status': 200,
            'users': [user.to_dict() for user in self.user_list.all_users]
        }), 200

    def sign_in(self):
        """ Class method to get single user by ID."""
        login =  request.get_json()

        user_name = login.get("user_name")
        password = login.get("password")

        error = self.user_list.validate_login(user_name, password)

        if error:
            return jsonify({
                'message':error,
                "status": 403
            }), 403

        token = jwt.encode(
            {"user_id": user_name, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=15)}, my_secret_key).decode('UTF-8')

        payload = jwt.decode(token, my_secret_key)

        return jsonify({
            'status': 200,
            'user logged in': [{
                'token': token,
                'success': f'{user_name} successfully logged in.'
            }]
        }), 200

    def app_user(self, user_id):
        """ Retrieve single app user."""
        user = self.user_list.single_user(user_id)
        if user is None:
            return jsonify({
                'status': 400,
                'error': "No user with given ID."
            }), 400
        return jsonify({
            'status':200,
            'single user': [user.to_dict()]
        }), 200
