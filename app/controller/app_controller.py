from datetime import datetime
from flask import jsonify
# from models.model_redflags import Redflag
# from models.model_redflags import REDFLAGS
from ..models.model_redflags import REDFLAGS

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
        'record_id': len(REDFLAGS) + 1, 
        'created_on': str(datetime.now()),
        'created_by': request_data['created_by'],
        'record_type': 'RedFlag',
        'location': request_data['location'], 
        'status': 'Draft', 
        'comment': request_data['comment ']
    }

def all_incidents():
    empty_list = [{'message':'There are no red flags.'}]
    if not REDFLAGS:
        return jsonify({
            'status': 200,
            'data': empty_list
        }), 200
    return jsonify({
        'status': 200,
        'data': REDFLAGS
    }), 200

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