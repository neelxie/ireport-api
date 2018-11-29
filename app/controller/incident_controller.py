from datetime import datetime
from flask import jsonify
import json
from flask import request, make_response
from ..models.model_incident import IncidentModel

incident_obj = IncidentModel()

class IncidentController:
    def __init__(self):
        self.incidents = []

    def add_incident(self, args):
        """ Method to create an incident."""

        incident = incident_obj.create_incident(args)
        if not incident or incident is None:
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
        if not incidents or len(incidents) < 1 or incidents is None:
            return jsonify({
                'message':'sorry! no incidents were found'
            }), 200
        return jsonify({
            'message': 'success',
            'incidents': incidents
        }), 200

    
    # my_redflag = Incident(incident_id, created_on, created_by, record_type, location, status, comment)
    # REDFLAGS.append(my_redflag.to_dict())
    # return jsonify({
    #     "msg": "start",
    #     "data": my_redflag.to_dict()
    # }), 201

    def get_incident(self, incident_id):
        """ Class method to fetch single incident by ID."""

        incident = incident_obj.get_incident(incident_id)
        if not incident or incident is None:
            return jsonify({
                'message':'sorry! incident with Id not found'
            }), 200
        return jsonify({
            'message': 'success',
            'Single incident': incident
        }), 200
    

# def edit_location(incident_id):  
#         """ Method to change a redflag location."""
#         new_data = request.get_json()
#         for redflag in REDFLAGS:
#             if redflag.get("incident_id") == int(incident_id):
#                 data = redflag
#         if data:
#             if not data['status'] == 'Draft':
#                 return jsonify(
#                     {"error": "Can only edit location when red flag status is Draft."})
#             data['location'] = new_data['location']
#             return jsonify(
#                 {"msg": "Updated red-flag record's location."}), 200
#         return jsonify({"error": "Can not change location of non existant redflag."})

# def change_comment(incident_id):   
#         """ Method to change a redflag record comment."""
#         new_data = request.get_json()
#         for redflag in REDFLAGS:
#             if redflag.get("incident_id") == int(incident_id):
#                 data = redflag
#         if data:
#             if not data['status'] == 'Draft':
#                 return jsonify(
#                     {"error": "Can only edit comment when red flag status is Draft."})
#             data['comment'] = new_data['comment']
#             return jsonify(
#                 {"msg": "Updated red-flag record's comment."}), 200
#         return jsonify({"error": "Can not change comment of non existant redflag."})

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
