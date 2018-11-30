""" File contains a utility class for helper functions."""

import re
from flask import jsonify

class Valid:
    """ Validation class for app."""

    def check_item(self, item):
        """ Method to check whether item is not None
            or valid or empty."""
        if isinstance(item, list) and len(item) < 1:
            return False
            
        if  not item or item is None:
            return False

    def check_valid_string(self, name):
        """ Method to validate string."""
        if not isinstance(name, str):
            return False

    # def check_update(self, item):
    #     """ Method to validate PATCH data."""
    #     if not isinstance(item, dict) or #len(item) != 1:
    #         if isinstance(item['location'], str)
    #             jadgfqhj
    #         if type(dict['comment']) is str:
    #             kfgqjke
    #         item.items()[1]
    #         return False
