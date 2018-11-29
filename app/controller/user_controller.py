from flask import jsonify
from flask import request
from datetime import datetime
from ..models.model_users import UserModel

user_model = UserModel()

class UserController:
    """ Class for user controller."""

    def __init__(self):
        """ Class constructor for the User Controller."""
        self.users = []

    def register_user(self, args):
        """ Method to add user."""
        user = user_model.create_user(args)

        if not user or user is None:
            return jsonify({
                'message':'sorry! no users were found'
            }), 200
        return jsonify({
            'message': 'successfully created red flag',
            'users': user
        }), 201

    def fetch_users(self):
        """ Administrator method to retrieve all users."""
        users = user_model.get_users()
        if  not users or users is None or len(users) < 1:
            return jsonify({
                'message':'sorry! no users were found'
            }), 200
        return jsonify({
            'message': 'success',
            'users': users
        }), 200

    def fetch_one_user(self, user_id):
        """ Class method to get single user by ID."""
        user = user_model.get_one_user(user_id)
        if not user or user is None:
            return jsonify({
                'message':'sorry! user with Id not found'
            }), 200
        return jsonify({
            'message': 'success',
            'Single user': user
        }), 200
