# MINI PROJECT WEEK 4
import pymysql
# from dotenv import load_dotenv
import sys, os
import products
import couriers
import orders
import customers

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

clear = lambda: os.system('clear')

options = True
while options:
    # main manu options
    main_menu = """
    \n----------------MAIN MENU OPTIONS----------------------\n
    Choose options 0/1/2/3/4/5/6
    -------------------
    0. To EXIT app
    1. For Products Menu
    2. For Couriers Menu 
    3. For Orders Menu
    4. For Customers Menu
    5. SHOW TABLES
    6. Clear Screen
    -------------------"""
    print(main_menu)
        # Prompt user to choose on of the above options
    try:
        main_menu_option = int(input("Please enter one of the above Main Menu Options: "))
    
        if main_menu_option == 0:
            connection.close()
        
            print("\n------------------- EXITING APP -----------------------\n")
            options = False
        
        elif main_menu_option == 1:  
            while main_menu_option == 1:
                
                # PRODUCT MENU OPTIONS
                products_options = ''
                product_options = products.product_menu(products_options)
                    
                if product_options == 0:
                    # Go to the main menu options
                    break

                elif product_options == 1:
                    
                    products.display_products()   

                elif product_options == 2:
                    # Add product
                    products.add_new_product()
                        
                elif product_options == 3:
                    # UPDATE existing product name at index in product list
                    products.update_product()
                
                elif product_options == 4:
                    # DELETE product
                    products.delete_product()
                
                elif product_options == 5:
                    # Import products table in CSV Format
                    products.products_sqltable_to_csvfile()
                
                elif product_options == 6:
                    # Clear the screen
                    clear()
                 
        elif main_menu_option == 2:
            while main_menu_option == 2:

                # COURIERS MENU
                couriers_options = ''
                courier_options = couriers.courier_menu(couriers_options)
                
                if courier_options == 0:
                    # Go to the main menu options
                    break

                elif courier_options == 1:
                    # This will print the courier list
                    couriers.display_couriers()
                
                elif courier_options == 2:
                    # Add courier
                    couriers.add_new_courier()          
                    
                elif courier_options == 3:
                    # UPDATE courier
                    couriers.update_courier()
                
                elif courier_options == 4:
                    # DELETE courier
                    couriers.delete_courier()
                
                elif courier_options == 5:
                    # Import couriers table in CSV Format
                    couriers.courier_sqltable_to_csvfile()

                elif courier_options == 6:
                    # Clear the screen
                    clear()

        elif main_menu_option == 3:
            while main_menu_option == 3:

                # ORDERS MENU
                orders_options = ''
                order_options = orders.order_menu(orders_options)

                if order_options == 0:
                    # Go to the main menu options
                    options = True
                    break
                    
                elif order_options == 1:
                    orders.display_orders()
                    options = True
                
                
                elif order_options == 2:
                    # Add Order
                    orders.add_order()
                    options = True
            
                elif order_options == 3:
                    # Update existing order STATUS
                    orders.update_order_status()
                    options = True
                
                elif order_options == 4:

                    # Update existing order
                    orders.update_existing_order()
                    options = True
                
                elif order_options == 5:

                    # Dispaly orders by couriers
                    orders.order_list_by_courier()
                    options = True

                elif order_options == 6:
                    # Delete order 
                    orders.delete_order()
                    options = True
                
                elif order_options == 7:
                    # Import orders table in CSV Format
                    orders.order_sqltable_to_csvfile()
                    options = True
                
                elif order_options == 8:
                    # Clear the screen
                    clear()

        elif main_menu_option == 4:
            while main_menu_option == 4:
                
                # CUSTOMER MENU OPTIONS
                customers_options = ''
                customer_options = customers.customer_menu(customers_options)

                if customer_options == 0:
                    # Go to the main menu options
                    break

                elif customer_options == 1:
                    # Display customer table
                    customers.display_customers()

                elif customer_options == 2:
                    # Add product
                    customers.add_new_customer()
                       
                elif customer_options == 3:
                    # Update customer
                    customers.update_customer()
                
                elif customer_options == 4:
                    # DELETE product
                    customers.delete_customer()

                elif customer_options == 5:
                    # Import Customers table in CSV Format
                    customers.customer_sqltable_to_csvfile()

                elif customer_options == 6:
                    # Export Customers CSV file to MySQL table
                    customers.customer_from_csvfile_to_sqltable()
                
                elif customer_options == 7:
                    # Clear the screen
                    clear()


        elif main_menu_option == 5:
            miniproject = connection.cursor()
            miniproject.execute("SHOW TABLES")
            tables = miniproject.fetchall()
            for table_name in tables:
                table = table_name[0]
                print(table)
            miniproject.close()

        elif main_menu_option == 6:
            # Clear the screen
            clear()
            continue
    except ValueError:
        value_error = "\n*********** YOU ENTERED WRONG VALUE TYPE - PLEASE ENTER A NUMBER FOR OPTIONS *************"
        print(f"{value_error:1}")
    
    



