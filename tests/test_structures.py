from flask import Flask
import unittest
import simplejson as json
import datetime
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import jwt
from app.utility.auth import my_secret_key
from app.views.app_views import create_app
from app.db.ireporter_db import DatabaseConnection

test_db = DatabaseConnection()
app = create_app()


class TestStructure(unittest.TestCase):

    def setUp(self):
        """ The set up for my app tests."""
        self.app = app.test_client()
        self.test_redflag = dict(
            comment = "Tests for ireporter",
            status="Draft",
            location="kololo",
            image= "image.jpg",
            video= "video.mp4",
            created_on="2018-11-29 09:04:38.919951",
            created_by=1,
        )
        self.test_error_redflag = dict(
            comment = 55,
            status="Draft",
            record_type="RedFlag",
            location=555,
            image= 55,
            video= 55,
            created_on="2018-11-29 09:04:38.919951",
            created_by=1,
        )
        self.test_user = dict(
            email = "dede@cia.gov",
            first_name = "Greatest",
            is_admin = False,
            last_name = "Coder",
            other_name = "Ever",
            phone_number ="0705828612",
            registered = "2018-11-29 10:10:02.086352",
            user_id = 1,
            user_name = "hacker",
            password = "asdfghj"
        )
        self.test_user_email = dict(
            email = "dede@cia.gov",
            first_name = "Greatest",
            is_admin = False,
            last_name = "Coder",
            other_name = "Ever",
            phone_number ="457862556",
            registered = "2018-11-29 10:10:02.086352",
            user_id = 1,
            user_name = "mycoder",
            password = "123456"
        )
        self.test_user_error = dict(
            email = "",
            first_name = "",
            is_admin = 0,
            last_name = "Coder",
            other_name = "Ever",
            phone_number ="0705828612",
            registered = "2018-11-29 10:10:02.086352",
            user_id = 1,
            user_name = "mycoder",
            password = "123456"
        )
        self.token = jwt.encode(
            {"user_id": self.test_user['user_id']}, my_secret_key).decode('UTF-8')
        self.headers = {'Authorization': f'Bearer {self.token}'}
        # self.invalid_token = jwt.encode(
        #     {"user_id": self.test_user['user_id']}, "bcbcb").decode('UTF-8')
        # self.header = {'Authorization': f'Bearer {self.invalid_token}'}
        test_db.create_db_tables()

    def sign_up(self):
        create_ireporter = self.app.post(
            "/api/v2/auth/signup", content_type='application/json', data=json.dumps(self.test_user))
        return create_ireporter

    def user_login(self):
        signed_in = self.sign_up()
        ireporter = self.app.post('/api/v2/auth/login', content_type='application/json', 
            data=json.dumps({"user_name":"hacker", "password":"asdfghj"}))
        return ireporter

    def tearDown(self):
        test_db.drop_tables()
