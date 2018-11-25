from datetime import datetime
from models.model_redflags import Redflag
from models.model_redflags import REDFLAGS

def post_redflag():

    request_data = request.get_json()
    red = dict(
        'record_id': len(REDFLAGS) + 1, 
        'created_on': str(datetime.now()),
        'created_by': request_data['created_by'],
        'record_type': 'RedFlag',
        'location': request_data['location'], 
        'status': 'Draft', 
        'comment': request_data['comment ']
    )
    red
    