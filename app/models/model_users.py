""" This is the Users' models file."""
import datetime
from ..utilities.validation import Valid

valid = Valid()

class Base:
    """ This is the base class for a person and 
        holds the person's names and phone number."""

    def __init__(self, first_name, last_name, other_name, phone_number):
        """ Constructor for the base class."""
        self.first_name = first_name
        self.last_name = last_name
        self.other_name = other_name
        self.phone_number = phone_number


class Credential:
    """ Class to hold the necessary log in credentials."""

    def __init__(self, email, user_name, password):
        """ Initializing the class will require the above attributes."""
        self.email = email
        self.user_name = user_name
        self.password = password


class User:
    """ Class for comprehensive Users"""

    def __init__(self, base, credential, is_admin, user_id):
        """ Using composition, integrate base class, credential and 
            other remaining attributes to make a complete User Class."""
        self.base = base
        self.credential = credential
        self.is_admin = is_admin
        self.user_id = user_id
        self.registered = str(datetime.datetime.now())

    def to_dict(self):
        """ Method to change the user class to a JSON object for retrieval."""

        return {
            "first_name": self.base.first_name,
            "last_name": self.base.last_name,
            "other_name": self.base.other_name,
            "phone_number": self.base.phone_number,
            "email": self.credential.email,
            "user_name": self.credential.user_name,
            "password": self.credential.password,
            "is_admin": self.is_admin,
            "user_id": self.user_id,
            "registered": self.registered
        }


class UserDB:
    """ App users will be stored in this class."""
    def __init__(self):
        """ app users will be held in a list called all_users."""
        self.all_users = []
        
    def create_user(self, user):
        """ Method for adding a user."""
        return self.all_users.append(user)

    def checking_user(self, user_name, email):
        """ Check whether username or email already exist in list."""
        temp = [user for user in self.all_users if user.credential.user_name == user_name]
        mail = [user for user in self.all_users if user.credential.email == email]

        if len(temp) > 1:
            return "User name is already taken."
        elif len(mail) > 1:
            return "Email already has an account."
        else:
            return None
    
    def validate_login(self, user_name, password):
        error = valid.validate_login(user_name, password)

        if error:
            return error

        temp = [user for user in self.all_users if user.credential.user_name == user_name]
        
        if len(temp) != 1:
            return "Username not found. Please sign up."
        if temp[0].credential.password != password:
            return "Wrong Password"
        return None

