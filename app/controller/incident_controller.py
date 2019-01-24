""" File to hold the incident class controller."""
from flask import jsonify
from flask import request
import simplejson as json
from datetime import datetime
import jwt
from ..utility.validation import Valid
from ..utility.auth import my_secret_key, user_identity
from ..db.ireporter_db import DatabaseConnection

db = DatabaseConnection()


class IncidentController:
    """ Class that implements all app logic for incidents."""

    valid = Valid()

    def __init__(self):
        pass

    def index(self):
        """ function for the index route."""
        # db.drop_tables()
        # db.create_db_tables()

        data = [{'message': 'Welcome to the iReporter Site.'}]
        return jsonify({
            'data': data,
            'status': 200
        }), 200

    def add_incident(self, table_name):
        """ Method to create an incident."""

        incident_request = request.get_json()  # get posted data
        print(type(incident_request))

        location = incident_request.get('location')
        image = incident_request.get("image")
        video = incident_request.get("video")
        comment = incident_request.get('comment')
        payload = user_identity()
        print(payload)
        created_by = payload.get('user_id')

        # Incase of an error return it
        incident_attributes = ["location", "image", "video","comment"]

        my_error_list = self.valid.valdate_attributes(incident_request, incident_attributes)

        if my_error_list is not None:
            return jsonify({
                "status": 400,
                "message": "You have not entered this/these attributes.",
                "error": my_error_list
            }), 400

        error = self.valid.check_if_either_function_has_invalid(
            self.valid.validate_location_and_comment(
                location, comment), self.valid.check_media_file_is_valid(
                    image, video))


        if error:
            return jsonify({
                'error': error,
                "status": 400
            }), 400

        incident_id = db.add_incident(table_name, created_by, comment, location, image, video)

        return jsonify({
            'status': 201,
            "data": [{
                "incident_id": incident_id,
                "message": "Created incident record"}]
        }), 201

    def get_incidents(self, table_name):
        """ This method fetches incident."""

        all_incidents = db.get_incidents(table_name)
        if len(all_incidents) < 1:
            return jsonify({
                'data': [{'Message': 'sorry! Incidents list is empty.'}],
                'status': 200
            }), 200

        return jsonify({
            'status': 200,
            'data': [red_flag for red_flag in all_incidents]
        }), 200

    def get_incident(self, table_name, incident_id):
        """ Class method to fetch single incident by ID."""

        incident = db.get_an_incident(table_name, incident_id)

        if incident is None:
            return jsonify({
                'error': 'No incident with that ID was found.',
                'status': 400
            }), 400

        return jsonify({
            'status': 200,
            'Single incdent': [incident]
        }), 200

    def fetch_user_incident(self, table_name, user_id):
        """ retrieve single user incdents.
        """
        my_list = db.get_user_incidents(table_name, user_id)
        if not my_list:
            return jsonify({
                'status': 400,
                'error': "No user incidents yet."
            }), 400
        return jsonify({
            'status': 200,
            'user incidents': [incident for incident in my_list]
        }), 200

    def edit_location(self, table_name, incident_id):
        """ Method to change a incident location.
        """
        # get data to update with
        new_data = request.get_json()

        # validate the new_data
        location_error = self.valid.validate_location_update(
            new_data.get('location'))

        if location_error:
            return jsonify({
                "error": location_error,
                "status": 400
            })

        # fetch item to be updated
        incident = db.get_an_incident(table_name, incident_id)
        if not incident:
            return jsonify({
                "error": "Location of non existant incdent can not be changed.",
                'status': 400
            }), 400

        # check if incident status is "Draft".
        if incident["status"] != 'Draft':
            return jsonify({
                "error": "Can only edit location when incidents status is Draft.",
                'status': 400
            }), 400

        my_location = new_data.get('location')
        db.update_location(table_name, my_location, incident_id)

        return jsonify({
            "status": 200,
            "Location Update": [{
                "incident_id": incident_id,
                "message": "Updated incidents record's location."}]
        }), 200

    def change_comment(self, table_name, incident_id):
        """ Method to change a incident record comment.
        """
        new_comment = request.get_json()

        error = self.valid.validate_comment_update(new_comment.get('comment'))
        if error:
            return jsonify({
                "status": 400,
                "error": error
            }), 400

        incident = db.get_an_incident(table_name, incident_id)
        if not incident:
            return jsonify({
                "error": "Can not change comment of non existant incident.",
                'status': 400
            }), 400

        if incident["status"]!= 'Draft':
            return jsonify({
                "error": "Can only edit comment when incidents status is Draft.",
                'status': 400
            }), 400

        new_comment = new_comment.get('comment')
        db.update_comment(table_name, new_comment, incident_id)
        return jsonify(
            {
                "Comment Updated": [{
                    "Success": "Updated incidents record's comment.",
                    "incident_id": incident_id
                }],
                'status': 200
            }), 200

    def change_status(self, table_name, incident_id):
        """ Method to change a record status by admin.
        """
        new_status = request.get_json()

        status = new_status.get("status")
        wrong_status = self.valid.validate_status(status)

        if wrong_status:
            return jsonify({
                "error": wrong_status,
                'status': 400
            }), 400

        incident = db.get_an_incident(table_name, incident_id)
        
        if not incident:
            return jsonify({
                "error": "Can not change status of an incident that doesnt exist.",
                'status': 400
            }), 400

        db.update_status(table_name, status, incident_id)
        return jsonify(
            {
                "Status Changed": [{
                    "Success": "incident record has been changed.",
                    "incident_id": incident_id
                }],
                'status': 200
            }), 200

    def delete_incident(self, table_name, incident_id):
        """ This is a method to delete a red flag.
        """
        incident = db.get_an_incident(table_name, incident_id)
        # get list of all items and delete from it
        if incident:

            db.delete_incident(table_name, incident_id)
            return jsonify({
                "incident deleted": [{
                    'Success': 'incident record has been deleted.',
                    "incident_id": incident_id
                }],
                "status": 200
            }), 200

        return jsonify({
            "error": 'Can not delete none existant records.',
            "status": 400
        }), 400
