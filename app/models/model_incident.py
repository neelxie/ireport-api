""" File contains model for red-flag."""

import datetime

# incidents list
incidents = [
    {
        "comment": "silliness",
        "created_by": 1,
        "created_on": "2018-11-29 10:04:38.919951",
        "incident_id": 1,
        "image" : "image.jpg",
        "video" : "video.mp4",
        "location": "waka",
        "record_type": "RedFlag",
        "status": "Draft"
    },
    {
        "comment": "goodness",
        "created_by": 1,
        "created_on": "2018-11-29 10:10:02.086352",
        "incident_id": 2,
        "location": "yapp",
        "image" : "image.jpg",
        "video" : "video.mp4",
        "record_type": "RedFlag",
        "status": "Draft"
    }
]


class IncidentModel:
    """ Incidents class."""

    # Class constructor
    def __init__(self):
        self.incidents = incidents

    def create_incident(self, args):
        """ class method to create a red flag incident."""
        incident = dict(
            incident_id=len(incidents) + 1,
            created_on=str(datetime.datetime.now()),
            created_by=args['created_by'],
            record_type='RedFlag',
            location=args['location'],
            image = ["image"],
            video = ["video"],
            status='Draft',
            comment=args['comment']
        )

        incidents.append(incident)

        return incident

    def get_incidents(self):
        """ This method of the class gets all incidents."""
        return self.incidents

    def get_incident(self, incident_id):
        """ Method to get an incident by ID."""

        for incident in incidents:
            if incident['incident_id'] == incident_id:
                return incident

        return None
