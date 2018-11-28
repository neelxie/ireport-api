""" Routes file."""
from flask import Flask
from flask import request
from flask import jsonify
from app.controller.incident_controller import all_incidents
from app.controller.incident_controller import error_route
from app.controller.incident_controller import index
from app.controller.incident_controller import one_redflag
from app.controller.incident_controller import edit_location
from app.controller.incident_controller import change_comment
from app.controller.incident_controller import delete_redflag
from app.controller.incident_controller import post_redflag

# create app
app = Flask(__name__)

# app.config['SECRET_KEY'] = 'IAM-the-Greatest-Coder-Ever!'


@app.route('/')
def home():
    """ This is the index route."""
    return index()

@app.route('/red-flags', methods=['POST'])
def create_ireport():
    """ Route to create an incident. Specifically for now
        a red flag. """
    # error_data = [{'error': 'No data has been entered.'}]
    # success_data = [{'message': 'Successfully Added.'}]
    # if not request_data:
    #     return jsonify({
    #         'data': error_data,
    #         'status': 400
    #     }), 400
    # return jsonify({
    #     'data': success_data,
    #     'status': 200
    # }), 200
    return post_redflag()

@app.route('/red-flags', methods=['GET'])
def get_all_redflags():
    """ App route to fetch all red flags."""
    return all_incidents()

@app.route('/red-flags/<incident_id>', methods=['GET'])
def get_specific_redflag(incident_id):
    """ This route fetchs a single red flag."""
    return one_redflag(incident_id)

@app.route('/red-flags/<incident_id>/location', methods=['PATCH'])
def new_location(incident_id):
    """ Route to edit red flag location."""
    return edit_location(incident_id)

@app.route('/red-flags/<incident_id>/comment', methods=['PATCH'])
def edit_record_comment(incident_id):
    """ This route changes record comment of a single red flag."""
    return change_comment(incident_id)

@app.route('/red-flags/<incident_id>', methods=['DELETE'])
def delete_record(incident_id):
    """ Route to delete a red flag."""
    return delete_redflag(incident_id)


@app.errorhandler(404)
def page_not_found(e):
    """ Error handler route for this app."""
    return error_route()