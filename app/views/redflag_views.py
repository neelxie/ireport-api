from flask import Blueprint
from ..utility.auth import token_required, admin_route
from app.controller.incident_controller import IncidentController

incedent_controller = IncidentController()

redflag_bp = Blueprint("redflag_bp", __name__)

TABLE_NAME = "redflags"
@redflag_bp.route('/')
def home():
    """ This is the index route.
    """
    return incedent_controller.index()


@redflag_bp.route('/red-flags', methods=['POST'])
@token_required
def create_redflag():
    """ Route to create an incident.
        Specifically for new a red flag.
    """
    return incedent_controller.add_incident(TABLE_NAME)


@redflag_bp.route('/red-flags', methods=['GET'])
@token_required
def get_all_redflags():
    """ App route to fetch all red flags.
    """
    return incedent_controller.get_incidents(TABLE_NAME)


@redflag_bp.route('/red-flags/<int:incident_id>', methods=['GET'])
@token_required
def get_specific_redflag(incident_id):
    """ This route fetchs a single red flag.
    """
    return incedent_controller.get_incident(TABLE_NAME, incident_id)


@redflag_bp.route('/red-flags/<int:incident_id>/location', methods=['PATCH'])
@token_required
def new_location(incident_id):
    """ App Route to edit a red flag location.
    """
    return incedent_controller.edit_location(TABLE_NAME, incident_id)


@redflag_bp.route('/red-flags/<int:incident_id>/comment', methods=['PATCH'])
@token_required
def edit_record_comment(incident_id):
    """ This route changes record comment of a single red flag.
    """
    return incedent_controller.change_comment(TABLE_NAME, incident_id)


@redflag_bp.route('/red-flags/<int:incident_id>/status', methods=['PATCH'])
@token_required
@admin_route
def change_status(incident_id):
    """ This is an Admin only route to change record red flag status.
    """
    return incedent_controller.change_status(TABLE_NAME, incident_id)


@redflag_bp.route('/red-flags/<int:incident_id>', methods=["DELETE"])
@token_required
def delete_record(incident_id):
    """ Route to delete a red flag.
    """
    return incedent_controller.delete_incident(TABLE_NAME, incident_id)
