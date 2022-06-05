
from logging import exception
from pydoc import doc
from random import choice
import stat
import pymysql
import os
from sqlalchemy import create_engine
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
    Choose option 0/1/2/3/4/5/6/7/8
    -------------------
    0. RETURN TO MAIN MENU
    1. For Order List
    2. Create new order
    3. Update existing order status
    4. Update existing order
    5. List Orders by Courier
    6. Delete order
    7. CSV FORMAT
    8. Clear Screen
    -------------------"""
    print(order_menu)
        
    order_menu_options = int(input("Please enter one of the above Order Menu Options: "))
    return order_menu_options


def display_orders():

    # This will display orders table
    miniproject = connection.cursor()
    miniproject.execute("SELECT * FROM orders")
    rows = miniproject.fetchall()

    # print columns
    print("\n\n")
    print("                                                                                        ORDERS TABLE "          )
    print("""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
    print("| {0:^8} | {1:<10} | {2:^45} | {3:^18} | {4:^12} | {5:^17} |{6:^48} | ".format("Order ID", "Customer Name", "Customer Address", "Phone Number", "Courier", "Status", "Items"))
    print("""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")

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
        print("""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
    miniproject.close()
  
def display_orders_status():
    # This will display orders_status table
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
    """Takes integer list of one or more comma-separated Product IDs
       and return products names associated to IDs in """
    get_operator = lambda x: '=' if len(x) == 1 else 'IN'
    get_value = lambda x: int(x[0]) if len(x) == 1 else x 
    miniproject = connection.cursor()
    query = 'SELECT product_name FROM products WHERE product_id ' + get_operator(index) + ' %s'
    miniproject.execute(query, (get_value(index),))
    products = miniproject.fetchall()
    my_list = [x for x, in products]
    product = ','.join(my_list)
    miniproject.close()
    return product

def choose_order_status(index):
    """Takes interger status ID associated with order status and returns the 
    status in word string (i.e Preparing, Shipped) """
    miniproject = connection.cursor()
    miniproject.execute(f"SELECT status FROM order_status WHERE id = {index}")
    status = miniproject.fetchone()
    orders_status = ''.join(status)
    miniproject.close()
    return orders_status

def choose_courier(index):
    """Takes interger Courier ID associated with Couriers and returns the 
       courier_name in word string (i.e DPD, DHL) """
    miniproject = connection.cursor()
    miniproject.execute(f"SELECT courier_name FROM couriers WHERE courier_id = {index}")
    courier = miniproject.fetchone()
    courier_name = ''.join(courier)
    miniproject.close()
    return courier_name

def order_list_by_courier():

    # Display orders in ascending order of courier
    miniproject = connection.cursor()
    miniproject.execute("SELECT * FROM orders ORDER BY courier ASC")
    rows = miniproject.fetchall()

    # print columns
    print("\n\n")
    print("                                                                                        ORDERS TABLE "          )
    print("""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
    print("| {0:^8} | {1:<10} | {2:^45} | {3:^18} | {4:^12} | {5:^17} |{6:^48} | ".format("Order ID", "Customer Name", "Customer Address", "Phone Number", "Courier", "Status", "Items"))
    print("""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")

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
        print("""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
    miniproject.close()



try:
    def add_order():
        # Show orders table
        # Prompt user to add new customer name, address and phone number
        display_orders()
        miniproject = connection.cursor()
        print("\n-------------------------Please enter Order details------------------------------ ")
        name = input("\nEnter Customer Name: ")
        address = input("\nEnter Customer Address: ")
        phone_number = input("\nEnter Customer Number: ")  
    
        """Show products table
        Prompt user to enter comma-separated Product IDs to select products and converted into list of integers
        Call the choose_products function and assign items
        Show couriers table, and prompt user to enter courier id - call choose_courier function and assign courier
        Show order_status table, and prompt user to enter  id - call choose_order_satus function and assign status
        """
        display_products()
        product_ids = list(map(int, input("Please enter comma-separated list of Product IDs: ").split(",")))
        items = choose_products(product_ids)
        display_couriers()
        courier_id = int(input("\nPlease enter Courier ID associated with the courier name: "))
        courier = choose_courier(courier_id) 
        display_orders_status()
        status_id = int(input("\nPlease enter ID associated with the status: "))
        status = choose_order_status(status_id)
        miniproject.execute(f"""INSERT INTO orders (customer_name, customer_address, phone_number, courier, status, items) 
                                VALUES (\"{name}\", \"{address}\",\"{phone_number}\", \"{courier}\", \"{status}\", \"{items}\")""")
        connection.commit()
        miniproject.close()
    

    def update_order_status():
        
        # Show orders and orders_status table
        # Prompt user to enter Order ID and status ID
        # Fetch Order Status (i.e Preparing) and assing it to the order_state variable
        # Update the status 
        display_orders()
        print("\n-------------------------- UPDATE ORDER STATUS -------------------------- ")
    
        miniproject = connection.cursor()
        id = int(input("\nPlease enter Order ID: "))
        display_orders_status()
        status_index = int(input("\nPlease enter order status ID: "))
        order_state = choose_order_status(status_index)
        miniproject.execute(f"UPDATE orders SET status = \"{order_state}\" WHERE order_id = {id}")
        connection.commit()
        miniproject.close()


    def update_existing_order():

        # Show orders table
        # Prompt user to enter Order ID to update product
        # Select specific order assciated to the Order ID 
        display_orders()
        print("\n-------------------------- UPDATE ORDER ------------------------------- ")
        order_id = int(input("\nPlease enter Order ID for the order you want to update: "))
        miniproject = connection.cursor()
        miniproject.execute(f"SELECT * FROM orders WHERE order_id = {order_id} ")
        order_rows = miniproject.fetchall()

        # Loop through the rows and assign variable for each record in the row
        # Loop through each column and ask user to choose to update the column Y/N
        # if Y(yes), update the column 
        # Finally update the records in the table
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

            miniproject.execute(f"""UPDATE orders SET customer_name = \"{name}\", customer_address = \"{address}\", 
                                phone_number = \"{phone_number}\", courier = \"{courier}\", items = \"{items}\" WHERE order_id = {order_id}""")
            connection.commit()     
            miniproject.close()                   

    def delete_order():
        # Print order list with its index value
        # Prompt user to enter order index value
        display_orders()
        print("\n----------------------- DELETE ORDER  ---------------------")
        id = int(input("\nPlease enter Order ID: "))
        miniproject = connection.cursor()
        miniproject.execute(f"DELETE FROM orders WHERE order_id = {id} ")
        connection.commit() 
        miniproject.close()

except ValueError:
    value_error = "\n*********** YOU ENTERED WRONG VALUE TYPE - PLEASE TRY AGAIN *************"
    print(f"{value_error:1}")


def order_sqltable_to_csvfile():
    # Select and import all records from customers table to pandas DataFrame
    # Save the records to CSV format
    sql_query = pd.read_sql_query("SELECT * FROM orders", connection)

    headers = ['Order ID', 'Customer Name', 'Customer Address', 'Phone Number', 'Courier', 'Status', 'Items']
    orders_data = pd.DataFrame(sql_query)
    print(f"\n\n---------------------------------------------------------------- ORDERS TABLE CSV FORMAT -------------------------------------------------------------- \n") 
    print(f" {orders_data} \n\n""")
    orders_data.to_csv("orders.csv", index = False, header = headers)

def orders_from_csvfile_to_sqltable():
    # Reads the orders.csv file into pandas dataframe and creates table (orders_sample_table) with all records in database
    db_data = 'mysql+pymysql://' + 'root' + ':' + 'florim' + '@' + 'localhost' + ':3306/' + 'miniproject' + '?charset=utf8mb4' 
    engine = create_engine(db_data, echo = False)
    df = pd.read_csv("orders.csv")
    data = pd.DataFrame(df)
    data.to_sql(name='orders_sample_table', con=engine, if_exists = 'append', index=False)


            