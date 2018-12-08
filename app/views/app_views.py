""" Routes file."""
from flask import Flask
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
from app.controller.incident_controller import IncidentController
from app.controller.user_controller import UserController

# create app
app = Flask(__name__)
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = 'IAM-the-Greatest-Coder-Ever!'

incendent_controller = IncidentController()
my_user = UserController()

@app.route('/api/v1/')
def home():
    """ This is the index route."""
    return incendent_controller.index()

@app.route('/api/v1/red-flags', methods=['POST'])
@jwt_required
def create_redflag():
    """ Route to create an incident. Specifically for now
        a red flag. """
    return incendent_controller.add_incident()

@app.route('/api/v1/red-flags', methods=['GET'])
@jwt_required
def get_all_redflags():
    """ App route to fetch all red flags."""
    return incendent_controller.get_incidents()

@app.route('/api/v1/red-flags/<int:incident_id>', methods=['GET'])
@jwt_required
def get_specific_redflag(incident_id):
    """ This route fetchs a single red flag."""
    return incendent_controller.get_incident(incident_id)

@app.route('/api/v1/auth/signup', methods=['POST'])
def signup():
    """ Route to create a user. """
    return my_user.register_user()

@app.route('/api/v1/users', methods=['GET'])
# @jwt_required
def app_users():
    """ Route to fetch all users."""
    return my_user.fetch_users()

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    """ This route fetchs a single."""
    return my_user.fetch_one_user()

@app.route('/api/v1/red-flags/<int:incident_id>/location', methods=['PATCH'])
@jwt_required
def new_location(incident_id):
    """ Route to edit red flag location."""
    return incendent_controller.edit_location(incident_id)

@app.route('/api/v1/red-flags/<int:incident_id>/comment', methods=['PATCH'])
@jwt_required
def edit_record_comment(incident_id):
    """ This route changes record comment of a single red flag."""
    return incendent_controller.change_comment(incident_id)

@app.route('/api/v1/red-flags/<int:incident_id>', methods=["DELETE"])
@jwt_required
def delete_record(incident_id):
    """ Route to delete a red flag."""
    return incendent_controller.delete_incident(incident_id)


@app.errorhandler(404)
def page_not_found(e):
    """ Error handler route for this app."""
    return incendent_controller.error_route()
    