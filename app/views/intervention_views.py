from flask import Blueprint
from ..utility.auth import token_required, admin_route
from app.controller.incident_controller import IncidentController

interven_controller = IncidentController()

intervention_bp = Blueprint("intervention_bp", __name__)

MY_TABLE = "interventions"

@intervention_bp.route('/interventions', methods=['POST'])
@token_required
def create_interventions():
    """ Route to create an incident.
        Specifically for new a red flag.
    """
    return interven_controller.add_incident(MY_TABLE)


@intervention_bp.route('/interventions', methods=['GET'])
@token_required
def get_all_interventions():
    """ App route to fetch all interventions.
    """
    return interven_controller.get_incidents(MY_TABLE)


@intervention_bp.route('/interventions/<int:incident_id>', methods=['GET'])
@token_required
def get_specific_intervention(incident_id):
    """ This route fetchs a single intervention.
    """
    return interven_controller.get_incident(MY_TABLE, incident_id)


@intervention_bp.route('/interventions/<int:incident_id>/location', methods=['PATCH'])
@token_required
def new_location(incident_id):
    """ App Route to edit a intervention location.
    """
    return interven_controller.edit_location(MY_TABLE, incident_id)


@intervention_bp.route('/interventions/<int:incident_id>/comment', methods=['PATCH'])
@token_required
def edit_record_comment(incident_id):
    """ This route changes record comment of a single interventions.
    """
    return interven_controller.change_comment(MY_TABLE, incident_id)


@intervention_bp.route('/interventions/<int:incident_id>/status', methods=['PATCH'])
@token_required
@admin_route
def change_status(incident_id):
    """ This is an Admin only route to change record intervention status.
    """
    return interven_controller.change_status(MY_TABLE, incident_id)


@intervention_bp.route('/interventions/<int:incident_id>', methods=["DELETE"])
@token_required
def delete_record(incident_id):
    """ Route to delete a intervention.
    """
    return interven_controller.delete_incident(MY_TABLE, incident_id)
