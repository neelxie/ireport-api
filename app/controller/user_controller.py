from flask import jsonify
from flask import request
from datetime import datetime
from ..models.model_users import UserModel


class UserController:
    """ Class for user controller."""

    user_model = UserModel()

    def __init__(self):
        """ Class constructor for the User Controller."""
        self.users = []

    def register_user(self):
        data = request.get_json()
        user = self.user_model.create_user(data)

        if not user:
            return jsonify({
                'message':'sorry! no users were found',
                "status": 400
            }), 400
        return jsonify({
            "status": 201,
            'message': 'successfully created red flag',
            'users': user
    
        }), 201

    def fetch_users(self):
        """ Administrator method to retrieve all users."""
        users = self.user_model.get_users()
        if  not users or len(users) < 1:
            return jsonify({
                'message':'sorry! no users were found',
                "status": 400
            }), 400
        return jsonify({
            'message': 'success',
            'users': users
        }), 200

    def fetch_one_user(self, user_id):
        """ Class method to get single user by ID."""
        user = self.user_model.get_one_user(user_id)
        if not user:
            return jsonify({
                'message':'sorry! user with Id not found',
                "status": 400
            }), 400
        return jsonify({
            'message': 'success',
            'Single user': user
        }), 200
