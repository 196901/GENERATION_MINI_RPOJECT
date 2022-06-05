from sqlite3 import Cursor
import pymysql
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
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

def customer_menu(customer__menu_options : str):
    customer_menu = """
\n--------------CUSTOMER MENU OPTIONS---------------------\n
    Choose option 0/1/2/3/4
    -------------------
    0. RETURN TO MAIN MENU
    1. For Customers List
    2. Create new customer
    3. Update existing customer
    4. Delete existing customer
    5. IMPORT TABLE IN CVS FORMAT
    6. EXPORT CSV FORMAT TO TABLE
    7. Clear Screen
    -------------------"""
    print(customer_menu) 
  
    customer__menu_options = int(input("Please enter one of the above Customer Menu Options: "))
    return customer__menu_options

    
def display_customers():
    # This will display customers table
    miniproject = connection.cursor()
    miniproject.execute("SELECT * FROM customers")
    rows = miniproject.fetchall()
    
    # print colums
    print("\n\n")
    print("                                            CUSTOMERS TABLE "          )
    print("""-------------------------------------------------------------------------------------------------------""")
    print("| {0:^12} | {1:<15} | {2:^45} | {3:^18} |  ".format("Customer ID", "Customer Name", "Customer Address", "Phone Number"))
    print("""-------------------------------------------------------------------------------------------------------""")

    # print records
    for row in rows:
        id = row[0]
        name = row[1]
        address = row[2]
        number = row[3]
        print("| {0:^12} | {1:<15} | {2:<45} | {3:^18} | ".format(id , name, address , number))
        print("""-------------------------------------------------------------------------------------------------------""")
    miniproject.close()

try:
    def add_new_customer():
        # Show customers table
        # Prompt user to add new customer name, address and phone number
        # Add new customer to customers table
        display_customers()
        print("\n--------------- ADD NEW CUSTOMER DETAILS ----------------")
        customer_name = input("\nEnter new Customer Name: ")
        customer_address = input(f"\nPlease enter Customer Address for [ {customer_name} ] : ")
        phone_number = input(f"\nPlease enter Phone Number for [ {customer_name} ] : ")
        miniproject = connection.cursor()
        miniproject.execute(f"INSERT INTO customers (customer_name, customer_address, phone_number) VALUES (\"{customer_name}\", \"{customer_address}\", \"{phone_number}\")")
        connection.commit()
        miniproject.close()
    
    def update_customer():
        
        # Show customers table
        # Prompt user to enter Customer ID to update customer
        # Select specific customer assciated to the Customer ID 
        display_customers()
        print("\n----------------- UPDATE CUSTOMER DETAILS ----------------")
        ids = int(input("\nPlease enter Customer ID from the customer table: "))
        miniproject = connection.cursor()
        miniproject.execute(f"SELECT * FROM customers WHERE customer_id = {ids} ")
        rows = miniproject.fetchall()


        # Loop through the rows and assign variable for each record in the row
        # Loop through each column and ask user to choose to update the column Y/N
        # if Y(yes), update the column 
        # Finally update the records in the table
        for row in rows:
            id = row[0]
            name = row[1]
            address = row[2]
            number = row[3]
            for i in row:
                if i == id:
                    continue
                else:
                    update = input(f"\nDo you want to update {i} Y, N: ").upper()
                    if update == "Y" and i == name:
                        name = input(f"Please enter new customer name to replace current [ \"{name}\" ]: ")
                    
                    elif update == "Y" and i == address:
                        address = input(f"\nPlease enter Customer Address for for [ \"{name}\" ]: ")
                    
                    elif update == "Y" and i == number:
                        number = input(f"\nPlease enter Phone Number for [ \"{name}\" ]: ")
                        
                    else:
                        continue
            miniproject.execute(f"UPDATE customers SET customer_name = \"{name}\", customer_address = \"{address}\", phone_number = \"{number}\" WHERE customer_id = {ids}")
            connection.commit()
            miniproject.close()

    def delete_customer():
        """Print customer list to screen
        Prompt user to input Customer ID associated with the customer name to delete customer
        Remove the customer from customers table"""
        display_customers()
        print("\n--------------------- DELETE CUSTOMER  -------------------")
        ids = int(input("\nPlease enter Customer ID from the customer table: "))
        miniproject = connection.cursor()
        miniproject.execute(f"DELETE FROM customers WHERE customer_id = {ids} ")
        connection.commit()
        miniproject.close()  

except ValueError:
    value_error = "\n*********** YOU ENTERED WRONG VALUE TYPE - PLEASE TRY AGAIN *************"
    print(f"{value_error:1}")

def customer_sqltable_to_csvfile():
    # Select and import all records from customers table to pandas DataFrame
    # Save the records to CSV format

    sql_query = pd.read_sql_query("SELECT * FROM customers", connection)

    headers = ['Customer ID', 'Customer Name', 'Customer Address', 'Phone Number']
    customer_data = pd.DataFrame(sql_query)
    print(f"\n\n----------------------------- CUSTOMERS TABLE CSV FORMAT ---------------------------- \n") 
    print(f" {customer_data} \n\n""")
    customer_data.to_csv("customers.csv", index = False, header = headers)

def customer_from_csvfile_to_sqltable():
    # Reads the customer.csv file into pandas dataframe and creates table (customers_sample_table) with all records in database

    db_data = 'mysql+pymysql://' + 'root' + ':' + 'florim' + '@' + 'localhost' + ':3306/' + 'miniproject' + '?charset=utf8mb4' 
    engine = create_engine(db_data, echo = False)
    df = pd.read_csv("customers.csv")
    data = pd.DataFrame(df)
    data.to_sql(name='customers_sample_table', con=engine, if_exists = 'append', index=False)

