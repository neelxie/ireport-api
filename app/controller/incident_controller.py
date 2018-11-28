from datetime import datetime
from flask import jsonify
from flask import request
from ..models.model_incident import REDFLAGS
from ..models.model_incident import Incident

empty_list = [{'message':'There are no red flags.'}]
no_item = [{'Error':"No redflag by that ID in REDFLAGS list."}]

def index():
    """ function for the index route."""
    
    data = [{'message': 'Welcome to the iReporter Site.'}]
    return jsonify({
        'data': data,
        'status': 200,
    }), 200
    
def post_redflag():
    """ This method creates a new incident."""

    request_data = request.get_json() 
    incident_id = len(REDFLAGS) + 1
    created_on = str(datetime.now())
    created_by = request_data.get('created_by')
    record_type = 'RedFlag'
    location = request_data.get('location')
    status = 'Draft'
    comment = request_data.get('comment')
    
    my_redflag = Incident(incident_id, created_on, created_by, record_type, location, status, comment)
    REDFLAGS.append(my_redflag.to_dict())
    return jsonify({
        "msg": "start",
        "data": my_redflag.to_dict()
    }), 201

def all_incidents():
    
    if not REDFLAGS:
        return jsonify({
            'status': 200,
            'data': empty_list
        }), 200
    return jsonify({
        'status': 200,
        'All Redflags': REDFLAGS
    }), 200

def one_redflag(incident_id):
    """ Function to fetch a red flag by ID."""
    specific_redflag = [redflag for redflag in REDFLAGS if redflag.get("incident_id") == int(incident_id)]
    if specific_redflag:
        return jsonify({
            "One Redflag": specific_redflag,
            'status': 200
        }), 200
    return jsonify({
        "data": no_item,
        'status': 400
    })

def edit_location(incident_id):  
        """ Method to change a redflag location."""
        new_data = request.get_json()
        for redflag in REDFLAGS:
            if redflag.get("incident_id") == int(incident_id):
                data = redflag
        if data:
            if not data['status'] == 'Draft':
                return jsonify(
                    {"error": "Can only edit location when red flag status is Draft."})
            data['location'] = new_data['location']
            return jsonify(
                {"msg": "Updated red-flag record's location."}), 200
        return jsonify({"error": "Can not change location of non existant redflag."})

def change_comment(incident_id):   
        """ Method to change a redflag record comment."""
        new_data = request.get_json()
        for redflag in REDFLAGS:
            if redflag.get("incident_id") == int(incident_id):
                data = redflag
        if data:
            if not data['status'] == 'Draft':
                return jsonify(
                    {"error": "Can only edit comment when red flag status is Draft."})
            data['comment'] = new_data['comment']
            return jsonify(
                {"msg": "Updated red-flag record's comment."}), 200
        return jsonify({"error": "Can not change comment of non existant redflag."})

def delete_redflag(incident_id):
    for redflag in REDFLAGS:
        if redflag.get("incident_id") == int(incident_id):
            del REDFLAGS[int(incident_id) - 1]
    return jsonify({'message': 'red-flag record has been deleted.'})

def error_route():
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
    })