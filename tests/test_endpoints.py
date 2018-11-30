""" File to handle tests for incident endpoints. """
import json
from app.utilities.validation import Valid
from .test_structures import TestStructure

test_valid = Valid()

b = 1

class TestIncident(TestStructure):
    """ Test Class for all incidents endpoint"""

    def test_validation_class_valid(self):
        """ Test to check if item is not None."""
        my_list = []
        self.assertEqual(test_valid.check_item(my_list), False)

    def test_index_endpoint(self):
        """ Test method to test index endpoint of the app."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(
        ), '{"data":[{"message":"Welcome to the iReporter Site."}],"status":200}\n')

    def test_update_comment(self):
        """ Test method to edit red flag comment."""
        resp = self.app.patch('/red-flags/1/comment', data=json.dumps(self.test_redflag),
                              content_type='application/json')
        new_comment = {'comment': "Police Brutality"}
        self.test_redflag['comment'] = new_comment['comment']
        # GET THE comment which you changed
        # check that comment text is new_comment
        
        self.assertEqual(self.test_redflag['comment'], new_comment['comment'])
        # self.assertEqual(resp.status_code, 200)

    def test_update_location(self):
        """ Test method to change red flag location."""
        resp = self.app.patch('/red-flags/1/location', data=json.dumps(self.test_redflag),
                              content_type='application/json')
        new_request = {'location': "entebbe"}
        self.test_redflag['location'] = new_request['location']
        self.assertEqual(
            self.test_redflag['location'], new_request['location'])
        # self.assertEqual(resp.status_code, 200)

    def test_get_wrong_url(self):
        """ Test method to check whether incident is in list given its id."""
        resp = self.app.get('/red-fla')
        self.assertEqual(resp.status_code, 404)

    def test_fetch_all_redflags(self):
        """ Test to check route to fetch all incidents."""
        response = self.app.get('/red-flags',
                               content_type='application/json',
                               data=json.dumps(self.all_redflags))
        self.assertEqual(response.status_code, 200)

    def test_fetch_all_redflags_empty(self):
        """ Test for getting all inicdents while list is empty."""
        response = self.app.get('/red-flags',
                                content_type='application/json',
                                data=json.dumps(self.empty_list))
        self.assertEqual(len(self.empty_list), 0)
    
    def test_fetch_single_redflag(self):
        """ Test for checking retrieval of one incident."""
        response = self.app.get(
            '/red-flags/1', data=json.dumps(self.test_redflag))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.test_redflag, response.data)

    def test_add_redflag(self):
        """ Test method for adding an incident."""
        redflags = []
        response = self.app.post(
            '/red-flags',
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
        self.assertEqual(response.status_code, 201)
        self.assertIn(" ", str(response.data))
        self.assertTrue(len(redflags), 2)
        self.assertNotEqual("No redflags found", str(response.data))
        
    def test_delete_redflag(self):
        """ Test method for deletng an incident."""
        response = self.app.delete('/red-flags/1',
                                   content_type='application/json',)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(self.all_redflags), 1)

    def test_delete_redflag_nonexistent(self):
        """ Test for fetchng an item while incdents list is empty."""
        response = self.app.delete('/red-flags/1',
                                   content_type='application/json',
                                   data=json.dumps(self.empty_list))
        self.assertEqual(len(self.empty_list), 0)

    def test_retrieve_all_users(self):
        """ Test route for fetching all users."""
        response = self.app.get('/users',
                                content_type='application/json',
                                data=json.dumps(self.app_users))
        self.assertEqual(response.status_code, 200)

    def test_fetch_users_empty_list(self):
        """ Test for when users list is empty and a fetch is attempted."""
        response = self.app.get('/users',
                                content_type='application/json',
                                data=json.dumps(self.empty_list))
        self.assertEqual(len(self.empty_list), 0)
    
    def test_for_single_user(self):
        """ Test for fetching a single user."""
        response = self.app.get('/users/1', data=json.dumps(self.test_user))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.test_user, response.data)

    def test_signing_up(self):
        """ Test for adding an app user."""
        my_app_users = []
        response = self.app.post(
            '/users',
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
        self.assertTrue(len(my_app_users), 2)
        self.assertNotEqual("No users found", str(response.data))
