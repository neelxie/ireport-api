import unittest
import json
from flask import Flask
from flask_jwt_extended import create_access_token, get_jwt_identity
from app.views.app_views import app

class TestStructure(unittest.TestCase):

    def setUp(self):
        """ The set up for my app tests."""
        self.app = app.test_client()
        self.test_redflag = dict(
            comment = "Tests for ireporter",
            status="Draft",
            record_type="RedFlag",
            location="kanjokya",
            image= "image.jpg",
            video= "video.mp4",
            created_on="2018-11-29 09:04:38.919951",
            created_by=1,
        )
        self.test_user = dict(
            email = "dede@cia.gov",
            first_name = "Greatest",
            is_admin = False,
            last_name = "Coder",
            other_name = "Ever",
            phone_number = "0705828612",
            registered = "2018-11-29 10:10:02.086352",
            user_id = 1,
            user_name = "haxor",
            password = "123456"
        )
        # self.token = create_access_token(self.test_user['user_id'])
        # self.header = {'Authorization': f'Bearer {self.token}'}
        self.all_redflags=[self.test_redflag, self.test_redflag]
        self.app_users=[self.test_user, self.test_user]

    def sign_up(self):
        create_ireporter = self.app.post("/api/v1/auth/signup", content_type='application/json', data=json.dumps(self.test_user))
        self.assertEqual(create_ireporter.status_code, 201)
        response = json.loads(create_ireporter.data.decode())
        # self.assertEqual(response["success"][0], "sdjshd")

    def user_login(self):
        self.sign_up()
        ireporter = self.app.post('/api/v1/auth/login', content_type='application/json', 
            data=json.dumps({"user_name":"haxor", "password":"123456"}))
        self.assertEqual(ireporter.status_code, 200)
        # response = json.loads(ireporter.data)
        # self.assertEqual(response['message'], 'You have successfully been logged in as haxor')
        # self.user_access_token = response['access_token']
