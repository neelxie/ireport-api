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
                dbname='flask_api', user='postgres', host='localhost', password='', port=5432)
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
            registered TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP);"
        self.cursor.execute(create_table)

        create_table = "CREATE TABLE IF NOT EXISTS redflags \
            (incident_id SERIAL UNIQUE PRIMARY KEY, \
            created_on TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,\
            created_by INTEGER REFERENCES users(user_id), \
            record_type VARCHAR DEFAULT 'redflag', \
            comment VARCHAR(200) NOT NULL, \
            location NUMERIC, \
            image VARCHAR(50), \
            video VARCHAR(50), \
            status VARCHAR DEFAULT 'Draft');"
        self.cursor.execute(create_table)

        create_table = "CREATE TABLE IF NOT EXISTS interventions \
            (incident_id SERIAL UNIQUE PRIMARY KEY, \
            created_on TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, \
            created_by INTEGER REFERENCES users (user_id), \
            record_type VARCHAR DEFAULT 'intervention', \
            comment VARCHAR(200) NOT NULL, \
            location NUMERIC, \
            image VARCHAR(50), \
            video VARCHAR(50), \
            status VARCHAR DEFAULT 'Draft');"
        self.cursor.execute(create_table)

    def add_user(self, first_name, last_name, other_name, phone_number,
                 email, user_name, password, is_admin):
        query = f"INSERT INTO users ( first_name, last_name, other_name, \
        phone_number, email, user_name, password, is_admin)\
         VALUES ('{first_name}', '{last_name}', '{other_name}', '{phone_number}',\
          '{email}', '{user_name}', '{password}', '{is_admin}')RETURNING *; "
        self.cursor.execute(query)


    def add_incident(self, table_name, created_by,
                     comment, location, image, video):

        query = f"""INSERT INTO {table_name} (created_by, comment, location, \
        image, video) VALUES ('{created_by}', '{comment}', \
        {location}, '{image}', '{video}')RETURNING incident_id; """
        self.cursor.execute(query)
        fetched = self.cursor.fetchone()
        return fetched

    def get_incidents(self, table_name):
        query = "SELECT * FROM {};".format(table_name)
        self.cursor.execute(query)
        redflags = self.cursor.fetchall()
        return redflags

    def get_users(self):
        query = "SELECT * FROM users;"
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        return users

    def get_an_incident(self, table_name, incident_id):
        query = "SELECT * FROM {} WHERE incident_id= '{}';".format(table_name, incident_id)
        self.cursor.execute(query)
        red_flag = self.cursor.fetchone()
        return red_flag

    def get_user(self, user_id):
        query = "SELECT * FROM users WHERE user_id = '{}';".format(user_id)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user
    
    def get_user_incidents(self, table_name, created_by):
        query = "SELECT * FROM {} WHERE created_by = '{}';".format(table_name, created_by)
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
        return user_exists

    def update_status(self, table_name, status, incident_id):
        query = "UPDATE {} SET status = '{}' WHERE incident_id = '{}';".format(table_name, status, incident_id)
        self.cursor.execute(query)

    def update_comment(self, table_name, comment, incident_id):
        query = "UPDATE {} SET comment = '{}' WHERE incident_id = '{}';".format(table_name, comment, incident_id)
        self.cursor.execute(query)

    def update_location(self, table_name, location, incident_id):
        query = "UPDATE {} SET location = {} WHERE incident_id = '{}';".format(table_name, location, incident_id)
        self.cursor.execute(query)

    def delete_incident(self, table_name, incident_id):
        query = "DELETE FROM {} WHERE incident_id = '{}';".format(table_name, incident_id)
        self.cursor.execute(query)

    def drop_tables(self):
        query = "DROP TABLE interventions;DROP TABLE redflags;DROP TABLE users;"
        self.cursor.execute(query)
        return "Tables-dropped"

if __name__ == '__main__':
    db = DatabaseConnection()
