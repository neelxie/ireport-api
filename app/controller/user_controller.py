from flask import jsonify
from flask import request
from datetime import datetime
from ..models.model_users import USERS
from ..models.model_users import Users

def create_user():
    """ This method creates a new app user."""
    user_data = request.get_json() 
    incident_id = len(USERS) + 1
    created_on = str(datetime.now())
    created_by = request_data.get('created_by')
    record_type = 'RedFlag'
    location = request_data.get('location')
    status = 'Draft'
    comment = request_data.get('comment')
    
    my_redflag = Incident(incident_id, created_on, created_by, record_type, location, status, comment)
    USERS.append(my_redflag.to_dict())
    return jsonify({
        "msg": "start",
        "data": my_redflag.to_dict()
    }), 201

def all_incidents():
    
    if not USERS:
        return jsonify({
            'status': 200,
            'data': empty_list
        }), 200
    return jsonify({
        'status': 200,
        'All USERS': USERS
    }), 200

def one_redflag(incident_id):
    """ Function to fetch a red flag by ID."""
    specific_redflag = [redflag for redflag in USERS if redflag.get("incident_id") == int(incident_id)]
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
        for redflag in USERS:
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
        for redflag in USERS:
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
    for redflag in USERS:
        if redflag.get("incident_id") == int(incident_id):
            del USERS[int(incident_id) - 1]
    return jsonify({'message': 'red-flag record has been deleted.'})
