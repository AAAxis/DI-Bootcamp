import faker
import psycopg2

fake = faker.Faker(['pt-PT'])


HOSTNAME = 'localhost'
USERNAME = 'yussiroz'
PASSWORD = 'cluster'
DATABASE = 'fake'


    
def execute_query_commit(query: str) -> None:
    try:
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        return connection
    except:
        print('Connection failed')
    
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def execute_query_get(query: str) -> list:

    try:
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        return connection
    except:
        print('Connection failed')
    
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

for i in range(100):
    
    query = f"""
    insert into fake_people values 
    (default, '{fake.first_name()}', '{fake.last_name()}', '{fake.job()}')
    """

    execute_query_commit(query)

query = "select * from fake_people limit 10;"

fake_people = execute_query_get(query)

print(fake_people)
# print("\n".join(fake_people))