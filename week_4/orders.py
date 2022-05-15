
import pandas as pd
import json
from couriers import load_couriers_list, display_couriers
from products import load_products_list, display_products

# Load the PRODUCT list
products_list = load_products_list("products.csv")

# Load the COURIERS list
couriers_list = load_couriers_list("couriers.csv")

#couriers_list = load_couriers_list("couriers.txt")

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

def order_status():
    return ["preparing" , "shipped" , "delivered"]


def load_orders_list(filename):
    with open(filename, 'r') as file:
        orders =  json.load(file)
    # order_list = orders["orders"]
    return orders

def display_orders(orders):
    # orders = orders["orders"]
    for key, order in enumerate(orders["orders"]): 
        print(key, order)
    return orders

def save_orders(orders):
    # Save to orders.json file
    with open("orders.json", 'w') as file:
        json.dump(orders, file, indent = 4)
    return orders

def append_order(order_details):
    # Prompt user to enter Customer Name, Address, Phone Number
   
    display_orders(order_details)
    print("\n-------------------------Please enter Order details------------------------------ ")
    name = input("\nEnter Customer Name: ")
    address = input("\nEnter Customer Address: ")
    phone_number = input("\nEnter Customer Number: ")  
   
    # Print products list with its index value
    # Prompt user to enter products index values separated by commas to select products
    # Print couriers list with its index value
    # Prompt user to enter courier index value to select courier
    # Set Order Status to be preparing
    display_products(products_list)
    items = list(map(int, input("Please enter comma-separated list of product index values: ").split(",")))
    display_couriers(couriers_list)
    idx = int(input("\nPlease enter the index value associated with the courier name: ")) 
    orders_status = order_status()[2]

    # Append new order details to order list dictionary
    order_details["orders"].append({"customer_name" : name, 
                                    "customer_address" : address, 
                                    "customer_phone" : phone_number,
                                    "courier" : idx, 
                                    "status" : orders_status,
                                    "items": items})
    
    display_orders(order_details)
    return order_details

def update_order_status(order_state):
    print("\n-------------------------- Order List with index values ------------------------------- ")
    # Print order list with its index value
    # Prompt user to enter order index value 
    display_orders(order_state)
    order_index = int(input("\nPlease enter order list index value: "))

    print("\n------------------------- Order Status List with index values ------------------------- ")
    # Print order status list with its index value
    # Prompt user to enter order status index value
    for status_index, status in enumerate(order_status()):
        print(status_index , status)
    status_index = int(input("\nPlease enter order status list index value: "))

    order_state["orders"][order_index]["status"] = order_status()[status_index]
    return order_state

def update_existing_order(order_update):

    print("\n-------------------------- Order List with index values ------------------------------- ")
    # Print order list with its index value
    # Prompt user to enter order index value to update existing order
    display_orders(order_update)
    order_index = int(input("\nPlease enter order list index value: "))
    
    order = order_update["orders"][order_index]
    # Update existing order 
    for key, value in order.items():
        updated = input(f"\nDo you want to update [ {key} ] [ {value} ] Y, N: ").upper()
        if updated == "Y":
            user_input = input(f"\nPlease enter the new [ {key} ]: ")
            order_update["orders"][order_index][key] = user_input
        else:
            continue
    return order_update

def delete_order(orders):

    print("\n-------------------------- Order List with index values ------------------------------- ")
    # Print order list with its index value
    # Prompt user to enter order index value
    display_orders(orders)
    order_index = int(input("\nPlease enter order list index value: "))
    orders["orders"].pop(order_index) # delete order at index in order list

