""" File contains model for red-flag."""

import datetime

# red flags list
REDFLAGS = [
    {
        'incident_id': 1, 
        'created_on': "",
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
    
    def __init__(self, incident_id, created_on, created_by,
                 record_type, location, status, comment):
        self.incident_id = incident_id
        self.created_on = created_on
        self.created_by = created_by
        self.record_type = record_type
        self.location = location
        self.status = status
#       Images  = str()
#       Videos  = str()
        self.comment = comment

    def to_dict(self):
        red_flag = {
            "incident_id" : self.incident_id,
            "created_on" : self.created_on,
            "created_by" : self.created_by,
            "record_type" : self.record_type,
            "location" : self.location,
            "status" : self.status,
#       Images  = str()
#       Videos  = str()
            "comment" : self.comment
        }
        return red_flag
