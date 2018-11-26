from datetime import datetime
from flask import jsonify
from flask import request
from ..models.model_redflags import REDFLAGS

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

    request_data = request.get_json()
    red = {
        'red_flag_id': len(REDFLAGS) + 1, 
        'created_on': str(datetime.now()),
        'created_by': request_data['created_by'],
        'record_type': 'RedFlag',
        'location': request_data['location'], 
        'status': 'Draft', 
        'comment': request_data['comment ']
    }

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

def one_redflag(red_flag_id):
    specific_redflag = [redflag for redflag in REDFLAGS if redflag.get("red_flag_id") == int(red_flag_id)]
    if specific_redflag:
        return jsonify({
            "One Redflag": specific_redflag,
            'status': 200
        }), 200
    return jsonify({
        "data": no_item,
        'status': 400
    })

def edit_location(red_flag_id):
    
        """ Method to change a redflag location."""
        new_data = request.get_json()
        for redflag in REDFLAGS:
            if redflag.get("red_flag_id") == int(red_flag_id):
                data = redflag
        if data:
            if not data['status'] == 'Draft':
                return jsonify(
                    {"error": "Can only edit location when red flag status is Draft."})
            data['location'] = new_data['location']
            return jsonify(
                {"msg": "Updated red-flag record's location."}), 200
        return jsonify({"error": "Can not cancel non existant redflag order."})

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