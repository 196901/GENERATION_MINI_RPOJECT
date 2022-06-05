import pymysql
import os
import pandas as pd
from sqlalchemy import create_engine
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
    5. CSV FORMAT
    6. Clear Screen
    -------------------"""
    print(product_menu) 
  
    product__menu_options = int(input("Please enter one of the above Product Menu Options: "))
    return product__menu_options

    
def display_products():

    # This will display products table
    miniproject = connection.cursor()
    miniproject.execute("SELECT * FROM products")
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

try:
    def add_new_product():
        # Show products table
        # Prompt user to add new product name and price
        # Add new product to products table
        display_products()
        print("\n--------------- ADD NEW PRODUCT DETAILS ----------------")
        product_name = input("\nEnter new Product Name: ")
        product_price = float(input(f"\nPlease set the price for [ {product_name} ] : "))
        miniproject = connection.cursor()
        miniproject.execute(f"INSERT INTO products (product_name, price) VALUES (\"{product_name}\", {product_price})")
        connection.commit()
        miniproject.close()


    def update_product():
        
        # Show products table
        # Prompt user to enter Product ID to update product
        # Select specific product assciated to the Product ID 
        display_products()
        print("\n----------------- UPDATE PRODUCT DETAILS ----------------")
        ids = int(input("\nPlease enter Product ID from the product table: "))
        miniproject = connection.cursor()
        miniproject.execute(f"SELECT * FROM products WHERE product_id = {ids} ")
        rows = miniproject.fetchall()

        # Loop through the rows and assign variable for each record in the row
        # Loop through each column and ask user to choose to update the column Y/N
        # if Y(yes), update the column 
        # Finally aupdate the records
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
            miniproject.execute(f"UPDATE products SET product_name = \"{name}\", price = {price} WHERE product_id = {ids}")
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
        miniproject.execute(f"DELETE FROM products WHERE product_id = {ids} ")
        connection.commit()
        miniproject.close()  
except ValueError:
    value_error = "\n*********** YOU ENTERED WRONG VALUE TYPE - PLEASE TRY AGAIN *************"
    print(f"{value_error:1}")

def products_sqltable_to_csvfile():
    # Select and import all records from products table to pandas DataFrame
    # Save the records to CSV format
    sql_query = pd.read_sql_query("SELECT * FROM products", connection)
    headers = ['Product ID', 'Product Name', 'Price']
    products_data = pd.DataFrame(sql_query)
    print(f"\n\n-------- PRODUCTS TABLE CSV FORMAT ----------\n") 
    print(f" {products_data} \n\n""")
    products_data.to_csv("products.csv", index = False, header = headers)

def products_from_csvfile_to_sqltable():
    # Reads the products.csv file into pandas dataframe and creates table (products_sample_table) with all records in database
    db_data = 'mysql+pymysql://' + 'root' + ':' + 'florim' + '@' + 'localhost' + ':3306/' + 'miniproject' + '?charset=utf8mb4' 
    engine = create_engine(db_data, echo = False)
    df = pd.read_csv("products.csv")
    data = pd.DataFrame(df)
    data.to_sql(name='products_sample_table', con=engine, if_exists = 'append', index=False)



  
    
    

