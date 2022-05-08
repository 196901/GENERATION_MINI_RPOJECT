
from couriers import load_couriers_list, couriers_with_indexes

couriers_list = load_couriers_list("week_3/couriers.txt")

def order_menu(order_menu_options : str):
    order_menu = order_menu = """\n--------------------------ORDER MENU OPTIONS--------------------------------\n
                Choose option 0/1/2/3/4
                -------------------
                0. RETURN TO MAIN MENU
                1. For Order List
                2. Enter order details and append to order list
                3. Update existing order status
                4. Update existing order
                5. Delete existing order
                -------------------"""
    print(order_menu)
        
    order_menu_options = int(input("Please enter one of the above Order Menu Options: "))
    return order_menu_options

def orders_list():
    orders = [{
                    "customer_name" : "Mike",
                    "customer_address" : "16 London Road, London, E10 2HR",
                    "customer_phone" : "078957253617",
                    "courier" : 0,
                    "status" : "preparing"},
                    {
                    "customer_name" : "David",
                    "customer_address" : "345 Old Street, London, SE5 8AT",
                    "customer_phone" : "078957253617",
                    "courier" : 1,
                    "status" : "preparing"},
                    {
                    "customer_name" : "Arben",
                    "customer_address" : "28 Old Kent Road, London, SE1 5TY",
                    "customer_phone" : "078957253617",
                    "courier" : 2,
                    "status" : "preparing"}
]
    return orders


# for order in orders_list():
#     print(order)

def order_status():
    return ["preparing" , "shipped" , "delivered"]

def append_order(order_details : list):
    # Prompt user to enter Customer Name, Address, Phone Number
    print("\n-------------------------Please enter Order details------------------------------ ")
    name = input("\nEnter Customer Name: ")
    address = input("\nEnter Customer Address: ")
    phone_number = input("\nEnter Customer Number: ")  

    # Print couriers names with its index value
    # Prompt user to enter courier index value to select courier
    # Set Order Status to be preparing
    couriers_with_indexes(couriers_list) 
    idx = int(input("\nPlease enter the index value associated with the courier name: ")) 
    orders_status = order_status()[2]

    # Append new order details to order list dictionary
    order_details.append({"customer_name" : name, 
                          "customer_address" : address, 
                          "customer_phone" : phone_number,
                          "courier" : idx, 
                          "status" : orders_status})
    return order_details

def update_order_status(order_state : list):
    print("\n-------------------------- Order List with index values ------------------------------- ")
    # Print order list with its index value
    # Prompt user to enter order index value 
    for order_index, order in enumerate(orders_list()):
        print(order_index, order)
    order_index = int(input("\nPlease enter order list index value: "))

    print("\n------------------------- Order Status List with index values ------------------------- ")
    # Print order status list with its index value
    # Prompt user to enter order status index value
    for status_index, status in enumerate(order_status()):
        print(status_index , status)
    status_index = int(input("\nPlease enter order status list index value: "))

    order_state[order_index]["status"] = order_status()[status_index]
    return order_state

def update_existing_order(order_update : list):

    print("\n-------------------------- Order List with index values ------------------------------- ")
    # Print order list with its index value
    # Prompt user to enter order index value to update existing order
    for order_index, order in enumerate(orders_list()):
        print(order_index, order)
    order_index = int(input("\nPlease enter order list index value: "))

    # Update existing order 
    for key, value in orders_list()[order_index].items():
        updated = input(f"\nDo you want to update {key.capitalize()} {value} Y, N: ").upper()
        if updated == "Y":
            user_input = input(f"\nPlease enter the new {key.capitalize()}: ")
            order_update[order_index][key] = user_input
        else:
            continue
    return order_update

def delete_order(orders : list):

    print("\n-------------------------- Order List with index values ------------------------------- ")
    # Print order list with its index value
    # Prompt user to enter order index value
    for order_index, order in enumerate(orders_list()):
        print(order_index, order)
    order_index = int(input("\nPlease enter order list index value: "))
    orders.pop(order_index) # delete order at index in order list