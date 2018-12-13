""" File contains model for red-flag."""
from datetime import datetime
from flask_jwt_extended import get_jwt_identity


class IncidentDB:
    """ Incidents list class."""

    # Class constructor
    def __init__(self):
        """ The IncidentDB constructor initializes a list."""
        self.incidents = []

    def get_incidents(self):
        """ Class method to get all incidents in list."""
        return self.get_incidents

    def add_incident(self, incident):
        """ Method to add incident to IncidentsDB list."""
        return self.incidents.append(incident)

    def get_one_incident(self, incident_id):
        """ Method to get an incident by ID."""

        for my_incident in self.incidents:
            if my_incident.incident.incident_id == incident_id:
                return my_incident
        return None


class Incident:
    """ Base class for incidents."""

    def __init__(self, incident_id, comment):
        """ The Constructor for the incident class."""
        self.incident_id = incident_id
        self.comment = comment


class RedFlag:
    """ Red Flags Class"""

    def __init__(self, incident, location, image, video):
        """ The Red Flag class constructor."""

        self.incident = incident
        self.created_on = str(datetime.now())
        self.record_type = "Red-Flag"
        self.location = location
        self.image = image
        self.video = video
        self.status = "Draft"
        self.created_by = get_jwt_identity()
        

    def to_json(self):
        """ Method to change Red flag incident to json for views."""
        
        return {
            "incident_id": self.incident.incident_id,
            "created_on": self.created_on,
            "created_by": self.created_by,
            "record_type": self.record_type,
            "comment": self.incident.comment,
            "location": self.location,
            "image": self.image,
            "video": self.video,
            "status": self.status
        }
