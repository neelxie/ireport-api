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

    
    def test_unauthorized_fetch_all_redflags(self):
        """ Test to check route to fetch all incidents."""
        response = self.app.get('/api/v1/red-flags')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.data.decode(),
            '{"error":"Unauthorized! Token is missing.","status":401}\n')

    def test_fetch_all_redflags_empty(self):
        """ Test for getting all inicdents while list is empty."""
        response = self.app.get('/api/v1/red-flags', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data.decode(),
            '{"data":[{"Message":"sorry! Red Flags list is empty."}],"status":200}\n')

    def test_update_nonexistant_comment(self):
        """ Test method to edit red flag comment."""
        resp = self.app.patch(
            '/api/v1/red-flags/1/comment', data=json.dumps({'comment': "Police Brutality"}),
                              content_type='application/json', headers=self.headers)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(
            resp.data.decode(),
            '{"error":"Can not change comment of non existant redflag.","status":400}\n')

    def test_update_location(self):
        """ Test method to change red flag location."""
        resp = self.app.patch(
            '/api/v1/red-flags/1/location', data=json.dumps({'location': "entebbe"}),
                              content_type='application/json', headers=self.headers)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(
            resp.data.decode(),
            '{"error":"Location of non existant redflag can not be changed.","status":400}\n')


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
    

    # def test_add_redflag(self):
    #     """ Test method for adding an incident."""
    #     response = self.app.post(
    #         '/api/v1/red-flags',
    #         data=json.dumps(self.test_redflag))
    #     self.assertEqual(response.status_code, 201)
    #     self.assertNotEqual("No redflags found", str(response.data))

    def test_delete_redflag_nonexistent(self):
        """ Test for fetchng an item while incdents list is empty."""
        response = self.app.delete('/api/v1/red-flags/9',
                                   content_type='application/json', headers=self.headers)
        self.assertEqual(response.status_code, 400)

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
        response = self.app.get('/api/v1/red-flags', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data) response data too long so...
        self.assertIsInstance(response.data, bytes)
        self.assertIn("data", response.data.decode()) # the data list in the response
        one_redflag = self.app.get('/api/v1/red-flags/1', headers=self.headers)
        self.assertEqual(one_redflag.status_code, 200)
        one_redflag = json.loads(one_redflag.data.decode())
        self.assertEqual(one_redflag.get("status"), 200)
        self.assertIn("Single Red Flag", one_redflag)
        user_redflags = self.app.get('/api/v1/auth/users/1/red-flags', headers=self.headers)
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
        delete_red_flag = self.app.delete('/api/v1/red-flags/1',
                                          content_type='application/json', headers=self.headers)
        self.assertEqual(delete_red_flag.status_code, 200)
        delete_red_flag = json.loads(delete_red_flag.data.decode())
        self.assertEqual(delete_red_flag.get("status"), 200)
        self.assertIn("incident deleted", delete_red_flag)
