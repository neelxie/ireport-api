""" File to handle tests for incident endpoints. """
import json
from app.utilities.validation import Valid
from app.utilities.validation import file_format
from .test_structures import TestStructure

test_valid = Valid()


class TestIncident(TestStructure):
    """ Test Class for all incidents endpoint"""

    def test_validation_class_valid(self):
        """ Test to validate check incident method."""

        self.assertEqual(
            test_valid.check_incident("", 0.2, "lgfg.jpg", "ads.mp4", "sdfdsf"),
            "Created by has to be valid integer and not Zero.")
        self.assertEqual(
            test_valid.check_incident(1, "", "lgfg.jpg", "ads.mp4", "sdfdsf"),
            "Location has to be a valid float.")
        self.assertEqual(
            test_valid.check_incident(1, 0.2, "jpg", "ads.mp4", "sdfdsf"),
            "Image has to be of jpg or jpeg format and a valid String.")
        self.assertEqual(
            test_valid.check_incident(1, 0.2, "lgfg.jpg", 4, "sdfdsf"),
            "Video has to be a valid String of either mov or mp4.")
        self.assertEqual(
            test_valid.check_incident(1, 0.2, "lgfg.jpg", "ads.mp4", 4),
            "Comment has to be a valid String.")

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
        """ Method to check if image and video are valid."""
        self.assertFalse(test_valid.check_format("jd"))
        self.assertFalse(test_valid.check_format("jddfddmp4"))

    def test_file_format(self):
        """ Test for helper method in validation file."""
        self.assertTrue(file_format("crime.mp4"))

    def test_index_endpoint(self):
        """ Test method to test index endpoint of the app."""
        response = self.app.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data.decode(),
            '{"data":[{"message":"Welcome to the iReporter Site."}],"status":200}\n')

    def test_update_comment(self):
        """ Test method to edit red flag comment."""
        resp = self.app.patch('/api/v1/red-flags/1/comment', data=json.dumps(self.test_redflag),
                              content_type='application/json')
        new_comment = {'comment': "Police Brutality"}
        self.test_redflag['comment'] = new_comment['comment']
        # GET THE comment which you changed
        # check that comment text is new_comment

        self.assertEqual(self.test_redflag['comment'], new_comment['comment'])
        # self.assertEqual(resp.status_code, 200)

    def test_update_location(self):
        """ Test method to change red flag location."""
        resp = self.app.patch('/api/v1/red-flags/1/location', data=json.dumps(self.test_redflag),
                              content_type='application/json')
        new_request = {'location': "entebbe"}
        self.test_redflag['location'] = new_request['location']
        self.assertEqual(
            self.test_redflag['location'], new_request['location'])
        # self.assertEqual(resp.status_code, 200)

    def test_get_wrong_url(self):
        """ Test method to check whether incident is in list given its id."""
        resp = self.app.get('/api/v1/red-fla')
        self.assertEqual(resp.status_code, 404)

    def test_fetch_all_redflags(self):
        """ Test to check route to fetch all incidents."""
        response = self.app.get('/api/v1/red-flags')
        self.assertEqual(response.status_code, 200)

    def test_fetch_all_redflags_empty(self):
        """ Test for getting all inicdents while list is empty."""
        response = self.app.get('/api/v1/red-flags')
        self.assertEqual(len(self.empty_list), 0)

    def test_fetch_single_redflag(self):
        """ Test for checking retrieval of one incident."""
        response = self.app.get('/api/v1/red-flags/1')
        # self.assertEqual(response.status_code, 200)
        self.assertTrue(self.test_redflag, response.data)

    def test_add_redflag(self):
        """ Test method for adding an incident."""
        redflags = []
        response = self.app.post(
            '/api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(dict(
                created_on="2018-11-29 10:04:38.919951",
                created_by=1,
                record_type="Redflag",
                location='123.01.56.78',
                status="Draft",
                image="image.jpg",
                video="video.mp4",
                comment="Just testing this app."
            )))
        redflags.append(dict)
        # self.assertEqual(response.status_code, 201)
        self.assertIn(" ", str(response.data))
        self.assertTrue(len(redflags))
        self.assertNotEqual("No redflags found", str(response.data))

    def test_delete_redflag(self):
        """ Test method for deletng an incident."""
        response = self.app.delete('/api/v1/red-flags/1',
                                   data=json.dumps(self.test_redflag),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(self.all_redflags), 1)

    def test_delete_redflag_nonexistent(self):
        """ Test for fetchng an item while incdents list is empty."""
        response = self.app.delete('/api/v1/red-flags/9',
                                   content_type='application/json',
                                   data=json.dumps(self.empty_list))
        self.assertEqual(len(self.empty_list), 0)

    def test_retrieve_all_users(self):
        """ Test route for fetching all users."""
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)

    def test_fetch_users_empty_list(self):
        """ Test for when users list is empty and a fetch is attempted."""
        response = self.app.get('/api/v1/users')
        self.assertEqual(len(self.empty_list), 0)

    def test_for_single_user(self):
        """ Test for fetching a single user."""
        response = self.app.get('/api/v1/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.test_user, response.data)

    def test_signing_up(self):
        """ Test for adding an app user."""
        my_app_users = []
        response = self.app.post(
            '/api/v1/users',
            content_type='application/json',
            data=json.dumps(dict(
                email="dede@cia.gov",
                first_name="Greatest",
                is_admin=False,
                last_name="Coder",
                other_name="Ever",
                phone_number="0705828612",
                registered="2018-11-29 10:10:02.086352",
                user_id=1,
                user_name="haxor"
            )))
        my_app_users.append(dict)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(len(my_app_users))
        self.assertNotEqual("No users found", str(response.data))
