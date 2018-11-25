""" This is the Users' models file."""

# A list to contain all app users.
USERS = []


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
        USERS.append(self)
