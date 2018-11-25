""" Routes file."""
from flask import Flask
from flask import request
from flask import jsonify

# create app
app = Flask(__name__)

# app.config['SECRET_KEY'] = 'IAM-the-Greatest-Coder-Ever!'


@app.route('/')
def home():
    """ This is the index route."""
    data = [{'message': 'Welcome to the iReporter Site.'}]
    return jsonify({
        'data': data,
        'status': 200,
    }), 200

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

@app.errorhandler(404)
def page_not_found(e):
    """ Error handle route for this app."""

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