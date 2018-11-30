import unittest
from flask import Flask
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
            user_name = "haxor"
        )
        self.empty_list = []
        self.all_redflags=[self.test_redflag, self.test_redflag]
        self.app_users=[self.test_user, self.test_user]
