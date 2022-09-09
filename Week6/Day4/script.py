import psycopg2
import re 

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'cluster'
DATABASE = 'users'

def run_query(query):
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    try:
        results = cursor.fetchall()
        connection.close()
        return results
    except:
        connection.close()