import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '1948'
DATABASE = 'practice'

def run_query(query):
    '''connects to the db'''
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

    finally:
        cursor.close()

class menuItem():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def all(cls):
        all_query = "SELECT * FROM menu"
        return run_query(all_query)
    
    @classmethod
    def get_by_name(cls, name):
        get_by_name_query = f"SELECT {self.name} FROM menu"
        return run_query(get_by_name_query)

    def delete(self):
        delete_query = f'DELETE FROM menu WHERE item = {self.name}'
        run_query(delete_query)

    def save (self):
        save_query = f"""insert into menu (item, price) values ('{self.name}', {self.price})"""
        run_query(save_query)


    def update (self, new_price):
        self.price = new_price
        update_query = f"""UPDATE menu set price = {self.price} where item = {self.name}"""
        run_query(update_query)   
    def load_manager(name, price):
        return menuItem
    def show_user_menu():
        output = '''
        MENU
        (a)Add item to menu
        (d)Delete item from menu
        (v)View item from menu
        (e)Exit 
        '''
        print(output)

    def add_item_to_menu():
        name = input('name of item: ')
        price = int(input(f'the price for {name}'))
        item = load_manager(name, price)
        try:
            item.save()
        except psycopg2.errors.UniqueViolation:
            print('Can`t add duplicate item to menu.')

    def remove_item_from_menu():
        name = input('Nem of item: ')
        item = menuItem.fetch_by_name(name)
        item = menuItem(name = item[0], price = item[1])
        try:
            item.delete()
        except psycopg2.errors.Unique
    def show_restaurant_menu():
        print(menuItem.all())
    
    user_choice = ''
    while user_choice.lower() != 'e':
        show_restaurant_menu()
        if user_choice == 'a':
            add_item_to_menu()
        if user_choice == 'd':
            remove_item_from_menu()
        if user_choice == 'v':
            show_reataurant_menu

add_item_to_menu()
remove_item_from_menu()
show_restaurant_menu()


# item = menuItem('Burger', 35)
# item.save()
# # item.delete()
# item.update(37)
# print(item.all())