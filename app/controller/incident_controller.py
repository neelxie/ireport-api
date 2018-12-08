""" File to hold the incident class controller."""
from flask import jsonify
from flask import request
from ..models.model_incident import RedFlag
from ..models.model_incident import IncidentDB
from ..models.model_incident import Incident
from ..utilities.validation import Valid


class IncidentController:
    """ Class that implements all app logic for incidents."""

    my_list = IncidentDB()
    valid = Valid()

    def __init__(self):
        pass

    def index(self):
        """ function for the index route."""

        data = [{'message': 'Welcome to the iReporter Site.'}]
        return jsonify({
            'data': data,
            'status': 200
        }), 200

    def add_incident(self):
        """ Method to create an incident."""

        data = request.get_json()

        incident_id = len(self.my_list.incidents)+ 1
        created_by = data.get('created_by')
        location = data.get('location')
        image = data.get("image")
        video = data.get("video")
        comment = data.get('comment')

        error = self.valid.check_incident(created_by, location, image, video, comment)
        # incident = self.incident_obj.create_incident(data)
        my_red_flag = RedFlag(
            Incident(
                incident_id,
                created_by,
                comment),
            location,
            image,
            video)
        # Add redflag to list
        self.my_list.incidents.append(my_red_flag)

        if error:
            return jsonify({
                'error': error,
                "status": 400
            }), 400

        return jsonify({
            'status': 201,
            "data": [{'Red Flag successfully created': my_red_flag.to_json()}]
        }), 201


    def get_incidents(self):
        """ This method fetches incident."""

        if len(self.my_list.incidents) < 1:
            return jsonify({
                'data':[{'Message':'sorry! Red Flags list is empty.'}],
                'status': 200
                }), 200

        return jsonify({
            'status': 200,
            'data': [red_flag.to_json() for red_flag in self.my_list.incidents]
        }), 200

    def get_incident(self, incident_id):
        """ Class method to fetch single incident by ID."""

        incident = self.my_list.get_one_incident(incident_id)

        if len(self.my_list.incidents) < 1 or incident is None:
            return jsonify({
                'error':'No Red Flag with that ID was found.',
                'status': 400
                }), 400

        return jsonify({
            'status': 200,
            'Single Red Flag':[incident.to_json()]
        }), 200


    def edit_location(self, incident_id):
        """ Method to change a redflag location."""
        #get data to update with
        new_data = request.get_json()
        
        # fetch item to be updated
        incident = self.my_list.get_one_incident(incident_id)
        if not incident:
            return jsonify({
                "error": "Can not change location of non existant redflag.",
                'status': 400
            }), 400

        # check if incident status is "Draft".
        if incident.status != 'Draft':
            return jsonify({
                "error": "Can only edit location when red flag status is Draft.",
                'status': 400
                }), 400

        #validate the new_data
        location_error = self.valid.update_location(new_data.get('location'))

        if location_error:
            return jsonify({
                "error": location_error,
                "status": 400
            })

        incident.location = new_data.get('location')

        return jsonify({
            "status": 200,
            "data":[{"Success": "Updated red-flag record's location."}]
            }), 200

    def change_comment(self, incident_id):
        """ Method to change a redflag record comment."""
        new_comment = request.get_json()

        incident = self.my_list.get_one_incident(incident_id)
        if not incident:
            return jsonify({
                "error": "Can not change comment of non existant redflag.",
                'status': 400
            }), 400

        if incident.status != 'Draft':
            return jsonify({
                "error": "Can only edit comment when red flag status is Draft.",
                'status': 400
                }), 400

        error = self.valid.validate_comment_update(new_comment.get('comment'))
        if error:
            return jsonify({
                "status": 400,
                "error": error
                }), 400

        incident.incident.comment = new_comment.get('comment')
        return jsonify(
            {
                "data":[{"Success": "Updated red-flag record's comment."}],
                'status': 200
                }), 200

    def delete_incident(self, incident_id):
        """ This is a method to delete a red flag."""

        incident = self.my_list.get_one_incident(incident_id)
        # get list of all items and delete from it
        if incident:
            
            self.my_list.incidents.remove(incident)
            return jsonify({
                "data":[{'Success':'red-flag record has been deleted.'}],
                "status": 200
                }), 200

        return jsonify({
            "error":'No red-flag by that ID in records.',
            "status": 400
        }), 400

    def error_route(self):
        """ function for 404 error."""
        data = [
            {
                'Issue': 'You have entered an unknown URL.',
                'message': 'Please do contact Derrick Sekidde for more details on this.'
            }
        ]
        return jsonify({
            'status': 404,
            'data': data
        }), 404
