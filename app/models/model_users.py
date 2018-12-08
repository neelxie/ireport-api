""" This is the Users' models file."""
import datetime

# A list to contain all app users.
users = [
    {
        "user_id": 1,
        "first_name": "Greatest",
        "last_name": "Coder",
        "other_name": "Ever",
        "email": "dede@cia.gov",
        "phone_number": '0705828612',
        "user_name": "haxor",
        "registered": "2018-11-29 10:10:02.086352",
        "is_admin": True
    }
]


class UserModel:
    """ This is the app Users' class."""

    def __init__(self):
        """ class Constructor."""
        self.users = users
        
    def create_user(self, args):
        """ Method to create user."""
        user = dict(
            user_id=len(users) + 1,
            first_name=args['first_name'],
            last_name=args["last_name"],
            other_name=args["other_name"],
            email=args["email"],
            phone_number=args["phone_number"],
            user_name=args["user_name"],
            registered=str(datetime.datetime.now()),
            is_admin=args["is_admin"]
        )
        users.append(user)

        return user

    def get_one_user(self):
        """ Method to fetch details of one user."""
        
        item = [user for user in users if user['user_id'] == user_id]

        if item:
            return item[0]
        return None

    def get_users(self):
        """ Admin method to fetch all users."""
        return self.users

