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

def product_menu(product__menu_options : str):
    product_menu = """
\n--------------PRODUCT MENU OPTIONS---------------------\n
    Choose option 0/1/2/3/4
    -------------------
    0. RETURN TO MAIN MENU
    1. For Products List
    2. Create new product
    3. Update existing product
    4. Delete existing product
    -------------------"""
    print(product_menu) 
  
    product__menu_options = int(input("Please enter one of the above Product Menu Options: "))
    return product__menu_options

    
def display_products():
    miniproject = connection.cursor()
    miniproject.execute("SELECT * FROM products_copy")
    rows = miniproject.fetchall()
    
    # print colums
    print("\n\n                PRODUCTS TABLE ")
    print("----------------------------------------------")
    print("| {0:<10} | {1:^20} | {2:^6} |".format("Product ID", "Product Name", "Price"))
    print("----------------------------------------------")
    
    # print records
    for row in rows:
        id = row[0]
        name = row[1]
        price = row[2]
        print("| {0:^10} | {1:<20} | {2:<6} |".format(id , name , price))
    print("----------------------------------------------\n")
    miniproject.close()

def add_new_product():
    # Prompt user to add new product name and price
    # Append new product to product list
    display_products()
    print("\n--------------- ADD NEW PRODUCT DETAILS ----------------")
    product_name = str(input("\nEnter new Product Name: "))
    product_price = float(input(f"\nPlease set the price for [ {product_name} ] : "))
    miniproject = connection.cursor()
    miniproject.execute(f"INSERT INTO products_copy (product_name, price) VALUES (\"{product_name}\", {product_price})")
    connection.commit()
    miniproject.close()


def update_product():
    
    display_products()
    print("\n----------------- UPDATE PRODUCT DETAILS ----------------")
    ids = int(input("\nPlease enter Product ID from the product table: "))
    miniproject = connection.cursor()
    miniproject.execute(f"SELECT * FROM products_copy WHERE product_id = {ids} ")
    rows = miniproject.fetchall()

    for row in rows:
        id = row[0]
        name = row[1]
        price = row[2]
        for i in row:
            if i == id:
                continue
            else:
                update = input(f"\nDo you want to update {i} Y, N: ").upper()
                if update == "Y" and i == name:
                    name = input(f"Please enter new product name to replace current [ \"{name}\" ]: ")
                
                elif update == "Y" and i == price:
                    price = float(input(f"Please set price for [ \"{name}\" ]: "))
                    
                else:
                    continue
        miniproject.execute(f"UPDATE products_copy SET product_name = \"{name}\", price = {price} WHERE product_id = {ids}")
        connection.commit()
        miniproject.close()

def delete_product():
    """Print product list to screen
       Prompt user to input Product ID associated with the product name to delete product
       Remove the product from products table"""
    display_products()
    print("\n--------------------- DELETE PRODUCT  -------------------")
    ids = int(input("\nPlease enter Product ID from the product table: "))
    miniproject = connection.cursor()
    miniproject.execute(f"DELETE FROM products_copy WHERE product_id = {ids} ")
    connection.commit()
    miniproject.close()  



  
    
    

