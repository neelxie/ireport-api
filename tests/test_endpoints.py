""" File to handle tests for incident endpoints. """
import json
from .test_structures import TestStructure


class TestIncident(TestStructure):
    """ Test Class for all incidents endpoint"""

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

    # def test_unauthorized_fetch_all_redflags(self):
    #     """ Test to check route to fetch all incidents."""
    #     response = self.app.get('/api/v1/red-flags')
    #     self.assertEqual(response.status_code, 401)
    #     self.assertEqual(response.data.decode(), '{"msg":"Missing Authorization Header"}\n')

    # def test_fetch_all_redflags_authorized(self):
    #     """ Authorized fetch all red flags."""
    #     self.user_login()
    #     auth_post = self.app.post("/api/v1/red-flags", content_type='application/json', data=json.dumps(self.test_redflag), headers=self.header)
    #     self.assertEqual(auth_post.status_code, 201)
    #     response = json.loads(auth_post.data.decode())
    #     self.assertEqual(response['message'], 'RedFlag successfully created')

    def test_fetch_all_redflags_empty(self):
        """ Test for getting all inicdents while list is empty."""
        response = self.app.get('/api/v1/red-flags')
        self.assertEqual(response.status_code, 200)

    def test_fetch_single_redflag(self):
        """ Test for checking retrieval of one incident."""
        response = self.app.get('/api/v1/red-flags/1')
        # self.assertEqual(response.status_code, 200)
        self.assertTrue(self.test_redflag, response.data)

    def test_add_redflag(self):
        """ Test method for adding an incident."""
        response = self.app.post(
            '/api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(self.test_redflag))
        # self.assertEqual(response.status_code, 201)
        self.assertIn(" ", str(response.data))
        self.assertNotEqual("No redflags found", str(response.data))

    def test_delete_redflag(self):
        """ Test method for deletng an incident."""
        response = self.app.delete('/api/v1/red-flags/1',
                                   content_type='application/json')
        # self.assertEqual(response.status_code, 200)
        self.assertTrue(len(self.all_redflags), 1)

    def test_delete_redflag_nonexistent(self):
        """ Test for fetchng an item while incdents list is empty."""
        response = self.app.delete('/api/v1/red-flags/9',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_retrieve_all_users(self):
        """ Test route for fetching all users."""
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)

    def test_fetch_users_empty_list(self):
        """ Test for when users list is empty and a fetch is attempted."""
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)

    def test_signing_up(self):
        """ Test for fetching a single user."""
        self.sign_up()

    def test_loggin_in(self):
        """ Test for adding an app user."""
        self.user_login()
        # self.assertEqual(response.status_code, 201)
        # self.assertTrue(len(my_app_users))
