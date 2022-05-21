
from pydoc import doc
from random import choice
import stat
import pymysql
import os
from dotenv import load_dotenv
import pandas as pd
from products import display_products
from couriers import display_couriers
# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
port = os.environ.get("mysql_port")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="florim",
    database="miniproject"
    )

def order_menu(order_menu_options : str):
    order_menu = """
\n-------------- ORDER MENU OPTIONS ---------------------\n
    Choose option 0/1/2/3/4
    -------------------
    0. RETURN TO MAIN MENU
    1. For Oder List
    2. Create new order
    3. Update existing order
    4. Delete existing order
    5. Delete order
    -------------------"""
    print(order_menu)
        
    order_menu_options = int(input("Please enter one of the above Order Menu Options: "))
    return order_menu_options


def display_orders():
    miniproject = connection.cursor()
    miniproject.execute("SELECT * FROM orders_copy")
    rows = miniproject.fetchall()

    # print columns
    print("\n\n")
    print("                                                                                        ORDERS TABLE "          )
    print("""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
    print("| {0:^8} | {1:<10} | {2:^45} | {3:^18} | {4:<12} | {5:^17} |{6:^48} | ".format("Order ID", "Customer Name", "Customer Address", "Phone Number", "Courier", "Status", "Items"))
    print("""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")

    # print records
    for row in rows:
        id = row[0]
        name = row[1]
        address = row[2]
        number = row[3]
        courier = row[4]
        status = row[5]
        items = row[6]
        print("| {0:^8} | {1:<13} | {2:<45} | {3:^18} | {4:^12} | {5:^17} | {6:<48}|".format(id , name, address , number, courier, status, items))
        print("""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
    miniproject.close()
  
def display_orders_status():
    miniproject = connection.cursor()
    miniproject.execute(f"SELECT * FROM order_status")
    rows = miniproject.fetchall()

    # print columns
    print("\n\n      ORDER STATUS TABLE ")
    print("---------------------------------")
    print("| {0:^10} | {1:^16} |".format("ID", "Status"))
    print("---------------------------------")

    # print records
    for row in rows:
        id = row[0]
        status = row[1]
        print("| {0:^10} | {1:<16} |".format(id , status))
    print("---------------------------------\n")
    miniproject.close()

def choose_products(index):
    get_operator = lambda x: '=' if len(x) == 1 else 'IN'
    get_value = lambda x: int(x[0]) if len(x) == 1 else x 
    miniproject = connection.cursor()
    query = 'SELECT product_name FROM products_copy WHERE product_id ' + get_operator(index) + ' %s'
    # query = f"SELECT product_name FROM products_copy WHERE product_id in {repr(tuple(map(str, index)))}"
    miniproject.execute(query, (get_value(index),))
    products = miniproject.fetchall()
    my_list = [x for x, in products]
    product = ','.join(my_list)
    miniproject.close()
    return product

def choose_order_status(index):
    miniproject = connection.cursor()
    miniproject.execute(f"SELECT status FROM order_status WHERE id = {index}")
    status = miniproject.fetchone()
    orders_status = ''.join(status)
    miniproject.close()
    return orders_status

def choose_courier(index):
    miniproject = connection.cursor()
    miniproject.execute(f"SELECT courier_name FROM couriers_copy WHERE courier_id = {index}")
    courier = miniproject.fetchone()
    courier_name = ''.join(courier)
    miniproject.close()
    return courier_name


def add_order():
    # Prompt user to enter Customer Name, Address, Phone Number
    display_orders()
    miniproject = connection.cursor()
    print("\n-------------------------Please enter Order details------------------------------ ")
    name = input("\nEnter Customer Name: ")
    address = input("\nEnter Customer Address: ")
    phone_number = input("\nEnter Customer Number: ")  
   
    # Print products list with its index value
    # Prompt user to enter products index values separated by commas to select products
    # Print couriers list with its index value
    # Prompt user to enter courier index value to select courier
    # Set Order Status to be preparing
    display_products()
    product_ids = list(map(int, input("Please enter comma-separated list of Product IDs: ").split(",")))
    items = choose_products(product_ids)
    display_couriers()
    courier_id = int(input("\nPlease enter Courier ID associated with the courier name: "))
    courier = choose_courier(courier_id) 
    display_orders_status()
    status_id = int(input("\nPlease enter ID associated with the status: "))
    status = choose_order_status(status_id)
    # sql = f"""INSERT INTO orders_copy (customer_name, customer_address, phone_number, courier, status, items) VALUES (\"{name}\", \"{address}\",\"{phone_number}\", \"{courier}\", \"{status}\", \"{items}\")"""
    miniproject.execute(f"""INSERT INTO orders_copy (customer_name, customer_address, phone_number, courier, status, items) 
                            VALUES (\"{name}\", \"{address}\",\"{phone_number}\", \"{courier}\", \"{status}\", \"{items}\")""")
    connection.commit()
    miniproject.close()



def update_order_status():
    
    # Print order list with its index value
    # Prompt user to enter order index value 
    display_orders()
    print("\n-------------------------- UPDATE ORDER STATUS -------------------------- ")
    miniproject = connection.cursor()
    id = int(input("\nPlease enter Order ID: "))
    display_orders_status()
    status_index = int(input("\nPlease enter order status index value: "))
    order_state = choose_order_status(status_index)
    # sql = f"UPDATE orders_copy SET status = \"{order_state}\" WHERE order_id = {id}"
    miniproject.execute(f"UPDATE orders_copy SET status = \"{order_state}\" WHERE order_id = {id}")
    connection.commit()
    miniproject.close()


def update_existing_order():
    display_orders()
    print("\n-------------------------- UPDATE ORDER ------------------------------- ")
    # Print order list with its index value
    # Prompt user to enter order index value to update existing order
    order_id = int(input("\nPlease enter Order ID for the order you want to update: "))
    miniproject = connection.cursor()
    miniproject.execute(f"SELECT * FROM orders_copy WHERE order_id = {order_id} ")
    order_rows = miniproject.fetchall()
  
    for row in order_rows:
        id = row[0]
        name = row[1]
        address = row[2]
        phone_number = row[3]
        courier = row[4]
        status = row[5]
        items = row[6]

        for i in row:
            if i == id or i == status:
                continue
            else:
                update = input(f"\nDo you want to update {i} Y, N: ").upper()
                if update == "Y" and i == name:
                    name = input(f"Please enter new Customer Name to replace current name [ \"{name}\" ]: ")
                elif update == "Y" and i == address:
                    address = input(f"Please enter new address to replace current address [ \"{address}\" ]: ")
                elif update == "Y" and i == phone_number:
                    phone_number = input(f"Please enter new number to replace current number [ \"{phone_number}\" ]: ")
                elif update == "Y" and i == courier:
                    display_couriers()
                    courier_id = int(input(f"Please enter new Courier ID to replace current courier[ \"{courier}\" ]: "))
                    courier = choose_courier(courier_id)
                elif update == "Y" and i == items:
                    display_products()
                    product_ids = list(map(int, input("Please enter comma-separated list of Product IDs: ").split(",")))
                    items = choose_products(product_ids)
                else:
                    continue  

        miniproject.execute(f"""UPDATE orders_copy SET customer_name = \"{name}\", customer_address = \"{address}\", 
                             phone_number = \"{phone_number}\", courier = \"{courier}\", items = \"{items}\" WHERE order_id = {order_id}""")
        connection.commit()     
        miniproject.close()                     
update_existing_order()
def delete_order():
    # Print order list with its index value
    # Prompt user to enter order index value
    display_orders()
    print("\n----------------------- DELETE ORDER  ---------------------")
    id = int(input("\nPlease enter Order ID: "))
    miniproject = connection.cursor()
    miniproject.execute(f"DELETE FROM orders_copy WHERE order_id = {id} ")
    connection.commit() 
    miniproject.close()