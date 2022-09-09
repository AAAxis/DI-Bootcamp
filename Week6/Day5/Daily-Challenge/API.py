import requests

response = requests.get("https://restcountries.com/v3.1/all")

print(response)
#200 = Success
#300 = Redirect
#400 = Error
data = []
for i in range (10):   
    query = f""" insert into countries 
    values (default, '[response[i]['name']]', '{response.capital()}', '{response.flag()}', 
    '{response.flag()}', '{response.subregion()}', '{response.population()}')"""

    execute_query_commit(query)

query = "select * from fake_people limit 10;"

fake_people = execute_query_get(query)

print(fake_people)