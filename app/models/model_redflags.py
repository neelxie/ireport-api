""" File contains model for red-flag."""

# red flags list
REDFLAGS = []


class Redflag:
    """    Redflags class."""
    # Class constructor

    def __init__(self, record_id, created_on, created_by,
                 record_type, location, status, comment):
        self.record_id = record_id
        self.created_on = created_on
        self.created_by = created_by
        self.record_type = record_type
        self.location = location
        self.status = status
#       Images  =
#       Videos  =
        self.comment = comment
        REDFLAGS.append(self)
