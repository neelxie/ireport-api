""" File for test for the validation class."""

from app.utilities.validation import Valid
from app.utilities.validation import file_format
from .test_structures import TestStructure

test_valid = Valid()


class TestValidationClass(TestStructure):
    """ Test Class for validation used in utility."""

    def test_validate_check_incident(self):
        """ Test to validate check incident method."""
        self.assertEqual(
            test_valid.check_incident(1, 0), 1)
        self.assertEqual(
            test_valid.check_incident(0, 1), 1)
        self.assertEqual(
            test_valid.check_incident(0, 0), None)

    def test_validate_attributes(self):
        """ Test for the validation class method validate_attributes."""
        self.assertEqual(
            test_valid.validate_attributes(
                "",
                "just_testing"),
            "Location has to be a valid float.")
        self.assertEqual(
            test_valid.validate_attributes(
                0.245, 4), "Comment has to be a valid String.")

    def test_validate_list(self):
        """ Test to check if item is not None."""
        my_test_list = []
        self.assertFalse(test_valid.check_list(my_test_list))

    def test_valid_patch_location(self):
        """ Test to check if data from patch location is valid."""
        self.assertEqual(
            test_valid.update_location({"location": "d"}),
            "New location has to be a float.")

    def test_comment_update(self):
        """ Test method to validate comment data from patch."""
        self.assertEqual(
            test_valid.validate_comment_update({"comment": 54}),
            "New Comment ought to be a valid sentence.")

    def test_mime_format(self):
        """ Method to check for valid python strings."""
        self.assertFalse(test_valid.check_format("jd"))
        self.assertFalse(test_valid.check_format("jddfddmp4"))
        self.assertFalse(test_valid.verify_string(0))
        self.assertFalse(test_valid.verify_string(" "))

    def test_file_format(self):
        """ Test for helper method in validation file."""
        self.assertTrue(file_format("crime.mp4"))
        self.assertTrue(file_format("crime.jpeg"))

    def test_check_user_base(self):
        """ validation method check user base."""
        self.assertEqual(
            test_valid.check_user_base(
                "", "w2", "w22", "sdsdsd"),
            "First/Last/Other Name all have to be strings of two letters or more.")
        self.assertEqual(
            test_valid.check_user_base(
                "Derek", "Derrick", "Kidrice", "  "),
            "User Name has to be a string.")

    def test_check_credential(self):
        """ user credentials method test."""
        self.assertEqual(
            test_valid.check_credential(
                "@$$$", "asd@hdd.gob", "sdsdsds", False),
            "Phone number must be only digits and no white spaces.")
        self.assertEqual(
            test_valid.check_credential(
                "45786", "asdgob", "sdsdsds", False),
            "Enter a valid email address.")
        self.assertEqual(
            test_valid.check_credential(
                "45786", "asd@hdd.gob", "sd", False),
            "Password has to be a string and longer than 6 characters.")
        self.assertEqual(
            test_valid.check_credential(
                "45786", "asd@hdd.gob", "sdsdsds", "asasas"),
            "is_admin muust be a boolean.")

    def test_valid_mime(self):
        """ Test for validation method valida mime
            and the check_image_video method."""
        self.assertFalse(test_valid.valid_mime(0))
        self.assertEqual(
            test_valid.check_image_video(
                0, "video.mp4"),
            "Image has to be of jpg or jpeg format and a valid String.")
        self.assertEqual(
            test_valid.check_image_video(
                "image.jpeg", 0),
            "Video has to be a valid String of either mov or mp4.")

    def test_validate_login(self):
        """ validating entered login credentials."""
        self.assertEqual(test_valid.validate_login("fake", ""),"Username and Password have to be valid strings.")
