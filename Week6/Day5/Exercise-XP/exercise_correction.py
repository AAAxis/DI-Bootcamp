import psycopg2

HOSTNAME = 'localhost'
PASSWORD = '1948'
DATABASE = 'practice'
USERNAME = 'postgres'


def run_query(query):

    connection = psycopg2.connect(host = HOSTNAME, password =  PASSWORD, dbname =  DATABASE, user = USERNAME)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

    try: 
        results = cursor.fetchall()
        return results
    except:
        pass
    finally:
        print(query)
        connection.close()

class MenuItem:

    def __init__(self, name: str, price: int) -> object:
        self.name = name
        self.price = price

    def save(self):
        q = f"INSERT INTO menu VALUES (default, '{self.name}', {self.price})"
        run_query(q)

    def delete(self):
        q = f"DELETE FROM menu WHERE name = '{self.name}'"
        run_query(q)    

    def update(self, name, price):
        q = f"UPDATE menu set name = '{name}', price = {price} WHERE name = '{self.name}'"
        run_query(q) 

    @classmethod
    def all(cls):
        q = f"SELECT * FROM menu;"
        all = run_query(q) 
        return all 

    @classmethod
    def fetch_by_name(cls, name: str):
        q = f"SELECT * FROM menu where name = '{name}';"
        item = run_query(q) 
        try:
            return item[0]     
        except IndexError:
            return None

def load_manager(name, price) -> MenuItem:
    return MenuItem(name, price)

def show_user_menu():

    output = """
        MENU
    (a) Add item to menu
    (d) Delete item from menu
    (v) View item from menu
    (e) Exit
    ...
    """

    print(output)

def add_item_to_menu():

    name = input('Name of item: ')
    price = int(input(f'The price for {name}'))

    item = load_manager(name, price)
    try:
        item.save()
    except psycopg2.errors.UniqueViolation:
        print("Can't add duplicate item to menu!")

def remove_item_from_menu():

    name = input('Name of item: ')

    item = MenuItem.fetch_by_name(name) # tuple (name, price)
    item = MenuItem(name = item[1], price = item[2])
    if not item:
        raise ValueError(f'There is no such item: {name}')
    item.delete()
  

def show_restaurant_menu():
    print(MenuItem.all())

user_choice = ''

while user_choice.lower() != 'e':
    show_user_menu()

    user_choice = input('Choice: ')

    if user_choice == 'a':
        add_item_to_menu()

    if user_choice == 'd':
        remove_item_from_menu()

    if user_choice == 'v':
        show_restaurant_menu()
else:
    print('GOODBYE!!!')