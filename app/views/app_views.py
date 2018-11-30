""" Routes file."""
from flask import Flask
from flask import request
from flask import jsonify
from app.controller.incident_controller import IncidentController
from app.controller.user_controller import UserController

# create app
app = Flask(__name__)

# app.config['SECRET_KEY'] = 'IAM-the-Greatest-Coder-Ever!'

incendent_controller = IncidentController()
my_user = UserController()

@app.route('/')
def home():
    """ This is the index route."""
    return incendent_controller.index()

@app.route('/red-flags', methods=['POST'])
def create_redflag():
    """ Route to create an incident. Specifically for now
        a red flag. """
    data = request.get_json()
    return incendent_controller.add_incident(data)

@app.route('/red-flags', methods=['GET'])
def get_all_redflags():
    """ App route to fetch all red flags."""
    return incendent_controller.get_incidents()

@app.route('/red-flags/<int:incident_id>', methods=['GET'])
def get_specific_redflag(incident_id):
    """ This route fetchs a single red flag."""
    return incendent_controller.get_incident(incident_id)

@app.route('/users', methods=['POST'])
def signup():
    """ Route to create a user. """
    data = request.get_json()
    return my_user.register_user(data)

@app.route('/users', methods=['GET'])
def app_users():
    """ Route to fetch all users."""
    return my_user.fetch_users()

@app.route('/users/<int:user_id>', methods=['GET'])
def login(user_id):
    """ This route fetchs a single."""
    return my_user.fetch_one_user(user_id)

@app.route('/red-flags/<incident_id>/location', methods=['PATCH'])
def new_location(incident_id):
    """ Route to edit red flag location."""
    return incendent_controller.edit_location(incident_id)

@app.route('/red-flags/<incident_id>/comment', methods=['PATCH'])
def edit_record_comment(incident_id):
    """ This route changes record comment of a single red flag."""
    return incendent_controller.change_comment(incident_id)

@app.route('/red-flags/<int:incident_id>', methods=["DELETE"])
def delete_record(incident_id):
    """ Route to delete a red flag."""
    return incendent_controller.delete_incident(incident_id)


@app.errorhandler(404)
def page_not_found(e):
    """ Error handler route for this app."""
    return incendent_controller.error_route()
    