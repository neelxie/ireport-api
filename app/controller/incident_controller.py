from datetime import datetime
from flask import jsonify
import json
from flask import request, make_response
from ..models.model_incident import IncidentModel
from ..utilities.validation import Valid

incident_obj = IncidentModel()
valid = Valid()

class IncidentController:
    def __init__(self):
        self.incidents = []

    def add_incident(self, args):
        """ Method to create an incident."""

        incident = incident_obj.create_incident(args)
        validate = valid.check_item(incident)
        if validate:
            return jsonify({
                'message':'sorry! no incidents were found'
            }), 200
        return jsonify({
            'message': 'successfully created red flag',
            'incidents': incident
        }), 201
        
    def index(self):
        """ function for the index route."""
    
        data = [{'message': 'Welcome to the iReporter Site.'}]
        return jsonify({
            'data': data,
            'status': 200,
        }), 200
    
    def get_incidents(self):
        """ This method fetches incident."""

        incidents = incident_obj.get_incidents()
        # if not incidents or len(incidents) < 1 or incidents is None:
        validate = valid.check_item(incidents)
        if validate:
            return jsonify({
                'message':'sorry! no incidents were found'}), 200
        return jsonify({
            'message': 'success',
            'incidents': incidents
        }), 200

    def get_incident(self, incident_id):
        """ Class method to fetch single incident by ID."""

        incident = incident_obj.get_incident(incident_id)
        validate = valid.check_item(incident)
        if validate:
            return jsonify({
                'message':'sorry! incident with Id not found'
            }), 200
        return jsonify({
            'message': 'success',
            'Single incident': incident
        }), 200
    

    def edit_location(self, incident_id):  
        """ Method to change a redflag location."""

        #get data to update with
        new_data = request.get_json()
        # fetch item to be updated
        incident = incident_obj.get_incident(incident_id)
        if incident:
            if not incident['status'] == 'Draft':
                return jsonify(
                    {"error": "Can only edit location when red flag status is Draft."}), 400
            incident['location'] = new_data['location']
            return jsonify(
                {"msg": "Updated red-flag record's location."}), 200
        return jsonify({"error": "Can not change location of non existant redflag."}), 400

    def change_comment(self, incident_id):   
        """ Method to change a redflag record comment."""
        new_comment = request.get_json()
        incident = incident_obj.get_incident(incident_id)
        if incident:
            if not incident['status'] == 'Draft':
                return jsonify(
                    {"error": "Can only edit comment when red flag status is Draft."}), 400
            incident['comment'] = new_comment['comment']
            return jsonify(
                {"msg": "Updated red-flag record's comment."}), 200
        return jsonify({"error": "Can not change comment of non existant redflag."}), 400

    def delete_incident(self, incident_id):
        """ This is a method to delete a red flag."""
        # one_red_flag = incident_obj.get_incident(incident_id)
        incident = incident_obj.get_incident(incident_id)
        # get list of all items and delete from it
        incidents = incident_obj.get_incidents()
        if incident:
            incidents.remove(incident)
            return jsonify({
                "data": 'red-flag record has been deleted.',
                "status": 200}), 200
        return jsonify({
            "data": 'No red-flag by that ID in records.',
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
