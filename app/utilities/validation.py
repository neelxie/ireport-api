""" File contains a utility class for helper functions."""

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

    def check_incident(self, created_by, location, image, video, comment):
        """ Method to validate string."""

        if not created_by or not isinstance(created_by, int) or created_by == 0:
            return "Created by has to be valid integer and not Zero."

        if not  location or not isinstance(location, float):
            return "Location has to be a valid float."

        if not image or not isinstance(image, str) or self.check_format(image) is False:
            return "Image has to be of jpg or jpeg format and a valid String."

        if not video or not isinstance(video, str) or self.check_format(video) is False:
            return "Video has to be a valid String of either mov or mp4."

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
        