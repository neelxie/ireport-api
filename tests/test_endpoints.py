""" File to handle tests for incident endpoints. """

# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)
# warnings.simplefilter("ignore", DeprecationWarning)

import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", message="", category=DeprecationWarning, module="jwt")
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

    
    def test_unauthorized_fetch_all_redflags(self):
        """ Test to check route to fetch all incidents."""
        response = self.app.get('/api/v1/red-flags')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.data.decode(),
            '{"error":"Unauthorized! Token is missing.","status":401}\n')

    def test_fetch_all_redflags_empty(self):
        """ Test for getting all inicdents while list is empty."""
        empty_list = self.app.get('/api/v1/red-flags', headers=self.headers)
        self.assertEqual(empty_list.status_code, 200)
        self.assertEqual(
            empty_list.data.decode(),
            '{"data":[{"Message":"sorry! Red Flags list is empty."}],"status":200}\n')

    def test_update_nonexistant_comment(self):
        """ Test method to edit red flag comment."""
        comment_error = self.app.patch(
            '/api/v1/red-flags/1/comment', data=json.dumps({'comment': 525}),
                              content_type='application/json', headers=self.headers)
        self.assertEqual(comment_error.status_code, 400)
        self.assertEqual(
            comment_error.data.decode(),
            '{"error":"New Comment ought to be a valid sentence.","status":400}\n')

        resp = self.app.patch(
            '/api/v1/red-flags/1/comment', data=json.dumps({'comment': "Police Brutality"}),
                              content_type='application/json', headers=self.headers)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(
            resp.data.decode(),
            '{"error":"Can not change comment of non existant redflag.","status":400}\n')

    def test_update_location(self):
        """ Test method to change red flag location."""
        location_error = self.app.patch(
            '/api/v1/red-flags/1/location', data=json.dumps({'location': "entebbe"}),
                              content_type='application/json', headers=self.headers)
        self.assertEqual(
            location_error.data.decode(),
            '{"error":"New location has to be a float.","status":400}\n')
        resp = self.app.patch(
            '/api/v1/red-flags/1/location', data=json.dumps({'location': 23.012}),
                              content_type='application/json', headers=self.headers)
        self.assertEqual(
            resp.data.decode(),
            '{"error":"Location of non existant redflag can not be changed.","status":400}\n')

    def test_change_status(self):
        """ Test method to validate status before update."""
        resp = self.app.patch(
            '/api/v1/red-flags/1/status', data=json.dumps({'status': 23.012}),
                              content_type='application/json', headers=self.headers)
        self.assertEqual(
            resp.data.decode(),
            '{"error":"Status has to be a string of either \\"investigation\\", \\"resolved\\", or \\"rejected\\".","status":400}\n')
        no_user = self.app.patch(
            '/api/v1/red-flags/1/status', data=json.dumps({'status': 'resolved'}),
                              content_type='application/json', headers=self.headers)
        self.assertEqual(
            no_user.data.decode(),
            '{"error":"Can not change status of an incident that doesnt exist.","status":400}\n')


    def test_get_wrong_url(self):
        """ Test method to check whether incident is in list given its id."""
        resp = self.app.get('/api/v1/red-fla')
        self.assertEqual(resp.status_code, 404)


    def test_fetch_single_redflag_empty_list(self):
        """ Test for checking retrieval of one incident."""
        response = self.app.get('/api/v1/red-flags/1', headers=self.headers)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data.decode(),
            '{"error":"No Red Flag with that ID was found.","status":400}\n')

    def test_fetch_nonexistant_user_incidents(self):
        """ Test retrieving of user incidents when user is non existant."""
        response = self.app.get('/api/v1/auth/users/9/red-flags', headers=self.headers)
        self.assertEqual(response.data.decode(), '{"error":"No user with that ID","status":400}\n')
    

    def test_delete_redflag_nonexistent(self):
        """ Test for fetchng an item while incdents list is empty."""
        response = self.app.delete('/api/v1/red-flags/9',
                                   content_type='application/json', headers=self.headers)
        self.assertEqual(response.status_code, 400)

    # def test_add_redflag_error(self):
    #     error_incident = self.app.post(
    #         "/api/v1/red-flags", content_type='application/json',
    #         headers=self.headers, data=json.dumps(self.test_error_redflag))
    #     self.assertEqual(error_incident.status_code, 400)
    #     self.assertEqual(
    #         error_incident.data.decode(),
    #         '{"error":"Location has to be a valid float.","status":400}\n')
    #     # self.assertEqual(error_incident.get("status"), 201)

    def test_add_redflag(self):
        """ Add a red flag incident."""

        auth_post = self.app.post(
            "/api/v1/red-flags", content_type='application/json',
            headers=self.headers, data=json.dumps(self.test_redflag))
        self.assertEqual(auth_post.status_code, 201)
        response = json.loads(auth_post.data.decode())
        # would have checked for data returned but its too long
        self.assertEqual(response.get("status"), 201) # value from within returned response
        # check if redflags list is not empty
        response = self.app.get(
            '/api/v1/red-flags', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data) response data too long so...
        self.assertIsInstance(response.data, bytes)
        self.assertIn("data", response.data.decode()) # the data list in the response
        one_redflag = self.app.get(
            '/api/v1/red-flags/1', headers=self.headers)
        self.assertEqual(one_redflag.status_code, 200)
        one_redflag = json.loads(one_redflag.data.decode())
        self.assertEqual(one_redflag.get("status"), 200)
        self.assertIn("Single Red Flag", one_redflag)
        user_redflags = self.app.get(
            '/api/v1/auth/users/1/red-flags', headers=self.headers)
        # self.assertEqual(user_redflags.data.decode(), 'gdgdgd')
        self.assertIn("user incidents", user_redflags.data.decode())
        location_update = self.app.patch(
            '/api/v1/red-flags/1/location', data=json.dumps({'location': 23.0235}),
                                         content_type='application/json', headers=self.headers)
        self.assertEqual(location_update.status_code, 200)
        location_update = json.loads(location_update.data.decode())
        self.assertEqual(location_update.get("status"), 200)
        self.assertIn("Location Update", location_update)
        update_comment = self.app.patch(
            '/api/v1/red-flags/1/comment', data=json.dumps({'comment': "Police Brutality"}),
                                        content_type='application/json', headers=self.headers)
        self.assertEqual(update_comment.status_code, 200)
        update_comment = json.loads(update_comment.data.decode())
        self.assertEqual(update_comment.get("status"), 200)
        self.assertIn("Comment Updated", update_comment)
        change_status = self.app.patch('/api/v1/red-flags/1/status', data=json.dumps({'status': "resolved"}),
                                          content_type='application/json', headers=self.headers)
        self.assertEqual(change_status.status_code, 200)
        self.assertIn("Status Changed", change_status.data.decode())
        location_status_changed = self.app.patch(
            '/api/v1/red-flags/1/location', data=json.dumps({'location': 23.0235}),
                                         content_type='application/json', headers=self.headers)
        self.assertEqual(
            location_status_changed.data.decode(),
            '{"error":"Can only edit location when red flag status is Draft.","status":400}\n')
        comment_status = self.app.patch(
            '/api/v1/red-flags/1/comment', data=json.dumps({'comment': "Police Brutality"}),
                                        content_type='application/json', headers=self.headers)
        self.assertEqual(
            comment_status.data.decode(),
            '{"error":"Can only edit comment when red flag status is Draft.","status":400}\n')
        delete_red_flag = self.app.delete('/api/v1/red-flags/1',
                                          content_type='application/json', headers=self.headers)
        self.assertEqual(delete_red_flag.status_code, 200)
        delete_red_flag = json.loads(delete_red_flag.data.decode())
        self.assertEqual(delete_red_flag.get("status"), 200)
        self.assertIn("incident deleted", delete_red_flag)
                # Test for checking errors in creating an incident.
        # error_incident = self.app.post(
        #     "/api/v1/red-flags", content_type='application/json',
        #     headers=self.headers, data=json.dumps(self.test_error_redflag))
        # self.assertEqual(error_incident.status_code, 400)
        # self.assertEqual(
        #     error_incident.data.decode(),
        #     '{"error":"Location has to be a valid float.","status":400}\n')
