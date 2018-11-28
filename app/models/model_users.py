""" This is the Users' models file."""

# A list to contain all app users.
USERS = [
    {
        "user_id": 1,
        "first_name": "Greatest",
        "last_name": "Coder",
        "other_name": "Ever",
        "email": "dede@cia.gov",
        "phone_number": 0705828612,
        "user_name": "haxor",
        "registered": True,
        "is_admin": True
    }
]


class Users:
    """ This is the app Users' class."""

    def __init__(self, user_id, first_name, last_name, other_name,
                 email, phone_number, user_name, registered, is_admin):
        """ The app Users' constructor."""
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.other_name = other_name
        self.email = email
        self.phone_number = phone_number
        self.user_name = user_name
        self.registered = registered
        self.is_admin = is_admin

    def to_json(self):
        """ This method changes class to dict."""
        one_user = {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "other_name": self.other_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "user_name": self.user_name,
            "registered": self.registered,
            "is_admin": self.is_admin
        }
        return one_user
