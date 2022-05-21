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
    miniproject.execute("SELECT * FROM couriers_copy")
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
 
def add_new_courier():
    # Prompt user to add new product name and price
    # Append new product to product list
    display_couriers()
    print("\n--------------- ADD NEW COURIER DETAILS ----------------")
    courier_name = input("\nEnter new Courier Name: ")
    phone_number = input(f"\nPlease enter the number for [ {courier_name} ] : ")
    miniproject = connection.cursor()
    miniproject.execute(f"INSERT INTO couriers_copy (courier_name, phone_number) VALUES (\"{courier_name}\", \"{phone_number}\")")
    connection.commit()
    miniproject.close()

def update_courier():
    display_couriers()
    print("\n----------------- UPDATE COURIER DETAILS ----------------")
    courier_id = int(input("\nPlease enter Courier ID from the courier table: "))
    miniproject = connection.cursor()
    miniproject.execute(f"SELECT * FROM couriers_copy WHERE courier_id = {courier_id} ")
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
                    name = input(f"Please enter new courier name to replace current [ \"{name}\" ]: ")
                elif update == "Y" and i == number:
                    number = input(f"Please enter new number for [ \"{name}\" ]: ")
                else:
                    continue
               
        miniproject.execute(f"UPDATE couriers_copy SET courier_name = \"{name}\", phone_number = \"{number}\" WHERE courier_id = {courier_id}")
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
    miniproject.execute(f"DELETE FROM couriers_copy WHERE courier_id = {courier_id} ")
    connection.commit() 
    miniproject.close()  
