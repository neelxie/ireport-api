from app.views.app_views import create_app
from app.db.ireporter_db import DatabaseConnection

app = create_app()
db = DatabaseConnection()


if __name__ == '__main__':
    db.create_db_tables()
    app.run(debug=True)