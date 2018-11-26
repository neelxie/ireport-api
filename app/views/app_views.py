""" Routes file."""
from flask import Flask
from flask import request
from flask import jsonify
from ..controller.app_controller import all_incidents
from ..controller.app_controller import error_route
from ..controller.app_controller import index
from ..controller.app_controller import one_redflag
from ..controller.app_controller import edit_location

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
    error_data = [{'error': 'No data has been entered.'}]
    success_data = [{'message': 'Successfully Added.'}]
    if not request_data:
        return jsonify({
            'data': error_data,
            'status': 400
        }), 400
    return jsonify({
        'data': success_data,
        'status': 200
    }), 200

@app.route('/red-flags', methods=['GET'])
def get_all_redflags():
    """ App route to fetch all red flags."""
    return all_incidents()

@app.route('/red-flags/<red_flag_id>', methods=['GET'])
def get_specific_redflag(red_flag_id):
    """ This route fetchs a single red flag."""
    return one_redflag(red_flag_id)

@app.route('/red-flags/<red_flag_id>/location', methods=['PATCH'])
def new_location(red_flag_id):
    """ This route fetchs a single red flag."""
    return edit_location(red_flag_id)


@app.errorhandler(404)
def page_not_found(e):
    """ Error handler route for this app."""
    return error_route()