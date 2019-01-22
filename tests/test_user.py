""" File to handle tests for all users endpoints. """
import json
from flask import Flask
from app.views.app_views import create_app
from app.models.model_incident import IncidentDB
from .test_structures import TestStructure


class TestUser(TestStructure):
    """ Test Class user related endpoint"""

    def test_app(self):
        self.assertIsInstance(create_app(), Flask)

    def test_retrieve_all_users(self):
        """ Test route for fetching all users."""
        response = self.app.get('/api/v1/auth/users', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_fetch_user(self):
        """ Fetch user. """
        response = self.app.get('/api/v1/auth/users/1', headers=self.headers)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(),
                         '{"error":"No incidents for user yet.","status":400}\n')

    def test_fetch_users_empty_list(self):
        """ Test for when users list is empty and a fetch is attempted."""
        response = self.app.get('/api/v1/auth/users', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_signing_up(self):
        """ Test for fetching a single user."""
        signing_up_user = self.app.post(
            "/api/v1/auth/signup",
            content_type='application/json',
            data=json.dumps(
                self.test_another_user))
        self.assertEqual(signing_up_user.status_code, 201)
        # self.assertEqual(signing_up_user, "dfhjd")
        response = self.app.get('/api/v1/auth/users/1', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        exist = self.app.post(
            "/api/v1/auth/signup",
            content_type='application/json',
            data=json.dumps(self.test_user))
        self.assertEqual(
            exist.data.decode(),
            '{"error":"User name is already taken.","status":401}\n')
        email_taken = self.app.post(
            "/api/v1/auth/signup",
            content_type='application/json',
            data=json.dumps(self.test_user_email))
        self.assertEqual(
            email_taken.data.decode(),
            '{"error":"Email already has an account.","status":401}\n')
        user_error = self.app.post(
            "/api/v1/auth/signup",
            content_type='application/json',
            data=json.dumps(self.test_user_error))
        self.assertEqual(
            user_error.data.decode(),
            '{"error":"First/Last/Other Name all have to be strings of two letters or more.","status":400}\n')
        sign_up_user_error = self.app.post(
            '/api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(
                {
                    "user_name": "handn",
                    "password": "hhfhhfhf"}))
        self.assertEqual(
            sign_up_user_error.data.decode(),
            '{"message":"Username not found. Please sign up.","status":403}\n')

    def test_loggin_in(self):
        """ Test for adding an app user."""
        ireporter = self.user_login()
        self.assertEqual(ireporter.status_code, 200)
        response = json.loads(ireporter.data)
        # print(response)
        self.assertEqual(response.get("status"), 200)
        sign_up_password = self.app.post(
            '/api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(
                {
                    "user_name": "haxor",
                    "password": "12dfdf"}))
        self.assertEqual(
            sign_up_password.data.decode(),
            '{"message":"Username and Password have to be valid strings.","status":403}\n')
        sign_up_error = self.app.post(
            '/api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(
                {
                    "user_name": 52556,
                    "password": "12dfdf"}))
        self.assertEqual(
            sign_up_error.data.decode(),
            '{"message":"Username and Password have to be valid strings.","status":403}\n')

    # def test_retrieve_users_invalid_token(self):
    #     """ Test route for fetching all users."""
    #     response = self.app.get('/api/v1/auth/users', headers=self.header)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data.decode(), "bfb")
