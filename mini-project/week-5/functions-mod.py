import csv
import os
import pymysql
from dotenv import load_dotenv

def execute_sql(sql_command,params = None, fetch = False):
    #load environmental variables from .env file
    load_dotenv()
    host_name = os.environ.get("mysql_host")
    database_name = os.environ.get("mysql_db")
    user_name = os.environ.get("mysql_user")
    user_password = os.environ.get("mysql_pass")

    #make connection to database
    try:
        with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password
            ) as connection:
                #open cursor
                with connection.cursor() as cursor:
                    #execute sql command
                    sql = sql_command
                    cursor.execute(sql,params)
                    connection.commit()

                    # Fetch results if fetch is True
                    if fetch:
                        result = cursor.fetchall()
                        return result

    except Exception as e:
        print(f"There was an error: {e}")


#Product functions

def update_products(products):
    #delete table called products
    execute_sql("DROP TABLE IF EXISTS products")
    #create table called products
    execute_sql("""
                CREATE TABLE products(
                product_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price FLOAT NOT NULL,
                qty INT NOT NULL
                )
            """)

    #for product in products
    for product in products:
        #add a row
        execute_sql(
            "INSERT INTO products (name, price, qty) VALUES(%s,%s,%s)",
            (product['name'],product['price'],product['qty'])
            )
def show_updated_products():
    clear_screen()
    print("\nProducts Menu:\n")
    updated_products = get_products()
    for product in updated_products:
        print(f"{product['product_id']} {product['name']}: f{float(product['price']) :. 2f} qty: {product['qty']}")

def get_products():
    #get list of dicts from db and return
    results = execute_sql(
            """SELECT *
            FROM products""",
            fetch = True
            )

    products = [{"product_id": row[0],"name": row[1], "price": row[2], "qty": row[3]} for row in results]
    return products


#Orders functions

def update_orders(orders):
    #delete table called couriers
    execute_sql("DROP TABLE IF EXISTS orders")
    #create table called couriers
    execute_sql("""
                CREATE TABLE orders(
                orders_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(100) NOT NULL,
                Items VARCHAR(100) NOT NULL,
                Contact VARCHAR(100) NOT NULL,
                Address VARCHAR(100) NOT NULL,
                Status VARCHAR (30) NOT NULL,
                Courier VARCHAR(100) NOT NULL,
                Courier_contact VARCHAR(100) NOT NULL
                )
            """)

    #for order in orders
    for order in orders:
        #add a row
        execute_sql(
            "INSERT INTO orders (Name, Items, Contact, Address, Status, Courier, Courier_contact ) VALUES(%s,%s,%s,%s,%s,%s,%s)",
            (order[ 'Name' ],order['Items' ], order[ 'Contact' ],order['Address' ], order['Status' ],order['Courier'],order['Courier_contact'])
            )

def get_orders():
    #get list of dicts from db and return
    results = execute_sql(
            """SELECT *
            FROM orders""",
            fetch = True
            )

    orders = [{"orders_id": row[0], "Name": row[1], "Items": row[2], "Contact": row[3], "Address": row[4], "Status": row[5], "Courier": row[6], "Courier_contact": row[7],} for row in results]
    return orders

def show_order_names():

    clear_screen()
    print("\nCurrent orders:\n")
    updated_orders = get_orders()
    for order in updated_orders:
        print(f"{order['Name']}")

#Courier functions

def update_couriers(couriers):
    #delete table called couriers
    execute_sql("DROP TABLE IF EXISTS couriers")
    #create table called couriers
    execute_sql("""
                CREATE TABLE couriers(
                courier_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                contact VARCHAR(100) NOT NULL
                )
            """)

    #for courier in couriers
    for courier in couriers:
    #add a row
        execute_sql(
            "INSERT INTO couriers (name, contact) VALUES(%s,%s)",
            (courier['name'], courier['contact'])
            )

def get_couriers():
    #get list of dicts from db and return
    results = execute_sql(
            """SELECT *
            FROM couriers""",
            fetch = True
            )

    couriers = [{"courier_id": row[0], "name": row[1], "contact": row[2]} for row in results]
    return couriers

#Menu functions
def show_orders_menu():
    clear_screen()
    #orders will be dict in this list
    orders = []

    # #keep asking for input
    while True:
        clear_screen()
        try:
            order_menu_response = int(input("Orders menu\n\ne - Go back to main mesu\ni - List orders\n2 - New order\n3 - Update order items\n4 - Update order status\n5 - Delete order\n"))
            break

        except ValueError:
            clear_screen()
            print("Please choose from the options.")

    #return to product menu
    if order_menu_response == 0:
        return



def show_main_menu():
    #clear_screen()
    while True:
        try:
            #clear_screen()
            opening_response = int(input(f"Main menu: \n\ne - Exit\n1 - Product Menu\n2 - Order Menu \n3 - Courier Menu \n"))
            return opening_response
        except ValueError:
            clear_screen()
            print("Please choose from the options.")

#Other functions

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#test files open*** implement this in main file
def try_open(*args):
    for file in args:

        try:
            with open(file, "r",newline='') as file:
                pass

        except FileNotFoundError:
            print(f"{file} not found in current directory")
            exit()

        except Exception as e:
            print(f"An Error occurred: {e}")
            exit()