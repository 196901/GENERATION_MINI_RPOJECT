import pymysql
import os
import pandas as pd
from sqlalchemy import create_engine
# from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()
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


def courier_menu(courier__menu_options : str):
    courier_menu = """
\n--------------COURIER MENU OPTIONS---------------------\n
    Choose option 0/1/2/3/4
    -------------------
    0. RETURN TO MAIN MENU
    1. For Couriers List
    2. Create new courier
    3. Update existing courier
    4. Delete existing courier
    5. CSV FORMAT
    6. Clear Screen
    -------------------"""
    print(courier_menu) 
  
    courier__menu_options = int(input("Please enter one of the above Courier Menu Options: "))
    return courier__menu_options

def display_couriers():
    miniproject = connection.cursor()
    miniproject.execute("SELECT * FROM couriers")
    rows = miniproject.fetchall()
    
    # print colums
    print("\n\n               COURIERS TABLE ")
    print("---------------------------------------------")
    print("| {0:<10} | {1:^12} | {2:^13} |".format("Courier ID", "Courier Name", "Phone Number"))
    print("---------------------------------------------")
    
    # print records
    for row in rows:
        id = row[0]
        name = row[1]
        number = row[2]
        print("| {0:^10} | {1:<12} | {2:<13} |".format(id , name , number))
    print("---------------------------------------------\n")
    miniproject.close()
try: 
    def add_new_courier():
        # Prompt user to add new product name and price
        # Append new product to product list
        display_couriers()
        print("\n--------------- ADD NEW COURIER DETAILS ----------------")
        courier_name = input("\nEnter new Courier Name: ")
        phone_number = input(f"\nPlease enter the Phone Number for [ {courier_name} ] : ")
        miniproject = connection.cursor()
        miniproject.execute(f"INSERT INTO couriers (courier_name, phone_number) VALUES (\"{courier_name}\", \"{phone_number}\")")
        connection.commit()
        miniproject.close()

    def update_courier():

        # Show couriers table
        # Prompt user to enter Courier ID to update courier
        # Select specific courier assciated to the Courier ID 
        display_couriers()
        print("\n----------------- UPDATE COURIER DETAILS ----------------")
        courier_id = int(input("\nPlease enter Courier ID from the courier table: "))
        miniproject = connection.cursor()
        miniproject.execute(f"SELECT * FROM couriers WHERE courier_id = {courier_id} ")
        rows = miniproject.fetchall()
        
        # Loop through the rows and assign variable for each record in the row
        # Loop through each column and ask user to choose to update the column Y/N
        # if Y(yes), update the column 
        # Finally update the records in the table
        for row in rows:
            id = row[0]
            name = row[1]
            number = row[2]
            for i in row:
                if i == id:
                    continue
                else:
                    update = input(f"\nDo you want to update {i} Y, N: ").upper()
                    if update == "Y" and i == name:
                        name = input(f"Please enter new courier name to replace current [ \"{name}\" ]: ")
                    elif update == "Y" and i == number:
                        number = input(f"Please enter new number for [ \"{name}\" ]: ")
                    else:
                        continue
                
            miniproject.execute(f"UPDATE couriers SET courier_name = \"{name}\", phone_number = \"{number}\" WHERE courier_id = {courier_id}")
            connection.commit()
            miniproject.close()                

    def delete_courier():
        """Print product list to screen
        Prompt user to input Courier ID associated with the courier name to delete product
        Remove the courier from couriers table"""
        display_couriers()
        print("\n--------------------- DELETE COURIER  -------------------")
        courier_id = int(input("\nPlease enter Courier ID from the courier table: "))
        miniproject = connection.cursor()
        miniproject.execute(f"DELETE FROM couriers WHERE courier_id = {courier_id} ")
        connection.commit() 
        miniproject.close()  
except ValueError:
    value_error = "\n*********** YOU ENTERED WRONG VALUE TYPE - PLEASE TRY AGAIN *************"
    print(f"{value_error:1}")

def courier_sqltable_to_csvfile():
    # Select and import all records from customers table to pandas DataFrame
    # Save the records to CSV format
    sql_query = pd.read_sql_query("SELECT * FROM couriers", connection)

    headers = ['Courier ID', 'Courier Name','Phone Number']
    courier_data = pd.DataFrame(sql_query)
    print(f"\n\n--------- COURIERS TABLE CSV FORMAT ------------\n") 
    print(f" {courier_data} \n\n""")
    courier_data.to_csv("couriers.csv", index = False, header = headers)

def courier_from_csvfile_to_sqltable():

    # Reads the couriers.csv file into pandas dataframe and creates table (couriers_sample_table) with all records in database
    db_data = 'mysql+pymysql://' + 'root' + ':' + 'florim' + '@' + 'localhost' + ':3306/' + 'miniproject' + '?charset=utf8mb4' 
    engine = create_engine(db_data, echo = False)
    df = pd.read_csv("couriers.csv")
    data = pd.DataFrame(df)
    data.to_sql(name='couriers_sample_table', con=engine, if_exists = 'append', index=False)
