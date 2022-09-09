import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'yussiroz'
PASSWORD = 'cluster'
DATABASE = 'Hollywood'

try:
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
except:
    print('Connection failed')


cursor = connection.cursor()

query = "SELECT * FROM actors"

cursor.execute(query)

results = cursor.fetchall()

connection.close()


