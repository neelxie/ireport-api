""" Routes file."""
from flask import Flask, jsonify
from .user_views import auth_bp
from .intervention_views import intervention_bp
from .redflag_views import redflag_bp

# create app
def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(intervention_bp, url_prefix='/api/v1')
    app.register_blueprint(redflag_bp, url_prefix='/api/v1')

    @app.errorhandler(404)
    def page_not_found(e):
        """ Error handler route bad requests."""

        return jsonify({
            'status': 404,
            'data': [
                {
                    'Issue': "You have entered an unknown URL. NOTE all urls have a 'api/v1/' prefix.",
                    'message': 'Please do contact Derrick Sekidde for more details on this.'
                }]
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        """ This is a route handler for wrong methods."""

        return jsonify({
            "status": 405,
            "error": "The used method is not allowed for this endpoint. Change method or contact Derrick Sekidde."
        }), 405

    return app
