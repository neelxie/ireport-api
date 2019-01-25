""" File for test for the validation class."""
from app.utility.validation import Valid
from app.utility.validation import check_file_extension
from .test_structures import TestStructure

test_valid = Valid()


class TestValidationClass(TestStructure):
    """ Test Class for validation used in utility."""

    TEST_LIST = []

    def test_validate_check_if_either_function_has_invalid(self):
        """ Test to validate check incident method."""
        self.assertEqual(
            test_valid.check_if_either_function_has_invalid(1, 0), 1)
        self.assertEqual(
            test_valid.check_if_either_function_has_invalid(0, 1), 1)
        self.assertEqual(
            test_valid.check_if_either_function_has_invalid(0, 0), None)

    def test_validate_location_and_comment(self):
        """ Test for the validation class method validate_location_and_comment."""
        self.assertEqual(
            test_valid.validate_location_and_comment(
                "no",
                "just_testing"),
            "incident location should be an address in without spaces.")
        self.assertEqual(
            test_valid.validate_location_and_comment(
                "kanjokya", 4), "Comment has to be a valid String.")

    def check_for_white_spaces(self):
        """ Test to check if word has spaces."""
        self.assertFalse(test_valid.check_for_white_spaces(' '))
        

    def test_valid_patch_location(self):
        """ Test to check if data from patch location is valid."""
        self.assertEqual(
            test_valid.validate_location_update({"location": 12}),
            "New location should be an address in words.")

    def test_comment_update(self):
        """ Test method to validate comment data from patch."""
        self.assertEqual(
            test_valid.validate_comment_update({"comment": 54}),
            "New Comment ought to be a valid sentence.")

    def test_mime_format(self):
        """ Method to check for valid python strings."""
        self.assertFalse(test_valid.check_format("jd"))
        self.assertFalse(test_valid.check_format("jddfddmp4"))
        self.assertFalse(test_valid.validate_string(0))
        self.assertFalse(test_valid.validate_string(" "))

    def test_check_file_extension(self):
        """ Test for helper method in validation file."""
        self.assertTrue(check_file_extension("crime.mp4"))
        self.assertTrue(check_file_extension("crime.jpeg"))

    def test_validate_status(self):
        """ method to check if the status is valid."""
        self.assertEqual(
            test_valid.validate_status(55), 'Status has to be a string of either "investigation", "resolved", or "rejected".')

    def test_check_user_base(self):
        """ validation method check user base."""
        self.assertEqual(
            test_valid.check_user_base(
                "", "w2", "w22", "sdsdsd"),
            "Firstname should have only letters between 2 and 15 chaarcters.")
        self.assertEqual(
            test_valid.check_user_base(
                "badhdda", "w2", "w22", "sdsdsd"),
            "Last Name should have only letters between 2 and 15 chaarcters.")
        self.assertEqual(
            test_valid.check_user_base(
                "dsddsdsd", "hshhhshhs", "w22", "sdsdsd"),
            "Other Name should have only letters between 2 and 15 chaarcters.")
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
                "457862556", "asdgob", "sdsdsds", False),
            "Enter a valid email address.")
        self.assertEqual(
            test_valid.check_credential(
                "457862556", "asd@hdd.gob", "sd", False),
            "Password has have 6 to 15 characters.")
        self.assertEqual(
            test_valid.check_credential(
                "457862556", "asd@hdd.gob", "sdsdsds", "asasas"),
            "is_admin muust be a boolean.")

    def test_validate_media_file(self):
        """ Test for validation method valida mime
            and the check_media_file_is_valid method."""
        self.assertFalse(test_valid.validate_media_file(0))
        self.assertEqual(
            test_valid.check_media_file_is_valid(
                0, "video.mp4"),
            "Image has to be of jpg or jpeg format and a valid String.")
        self.assertEqual(
            test_valid.check_media_file_is_valid(
                "image.jpeg", 0),
            "Video has to be a valid String of either mov or mp4.")

    def test_validate_login(self):
        """ validating entered login credentials."""
        self.assertEqual(
            test_valid.validate_login(
                "fake", ""),"Username and Password have to be valid strings.")

    def test_token_strip(self):
        """ Test stripped token."""
        self.assertEqual(
            test_valid.strip_token_of_bearer(
                "Bearer eyiamthe.greatestcoder.ever"), "eyiamthe.greatestcoder.ever")

    def test_validate_attributes(self):
        """ Test to validate list attributes."""
        self.assertEqual(test_valid.valdate_attributes(None, []), "No data was entered or dict is empty.")
        self.assertEqual(test_valid.valdate_attributes({"cat": 3}, ["dog"]), ["dog"])
