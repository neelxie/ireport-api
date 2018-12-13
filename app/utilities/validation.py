""" File contains a utility class for helper functions."""
import re


def file_format(my_file):
    """ This method is to check the image/video file formats."""

    if my_file.endswith(".jpeg") or  my_file.endswith(".jpg"):
        return True

    if my_file.endswith(".mp4") or  my_file.endswith(".mov"):
        return True


class Valid:
    """ Validation class for app."""


    def check_format(self, my_str):
        """ Funtion to check if file string s not space but valid."""
        is_valid = file_format(my_str)
        if my_str.isspace() or len(my_str) < 5:
            return False

        if is_valid != True:
            return False

    def valid_mime(self, media_file):
        """ Method to check media file."""
        if not media_file or not isinstance(media_file, str) or self.check_format(media_file) is False:
            return False

    def check_incident(self, func1, func2):
        """ """
        error_one = func1
        error_two = func2
        if error_one:
            return error_one
        elif error_two:
            return error_two
        return None

    def check_image_video(self, image, video):
        """ Validate images and video files."""
        if self.valid_mime(image) is False:
            return "Image has to be of jpg or jpeg format and a valid String."

        if self.valid_mime(video) is False:
            return "Video has to be a valid String of either mov or mp4."


    def validate_attributes(self, location, comment):
        """ Method to validate string."""

        if not  location or not isinstance(location, float):
            return "Location has to be a valid float."

        if not comment or not isinstance(comment, str) or len(comment) < 6:
            return "Comment has to be a valid String."


    def check_list(self, incidents):
        """ Method to check if list is not empty."""
        if not incidents or len(incidents) < 1:
            return False

    def update_location(self, data):
        """ Class method to validate PATCH location data."""
        if not data or not isinstance(data, float):
            return "New location has to be a float."

    def validate_comment_update(self, update):
        """ Class method to validate new comment data."""
        if not update or not isinstance(update, str) or len(update) < 5:
            return "New Comment ought to be a valid sentence."
        
    def verify_string(self, my_string):
        """ Validation method for a valid string."""
        if not my_string or not isinstance(my_string, str):
            return False

        if my_string.isspace() or len(my_string) < 2:
            return False

    def check_user_base(self, first_str, sec_str, thrd_str, fth_str):
        """ To validate the names for app user signing up."""
        if self.verify_string(first_str) is False or self.verify_string(sec_str) is False or self.verify_string(thrd_str) is False:
            return "First/Last/Other Name all have to be strings of two letters or more."

        if self.verify_string(fth_str) is False:
            return "User Name has to be a string."
        
    def check_credential(self, phn_num, email, pass_word, ad_min):
        """ Method to validate user credentials."""
        if not re.match(r"^[0-9]*$", phn_num):
            return "Phone number must be only digits and no white spaces."

        if self.verify_string(email) or not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
            return "Enter a valid email address."

        if self.verify_string(pass_word) is False or len(pass_word) < 6:
            return "Password has to be a string and longer than 6 characters."

        if not isinstance(ad_min, bool):
            return "is_admin muust be a boolean."

    def validate_login(self, user_name, password):
        """method to check if login details are valid."""
        if self.verify_string(user_name) is False or self.verify_string(password) is False:
            return "Username and Password have to be valid strings."
