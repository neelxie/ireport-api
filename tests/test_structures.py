import unittest
from flask import Flask
from app.views.app_views import app

class TestStructure(unittest.TestCase):

    def test_app(self):
        self.assertIsInstance(app, Flask)