""" File contains a utility class for helper functions."""
import re


def check_file_extension(my_file):
    """ This method is to check the image/video file extensions.
    """
    if my_file.endswith(".jpeg") or my_file.endswith(".jpg"):
        return True

    if my_file.endswith(".mp4") or my_file.endswith(".mov"):
        return True


class Valid:
    """ Validation class for app.
    """
    # These are the only valid incident statuses
    VALID_STATUSES = ['investigation', 'resolved', 'rejected']

    def strip_token_of_bearer(self, token):
        """ Authentication helper function to strip the token.
        """
        new_token = token.lstrip('Bearer').strip(' ')
        return new_token

    def check_format(self, my_str):
        """ Funtion to check if file string has not space but valid.
        """
        is_valid = check_file_extension(my_str)
        if my_str.isspace() or len(my_str) < 5:
            return False

        if not is_valid:
            return False

    def validate_media_file(self, media_file):
        """ Method to check media file.
        """
        if not isinstance(media_file, str) or self.check_format(
                media_file) is False:
            return False

    def check_if_either_function_has_invalid(self, func1, func2):
        """This function takes in two functions and checks if neither is none.
        """
        error_one = func1
        error_two = func2
        if error_one:
            return error_one
        elif error_two:
            return error_two
        return None

    def check_media_file_is_valid(self, image, video):
        """ Validate images and video files.
        """
        if self.validate_media_file(image) is False:
            return "Image has to be of jpg or jpeg format and a valid String."

        if self.validate_media_file(video) is False:
            return "Video has to be a valid String of either mov or mp4."

    def validate_location_and_comment(self, location, comment):
        """ Method to validate comment and location.
        """
        if not isinstance(location, float):
            return "Location has to be a valid float."

        if not isinstance(comment, str) or len(comment) < 6:
            return "Comment has to be a valid String."

    def check_list(self, my_list):
        """ Method to check if list is not empty.
        """
        if not my_list or len(my_list) < 1:
            return False

    def validate_location_update(self, data):
        """ Class method to validate PATCH location data.
        """
        if not data or not isinstance(data, float):
            return "New location has to be a float."

    def validate_comment_update(self, update):
        """ Class method to validate new comment data.
        """
        if not update or not isinstance(update, str) or len(update) < 5:
            return "New Comment ought to be a valid sentence."

    def validate_string(self, my_string):
        """ Validation method for a valid string.
        """
        if not isinstance(my_string, str) or not my_string.isalpha():
            return False

        if my_string.isspace() or len(my_string) > 15 or len(my_string) < 2:
            return False

    def check_user_base(self, first_str, sec_str, thrd_str, fth_str):
        """ To validate the names for app user signing up.
        """
        if self.validate_string(first_str) is False or self.validate_string(
                sec_str) is False or self.validate_string(thrd_str) is False:
            return "First/Last/Other Name all have to be strings of two letters or more."

        if self.validate_string(fth_str) is False:
            return "User Name has to be a string."

    def check_credential(self, phn_num, email, pass_word, ad_min):
        """ Method to validate user credentials.
        """
        # if not phn_num or not re.match(r"^[0-9]*$", phn_num):
        if not phn_num or not isinstance(phn_num, int):
            return "Phone number must be only digits and no white spaces."

        if not isinstance(email, str) or not re.match(
                r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
            return "Enter a valid email address."

        if self.validate_string(pass_word) is False or len(pass_word) < 6:
            return "Password has to be a string and longer than 6 characters."

        if not isinstance(ad_min, bool):
            return "is_admin muust be a boolean."

    def validate_login(self, user_name, password):
        """method to check if login details are valid strings.
        """
        if self.validate_string(
                user_name) is False or self.validate_string(password) is False:
            return "Username and Password have to be valid strings."

    def validate_status(self, status):
        """Method to check if status is valid.
        """
        if self.validate_string(
                status) is False or status not in self.VALID_STATUSES:
            return 'Status has to be a string of either "investigation", "resolved", or "rejected".'

    def valdate_attributes(self, data, mylist):
        """Method to validate list elements.
        """
        if data is None or len(data) < 1:
            return "No data was entered or dict is empty."
        error_list = [attr for attr in mylist if data.get(attr) is None]
        if len(error_list) > 0:
            return error_list
