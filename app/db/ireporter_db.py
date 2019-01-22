import psycopg2
import psycopg2.extras
from pprint import pprint
import simplejson as json
import os

class DatabaseConnection:
    def __init__(self):
        
        if os.getenv('DB_NAME') == "test_flask":
            self.db_name = 'test_flask'
        else:
            self.db_name = 'flask_api'

        pprint(self.db_name)
        try:
            self.connection = psycopg2.connect(
                dbname=self.db_name, user='postgres', host='localhost', password='', port=5432)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            print('Connected to the database successfully')
    
        except:
            pprint("Failed to connect to database.")

    def create_db_tables(self):
        create_table = "CREATE TABLE IF NOT EXISTS users \
            ( first_name VARCHAR(50) NOT NULL, \
            last_name VARCHAR(50) NOT NULL, \
            other_name VARCHAR(50), \
            phone_number VARCHAR(50), \
            email VARCHAR(50), \
            user_name VARCHAR(50), \
            password VARCHAR(50), \
            is_admin BOOLEAN NOT NULL, \
            user_id SERIAL PRIMARY KEY, \
            registered VARCHAR(150) NOT NULL);"
        self.cursor.execute(create_table)

        create_table = "CREATE TABLE IF NOT EXISTS incidents \
            (incident_id SERIAL UNIQUE PRIMARY KEY, \
            created_on VARCHAR(50) NOT NULL, \
            created_by integer REFERENCES users (user_id), \
            record_type VARCHAR(10) NOT NULL, \
            comment VARCHAR(200) NOT NULL, \
            location NUMERIC, \
            image VARCHAR(50), \
            video VARCHAR(50), \
            status VARCHAR(30));"
        self.cursor.execute(create_table)

    def add_user(self, first_name, last_name, other_name, phone_number,
                 email, user_name, password, is_admin, registered):
        query = f"INSERT INTO users ( first_name, last_name, other_name, \
        phone_number, email, user_name, password, is_admin, registered)\
         VALUES ('{first_name}', '{last_name}', '{other_name}', '{phone_number}',\
          '{email}', '{user_name}', '{password}', '{is_admin}', '{registered}');"
        self.cursor.execute(query)


    def add_incident(self, created_on, created_by, record_type,
                     comment, location, image, video, status):

        # lat, lon = location.split(',')
        # location = (float(lat), float(lon))
        query = f"INSERT INTO incidents (created_on, created_by, record_type, \
        comment, location, image, video, status) VALUES ('{created_on}', \
        '{created_by}', '{record_type}', '{comment}', {location}, '{image}', '{video}', '{status}');"
        self.cursor.execute(query)
    # cast(location as float)

    def get_incidents(self):
        query = "SELECT * FROM incidents;"
        self.cursor.execute(query)
        redflags = self.cursor.fetchall()
        return redflags

    def get_users(self):
        query = "SELECT * FROM users;"
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        return users

    def get_an_incident(self, incident_id):
        query = "SELECT * FROM incidents WHERE incident_id= '{}';".format(incident_id)
        self.cursor.execute(query)
        red_flag = self.cursor.fetchone()
        return red_flag

    def get_user(self, user_id):
        query = "SELECT * FROM users WHERE user_id = '{}';".format(user_id)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user
    
    def get_user_incidents(self, created_by):
        query = "SELECT * FROM incidents WHERE created_by = '{}';".format(created_by)
        self.cursor.execute(query)
        user_incidents = self.cursor.fetchall()
        return user_incidents

    def check_username(self, user_name):
        query = "SELECT * FROM users WHERE user_name='{}';".format(user_name)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user
    
    def check_email(self, email):
        query = "SELECT * FROM users WHERE email='{}';".format(email)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def login(self, password, user_name):
        query = "SELECT user_name, password FROM users WHERE user_name='{}' and password='{}';".format(user_name, password)
        self.cursor.execute(query)
        user_exists = self.cursor.fetchone()
        pprint(user_exists)
        return user_exists

    def update_status(self, status, incident_id):
        query = "UPDATE incidents SET status = '{}' WHERE incident_id = '{}';".format(status, incident_id)
        self.cursor.execute(query)

    def update_comment(self, comment, incident_id):
        query = "UPDATE incidents SET comment = '{}' WHERE incident_id = '{}';".format(comment, incident_id)
        self.cursor.execute(query)

    def update_location(self, location, incident_id):
        query = "UPDATE incidents SET location = {} WHERE incident_id = '{}';".format(location, incident_id)
        self.cursor.execute(query)

    def delete_incident(self, incident_id):
        query = "DELETE FROM incidents WHERE incident_id = '{}';".format(incident_id)
        self.cursor.execute(query)

    def drop_tables(self):
        query = "DROP TABLE incidents;DROP TABLE users;"
        self.cursor.execute(query)
        return "Tables-dropped"

if __name__ == '__main__':
    db = DatabaseConnection()