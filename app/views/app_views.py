""" Routes file."""
from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from .user_views import auth_bp
from .intervention_views import intervention_bp
from .redflag_views import redflag_bp

SWAGGER_URL='/oiuytrfwazcv api/v2/docs'
API_URL='https://app.swaggerhub.com/apis-docs/GreatestCoderEverApi/iReporter/v1.0.1'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
# create app
def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_bp, url_prefix='/api/v2/auth')
    app.register_blueprint(intervention_bp, url_prefix='/api/v2')
    app.register_blueprint(redflag_bp, url_prefix='/api/v2')
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

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
