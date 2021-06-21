""" file doc string. """
from flask import Blueprint
from app.controller.user_controller import UserController
from ..utility.auth import token_required, admin_route
from ..controller.incident_controller import IncidentController
from .intervention_views import MY_TABLE
from .redflag_views import TABLE_NAME


my_user = UserController()
incident_controller = IncidentController()

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route('/signup', methods=['POST'])
def signup():
    """ Registration for new user.
    """
    return my_user.register_user()


@auth_bp.route('/users', methods=['GET'])
@token_required
@admin_route
def app_users():
    """ Route to fetch all users.
    """
    return my_user.fetch_users()


@auth_bp.route('/login', methods=['POST'])
def login():
    """ View for app user to log into their account.
    """
    return my_user.sign_in()


@auth_bp.route('/users/<int:user_id>', methods=['GET'])
@token_required
@admin_route
def fetch_user(user_id):
    """ Admin route to fetch single user.
    """
    return my_user.app_user(user_id)


@auth_bp.route('/users/<int:user_id>/red-flags', methods=['GET'])
@token_required
@admin_route
def user_redflags(user_id):
    """ Method route to retrieve all redflags from a single user.
    """
    return incident_controller.fetch_user_incident(TABLE_NAME, user_id)


@auth_bp.route('/users/<int:user_id>/interventions', methods=['GET'])
@token_required
@admin_route
def interventions_of_single_user(user_id):
    """ Method route to retrieve all interventions created by a single user.
    """
    return incident_controller.fetch_user_incident(MY_TABLE, user_id)
