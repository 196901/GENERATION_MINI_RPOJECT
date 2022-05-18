import pymysql
import os
from dotenv import load_dotenv

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
    -------------------"""
    print(courier_menu) 
  
    courier__menu_options = int(input("Please enter one of the above Courier Menu Options: "))
    return courier__menu_options

def display_couriers():
    miniproject = connection.cursor()
    sql_query = "SELECT * FROM couriers_copy"

    miniproject.execute(sql_query)
    rows = miniproject.fetchall()
    # print(rows)
    print("\n-------------------------------------------")
    print("{0:<10} | {1:^12} | {2:^13} |".format("Courier ID", "Courier Name", "Phone Number"))
    print("-------------------------------------------")

    for row in rows:
        id = row[0]
        name = row[1]
        number = row[2]

        print("{0:^10} | {1:<12} | {2:<13} |".format(id , name , number))
    print("-------------------------------------------\n")
    miniproject.close()
    connection.close()


def add_new_courier():
    # Prompt user to add new product name and price
    # Append new product to product list
    display_couriers()
    print("\n--------------- ADD NEW COURIER DETAILS ----------------")
    courier_name = input("\nEnter new Courier Name: ")
    phone_number = input(f"\nPlease enter the number for [ {courier_name} ] : \n")
    miniproject = connection.cursor()
    sql_query = f"INSERT INTO couriers_copy (courier_name, phone_number) VALUES (\"{courier_name}\", \"{phone_number}\")"
    miniproject.execute(sql_query)
    connection.commit()
    miniproject.close()
    # connection.close()

def update_courier():
    
    display_couriers()
    print("\n----------------- UPDATE COURIER DETAILS ----------------")
    ids = int(input("\nPlease enter Courier ID from the courier table: "))
    miniproject = connection.cursor()
    sql_query = f"SELECT * FROM couriers_copy WHERE courier_id = {ids} "

    miniproject.execute(sql_query)
    rows = miniproject.fetchall()

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
                    new_name = input(f"Please enter new courier name to replace current [ \"{name}\" ]: ")
                    sql = f"UPDATE couriers_copy SET courier_name = \"{new_name}\" WHERE courier_id = {ids}"
                    miniproject.execute(sql)
                    connection.commit() 
                elif update == "Y" and i == number:
                    new_number = input(f"Please enter new number for [ \"{name}\" ]: ")
                    sql2 = f"UPDATE couriers_copy SET phone_number = \"{new_number}\" WHERE courier_id = {ids}"
                    miniproject.execute(sql2)
                    connection.commit() 
                else:
                    continue
    miniproject.close()
    # connection.close()


def delete_courier():
    """Print product list to screen
       Prompt user to input Courier ID associated with the courier name to delete product
       Remove the courier from couriers table"""
    display_couriers()
    print("\n--------------------- DELETE COURIER  -------------------")
    ids = int(input("\nPlease enter Courier ID from the courier table: "))
    miniproject = connection.cursor()
    sql_query = f"DELETE FROM couriers_copy WHERE courier_id = {ids} "

    miniproject.execute(sql_query)
    connection.commit() 

