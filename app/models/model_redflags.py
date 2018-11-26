""" File contains model for red-flag."""

import datetime
# red flags list
REDFLAGS = [
    {
        'red_flag_id': 1, 
        'created_on': str(datetime.datetime.now()),
        'created_by': 1,
        'record_type': 'RedFlag',
        'location': '235565', 
        'status': 'Draft', 
        'comment': 'Nepotism'
    }
]


class Incident:
    """    Redflags class."""
    # Class constructor

    def __init__(self, red_flag_id, created_on, created_by,
                 record_type, location, status, comment):
        self.red_flag_id = red_flag_id
        self.created_on = created_on
        self.created_by = created_by
        self.record_type = record_type
        self.location = location
        self.status = status
#       Images  =
#       Videos  =
        self.comment = comment
        REDFLAGS.append(dict(self))
