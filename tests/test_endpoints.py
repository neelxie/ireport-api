""" File to handle tests for incident endpoints. """
import simplejson as json
from .test_structures import TestStructure


class TestIncident(TestStructure):
    """ Test Class for all incidents endpoint"""
    # I could have more testcases or more comments BUT the lines 
    # would be TOO LONG!

    def test_index_endpoint(self):
        """ Test method to test index endpoint of the app."""
        response = self.app.get('/api/v2/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(),
            '{"data":[{"message":"Welcome to the iReporter Site."}],"status":200}\n')
    
    def test_unauthorized_fetch_all_redflags(self):
        """ Test to check route to fetch all incidents."""
        response = self.app.get('/api/v2/red-flags')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data.decode(),
            '{"error":"Unauthorized! Token is missing.","status":401}\n')

    def test_fetch_all_redflags_empty(self):
        """ Test for getting all inicdents while list is empty."""
        empty_list = self.app.get('/api/v2/red-flags' , headers=self.headers)
        self.assertEqual(empty_list.status_code, 200)
        print(empty_list)
        self.assertEqual(
            empty_list.data.decode(),
            '{"data":[{"Message":"sorry! Incidents list is empty."}],"status":200}\n')

    def test_update_nonexistant_comment(self):
        """ Test method to edit red flag comment."""
        comment_error = self.app.patch(
            '/api/v2/red-flags/1/comment', data=json.dumps({'comment': 525}),
                              content_type='application/json' , headers=self.headers)
        self.assertEqual(comment_error.status_code, 400)
        self.assertEqual(
            comment_error.data.decode(),
            '{"error":"New Comment ought to be a valid sentence.","status":400}\n')

        resp = self.app.patch(
            '/api/v2/red-flags/1/comment', data=json.dumps({'comment': "Police Brutality"}),
                              content_type='application/json' , headers=self.headers)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(
            resp.data.decode(),
            '{"error":"Can not change comment of non existant incident.","status":400}\n')

    def test_update_location(self):
        """ Test method to change red flag location."""
        location_error = self.app.patch(
            '/api/v2/red-flags/1/location', data=json.dumps({'location': "entebbe"}),
                              content_type='application/json' , headers=self.headers)
        self.assertEqual(
            location_error.data.decode(),
            '{"error":"New location has to be a float.","status":400}\n')
        resp = self.app.patch(
            '/api/v2/red-flags/1/location', data=json.dumps({'location': 23.012}),
                              content_type='application/json' , headers=self.headers)
        self.assertEqual(
            resp.data.decode(),
            '{"error":"Location of non existant incdent can not be changed.","status":400}\n')

    def test_change_status(self):
        """ Test method to validate status before update."""
        resp = self.app.patch(
            '/api/v2/red-flags/1/status', data=json.dumps({'status': 23.012}),
                              content_type='application/json' , headers=self.headers)
        self.assertEqual(
            resp.data.decode(),
            '{"error":"Status has to be a string of either \\"investigation\\", \\"resolved\\", or \\"rejected\\".","status":400}\n')
        no_user = self.app.patch(
            '/api/v2/red-flags/1/status', data=json.dumps({'status': 'resolved'}),
                              content_type='application/json' , headers=self.headers)
        self.assertEqual(
            no_user.data.decode(),
            '{"error":"Can not change status of an incident that doesnt exist.","status":400}\n')


    def test_get_wrong_url(self):
        """ Test method to check whether incident is in list given its id."""
        resp = self.app.get('/api/v2/red-fla')
        self.assertEqual(resp.status_code, 404)


    def test_fetch_single_redflag_empty_list(self):
        """ Test for checking retrieval of one incident."""
        response = self.app.get('/api/v2/red-flags/1' , headers=self.headers)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data.decode(),
            '{"error":"No incident with that ID was found.","status":400}\n')

    def test_fetch_nonexistant_user_incidents(self):
        """ Test retrieving of user incidents when user is non existant."""
        response = self.app.get('/api/v2/auth/users/9/red-flags', headers=self.headers)
        self.assertEqual(response.data.decode(), '{"error":"No user incidents yet.","status":400}\n')
    

    def test_delete_redflag_nonexistent(self):
        """ Test for fetchng an item while incdents list is empty."""
        response = self.app.delete('/api/v2/red-flags/9',
                                   content_type='application/json', headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_add_redflag(self):
        """ Add a red flag incident."""
        signee = self.sign_up()
        auth_post = self.app.post(
            "/api/v2/red-flags", content_type='application/json',
            data=json.dumps(self.test_redflag), headers=self.headers)
        # would have checked for data returned but its too long
        self.assertEqual(auth_post.status_code, 201) # value from within returned response
        # check if redflags list is not empty
        response = self.app.get('/api/v2/red-flags',
            content_type='application/json', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data) response data too long so...
        one_redflag = self.app.get('/api/v2/red-flags/1',
            content_type='application/json', headers=self.headers)
        self.assertEqual(one_redflag.status_code, 200)
        one_redflag = json.loads(one_redflag.data.decode())
        self.assertEqual(one_redflag.get("status"), 200)
        self.assertIn("Single incdent", one_redflag)
        user_redflags = self.app.get('/api/v2/auth/users/1/red-flags',
            content_type='application/json', headers=self.headers)
        self.assertEqual(user_redflags.status_code, 200)
        # self.assertIn("user incidents", user_redflags.data.decode())
        location_update = self.app.patch(
            '/api/v2/red-flags/1/location', data=json.dumps({'location': 23.0235}),
                headers=self.headers, content_type='application/json')
        self.assertEqual(location_update.status_code, 200)
        location_update = json.loads(location_update.data.decode())
        self.assertEqual(location_update.get("status"), 200)
        self.assertIn("Location Update", location_update)
        update_comment = self.app.patch(
            '/api/v2/red-flags/1/comment', data=json.dumps({'comment': "Police Brutality"}),
            headers=self.headers, content_type='application/json')
        self.assertEqual(update_comment.status_code, 200)
        update_comment = json.loads(update_comment.data.decode())
        self.assertEqual(update_comment.get("status"), 200)
        self.assertIn("Comment Updated", update_comment)
        change_status = self.app.patch('/api/v2/red-flags/1/status', data=json.dumps({'status': "resolved"}),
            headers=self.headers, content_type='application/json')
        self.assertEqual(change_status.status_code, 200)
        self.assertIn("Status Changed", change_status.data.decode())
        location_status_changed = self.app.patch(
            '/api/v2/red-flags/1/location', data=json.dumps({'location': 23.0235}),
            headers=self.headers, content_type='application/json')
        self.assertEqual(
            location_status_changed.data.decode(),
            '{"error":"Can only edit location when incidents status is Draft.","status":400}\n')
        comment_status = self.app.patch(
            '/api/v2/red-flags/1/comment', data=json.dumps({'comment': "Police Brutality"}),
            headers=self.headers, content_type='application/json')
        self.assertEqual(
            comment_status.data.decode(),
            '{"error":"Can only edit comment when incidents status is Draft.","status":400}\n')
        delete_red_flag = self.app.delete('/api/v2/red-flags/1',
            headers=self.headers)
        self.assertEqual(delete_red_flag.status_code, 200)

    def test_post_intervention(self):
        """ Posting an interventon incident."""
        signee = self.sign_up()
        auth_post = self.app.post(
            "/api/v2/interventions", content_type='application/json',
            data=json.dumps(self.test_redflag), headers=self.headers)
        # would have checked for data returned but its too long
        self.assertEqual(auth_post.status_code, 201)
        response = self.app.get('/api/v2/interventions',
            content_type='application/json', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        one_intervention = self.app.get('/api/v2/interventions/1',
            content_type='application/json', headers=self.headers)
        self.assertEqual(one_intervention.status_code, 200)
        user_interventions = self.app.get('/api/v2/auth/users/1/interventions',
            content_type='application/json', headers=self.headers)
        self.assertEqual(user_interventions.status_code, 200)
        location_update = self.app.patch(
            '/api/v2/interventions/1/location', data=json.dumps({'location': 23.0235}),
                headers=self.headers, content_type='application/json')
        self.assertEqual(location_update.status_code, 200)
        update_comment = self.app.patch(
            '/api/v2/interventions/1/comment', data=json.dumps({'comment': "Police Brutality"}),
            headers=self.headers, content_type='application/json')
        self.assertEqual(update_comment.status_code, 200)
        change_status = self.app.patch('/api/v2/interventions/1/status', data=json.dumps({'status': "resolved"}),
            headers=self.headers, content_type='application/json')
        self.assertEqual(change_status.status_code, 200)
        delete_intervention = self.app.delete('/api/v2/interventions/1',
            headers=self.headers)
        self.assertEqual(delete_intervention.status_code, 200)
        

    def test_retrieve_all_users(self):
        """ Test route for fetching all users."""
        response = self.app.get('/api/v2/auth/users', content_type='application/json', headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_fetch_user(self):
        """ Fetch user. """
        response = self.app.get('/api/v2/auth/users/1', content_type='application/json', headers=self.headers)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(),
                         '{"error":"No user by that ID.","status":400}\n')    

    def test_fetch_users_empty_list(self):
        """ Test for when users list is empty and a fetch is attempted."""
        response = self.app.get('/api/v2/auth/users', content_type='application/json', headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_signing_up(self):
        """ Test for fetching a single user."""
        create_ireporter = self.sign_up()
        self.assertEqual(create_ireporter.status_code, 201)
        response = self.app.get('/api/v2/auth/users/1', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        exist = self.app.post(
            "/api/v2/auth/signup",
            content_type='application/json',
            data=json.dumps(self.test_user))
        self.assertEqual(
            exist.data.decode(),
            '{"error":"Either username or email are already in registered.","status":401}\n')
        email_taken = self.app.post(
            "/api/v2/auth/signup",
            content_type='application/json',
            data=json.dumps(self.test_user_email))
        self.assertEqual(
            email_taken.data.decode(),
            '{"error":"Either username or email are already in registered.","status":401}\n')
        attribute_error = self.app.post(
            "/api/v2/auth/signup",
            content_type='application/json',
            data=json.dumps({}))
        self.assertEqual(attribute_error.data.decode(),
            '{"error":"You have not entered this/these user attributes.","missing attributes":"No data was entered or dict is empty.","status":400}\n')
        user_error = self.app.post(
            "/api/v2/auth/signup",
            content_type='application/json',
            data=json.dumps(self.test_user_error))
        self.assertEqual(user_error.data.decode(),
            '{"error":"Firstname should have only letters between 2 and 15 chaarcters.","status":400}\n')
        sign_up_user_error = self.app.post(
            '/api/v2/auth/login', content_type='application/json',
            data=json.dumps(
                {
                    "user_name":"handn",
                    "password":"123456"}))
        self.assertEqual(sign_up_user_error.data.decode(),
            '{"message":"Username and Password have to be valid strings.","status":401}\n')
        

    def test_loggin_in(self):
        """ Test for adding an app user."""
        ireporter = self.user_login()
        self.assertEqual(ireporter.status_code, 200)
        response = json.loads(ireporter.data)
        self.assertEqual(response.get("status"), 200)
        sign_up_password = self.app.post('/api/v2/auth/login',
            content_type='application/json',
            data=json.dumps(
                {
                    "user_name":"haxor",
                    "password":"12dfdf"}))
        self.assertEqual(
            sign_up_password.data.decode(),
            '{"message":"Username and Password have to be valid strings.","status":401}\n')
        sign_up_error = self.app.post(
            '/api/v2/auth/login',
            content_type='application/json',
            data=json.dumps(
                {
                    "user_name": 52556,
                    "password":"12dfdf"}))
        self.assertEqual(
            sign_up_error.data.decode(),
            '{"message":"Username and Password have to be valid strings.","status":401}\n')