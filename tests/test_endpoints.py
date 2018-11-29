""" File to handle tests for incident endpoints. """
import unittest
from .test_structures import TestStructure
import json

class TestIncident(TestStructure):
    """ Test Class for all incidents endpoint"""

    def test_index_endpoint(self):
        """ Test method to test index endpoint of the app."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '{"data":[{"message":"Welcome to the iReporter Site."}],"status":200}\n')

    # def test_post_incidents(self):
    #     """ Test method to test post endpoint of the app."""
    #     red_flag = {
    #         "incident_id" : 2,
    #         "created_on" : "ddsd",
    #         "created_by" : 1,
    #         "record_type" : "RedFlag",
    #         "location" : "Nkokonjeru",
    #         "status" : "Draft",
    #         "comment" : "We win"
    #     }
    #     response = self.app.post('/red-flags', data=json.dumps(red_flag),
    #          content_type='application/json')
    #     self.assertEqual(response.status_code, 201)yes

    # def test_edit_comment_incident(self):
    #     """ Test method to edit red flag comment."""
    #     red_flag = {
    #         "incident_id" : 2,
    #         "created_on" : "ddsd",
    #         "created_by" : 1,
    #         "record_type" : "RedFlag",
    #         "location" : "Nkokonjeru",
    #         "status" : "Draft",
    #         "comment" : "We win"
    #     }
    #     resp = self.app.patch('/red-flags/1/comment', data=json.dumps(red_flag),
    #          content_type='application/json')
    #     self.assertEqual(resp.status_code, 200)

    # def test_update_incident(self):
    #     """ Test method to change red flag location."""
    #     red_flag = {
    #         "comment" : "We win"
    #     }
    #     resp = self.app.patch('/red-flags/1/comment', data=json.dumps(red_flag),
    #          content_type='application/json')
    #     # self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(resp.data.decode(), red_flag.get('comment'))

    # yes

    # def test_authenticate_incident_user_id_missing(self):
    #     """ Test method to test delivery order without a user id."""
    #     red_flag = {
    #         "incident_id" : 2,
    #         "created_on" : "ddsd",
    #         "created_by" : "",
    #         "record_type" : "RedFlag",
    #         "location" : "Nkokonjeru",
    #         "status" : "Draft",
    #         "comment" : "We win"
    #     }
    #     resp = self.app.post('/red-flags', data=json.dumps(red_flag), content_type='application/json')
    #     self.assertEqual(
    #         resp.data.decode(), {"error":"field missing."})

    # def test_authenticate_incident_user_id(self):
    #     """ Test method to test delivery order with user id as empty string."""
    #     red_flag = {
    #         "incident_id" : 2,
    #         "created_on" : "ddsd",
    #         "created_by" : 1,
    #         "record_type" : "RedFlag",
    #         "location" : "Nkokonjeru",
    #         "status" : "Draft",
    #         "comment" : "We win"
    #     }
    #     resp = self.app.post('/red-flags', data=json.dumps(red_flag), content_type='application/json')
    #     self.assertEqual(
    #         resp.data.decode(), {"error":"User ID, incident weight and Price quote must be an int."})

    # def test_authenticate_incident_weight(self):
    #     """ Test method to test delivery order with incident weight as string."""
    #     red_flag = {
    #         "incident_id" : 2,
    #         "created_on" : "ddsd",
    #         "created_by" : 1,
    #         "record_type" : "RedFlag",
    #         "location" : "Nkokonjeru",
    #         "status" : "Draft",
    #         "comment" : "We win"
    #     }
    #     resp = self.app.post('/red-flags', data=json.dumps(red_flag), content_type='application/json')
    #     self.assertEqual(
    #         resp.data.decode(), {"error":"User ID, incident weight and Price quote must be an int."})

    # def test_authenticate_incident_price_quote(self):
    #     """ Test method to test delivery order without a price quote."""
    #     red_flag = {
    #         "incident_id" : 2,
    #         "created_on" : "ddsd",
    #         "created_by" : 1,
    #         "record_type" : "RedFlag",
    #         "location" : "Nkokonjeru",
    #         "status" : "Draft",
    #         "comment" : "We win"
    #     }
    #     resp = self.app.post('/red-flags', data=json.dumps(red_flag), content_type='application/json')
    #     self.assertEqual(
    #         resp.data.decode(), {"error":"User ID, incident weight and Price quote must be an int."})

    # def test_authenticate_incident_status_missing(self):
    #     """ Test method to test delivery order without a status"""
    #     red_flag = {
    #         "incident_id" : 2,
    #         "created_on" : "ddsd",
    #         "created_by" : 1,
    #         "record_type" : "RedFlag",
    #         "location" : "Nkokonjeru",
    #         "status" : "Draft",
    #         "comment" : "We win"
    #     }
    #     resp = self.app.post('/red-flags', data=json.dumps(red_flag), content_type='application/json')
    #     self.assertEqual(
    #         resp.data.decode(), {"msg":"incident has been added"})

    # def test_get_all_user_by_id(self):
    #     """ Test method to retrieve a user with id 1."""
    #     resp = self.app.get('/users/1')
    #     self.assertEqual(resp.status_code, 200)

    # def test_get_all_nonexistant_user_incidents(self):
    #     """ Test method to retrieve incidents of non existant user."""
    #     resp = self.app.get('/users/9/incidents')
    #     self.assertEqual(resp.data.decode(), {"error":"User not found"})
    #     self.assertEqual(resp.status_code, 200)

    # def test_get_user_with_zero_incidents(self):
    #     """ Test method to retrieve a user with no incident delivery orders yet."""
    #     resp = self.app.get('/users/3/incidents')
    #     self.assertEqual(resp.data.decode(), {"message":"User has no incidents yet."})

    # def test_cancel_nonexistant_incident_delivery(self):
    #     """ Test method to cancel an nonexistant delivery."""
    #     resp = self.app.put('/red-flags/9', data=json.dumps({"boy": "loo"}), content_type='application/json')
    #     self.assertEqual(
    #         resp.data.decode(), {'data': [
    #     {
    #         'Issue': 'You have entered an unknown URL.',
    #         'message': 'Please do contact Derrick Sekidde for more details on this.'
    #     }]})

    # def test_get_incident_by_wrong_id(self):
    #     """ Test method to check wrong id."""
    #     resp = self.app.get('/red-flags/9')
    #     self.assertEqual(resp.data.decode(), {'data': [
    #     {
    #         'Issue': 'You have entered an unknown URL.',
    #         'message': 'Please do contact Derrick Sekidde for more details on this.'
    #     }]})

    # def test_incidents_record_creation(self):
    #     """ Test method  to test status code of created incident order."""
    #     red_flag = {
    #         "incident_id" : 2,
    #         "created_on" : "ddsd",
    #         "created_by" : 1,
    #         "record_type" : "RedFlag",
    #         "location" : "Nkokonjeru",
    #         "status" : "Draft",
    #         "comment" : "We win"
    #     }
    #     resp = self.app.post('/red-flags', data=json.dumps(red_flag), content_type='application/json')
    #     # self.assertEqual(resp.status_code, 201)
    #     self.assertEqual(resp.data.decode(), {"msg":"incident has been added"})

    # def test_retrieve_all_incident_records(self):
    #     """ Test method  fetch all incidents in list."""
    #     resp = self.app.get('/red-flags')
    #     self.assertEqual(resp.status_code, 200)

    def test_get_wrong_url(self):
        """ Test method to check whether incident is in list given its id."""
        resp = self.app.get('/red-fla')
        self.assertEqual(resp.status_code, 404)

    # def tearDown(self):
    #     pass

    def test_fetch_all_redflags(self):
        response= self.app.get('/red-flags',
        content_type='application/json',
        data=json.dumps(self.all_redflags))
        self.assertEqual(response.status_code,200)

    def test_fetch_all_redflags_empty(self):
        response = self.app.get('/red-flags',
        content_type='application/json',
        data=json.dumps(self.empty_list))
        self.assertEqual(len(self.empty_list),0)
    
    def test_fetch_single_redflag(self):
        response= self.app.get('/red-flags/1',data=json.dumps(self.test_redflag))
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.test_redflag,response.data)

    def test_add_redflag(self):
        redflags =[]
        response=self.app.post(
            '/red-flags',
            content_type='application/json',
            data=json.dumps(dict(
                created_on = "2018-11-29 10:04:38.919951",
                created_by = 1,
                record_type = "Redflag",
                location = '123.01.56.78',
                status = "Draft",
                # image = "image goes here",
                # video = "video goes here",
                comment = "Just testing this app."
            )))
        redflags.append(dict)
        self.assertEqual(response.status_code,201)
        self.assertIn(" ", str(response.data))
        self.assertTrue(len(redflags),2)
        self.assertNotEqual("No redflags found",str(response.data))
        
    def test_delete_redflag(self):
        response=self.app.delete('/red-flags/1',
        content_type='application/json',)
        self.assertEqual(response.status_code,200)
        self.assertTrue(len(self.all_redflags),1)
        # self.assertIn("red-flag record has been deleted.", b'(str(response.data))\n')

    def test_delete_redflag_nonexistent(self):
        response=self.app.delete('/red-flags/1',
        content_type='application/json',
        data=json.dumps(self.empty_list))
        self.assertEqual(len(self.empty_list),0)

    def test_retrieve_all_users(self):
        response= self.app.get('/users',
        content_type='application/json',
        data=json.dumps(self.app_users))
        self.assertEqual(response.status_code,200)

    def test_fetch_users_empty_list(self):
        response = self.app.get('/users',
        content_type='application/json',
        data=json.dumps(self.empty_list))
        self.assertEqual(len(self.empty_list),0)
    
    def test_for_single_user(self):
        response= self.app.get('/users/1',data=json.dumps(self.test_user))
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.test_user,response.data)

    def test_signing_up(self):
        my_app_users =[]
        response=self.app.post(
            '/users',
            content_type='application/json',
            data=json.dumps(dict(
                email = "dede@cia.gov",
                first_name = "Greatest",
                is_admin = False,
                last_name = "Coder",
                other_name = "Ever",
                phone_number = "0705828612",
                registered = "2018-11-29 10:10:02.086352",
                user_id = 1,
                user_name = "haxor"
            )))
        my_app_users.append(dict)
        self.assertEqual(response.status_code,201)
        self.assertTrue(len(my_app_users),2)
        self.assertNotEqual("No users found",str(response.data))
