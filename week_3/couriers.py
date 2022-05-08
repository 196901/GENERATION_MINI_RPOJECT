from os.path import exists
def courier_menu(courier__menu_options : str):
    courier_menu = """\n--------------------------COURIERS MENU OPTIONS-----------------------------\n
                Choose option 0/1/2/3/4
                -------------------
                0. RETURN TO MAIN MENU
                1. For Couriers List
                2. Create new courier
                3. Update existing courier
                4. Delete existing courier
                -------------------"""
    print(courier_menu) 
  
    courier__menu_options = int(input("Please enter one of the above courier Menu Options: "))
    return courier__menu_options

def load_couriers_list(filename):
    couriers = []
    # Open file and load couriers list from couriers.txt
    with open(filename, "r") as courier:
        for courier_name in courier.readlines():
            couriers.append(courier_name.strip())
    return couriers

def save_to_couriers_list(save_couriers : list):
    
    file_exists = exists("week_3/couriers.txt")

    # Save courier list to couriers.txt
    # Check if file exists
    if file_exists:
        with open("week_3/couriers.txt", "r+") as file:
                for courier in save_couriers:
                    file.write(courier + "\n")    
    else:
        with open("week_3/couriers.txt", "w") as file:
            for courier in save_couriers:
                file.write(courier + "\n")
    return save_couriers

def add_new_courier(new_courier : list):
    
    # Prompt user to add new courier
    # Append new courier to courier list
    add_new_courier = input("\nPlease enter a new courier to add: ")
    new_courier.append(add_new_courier)

    # Save new courier to couriers.txt
    save_to_couriers_list(new_courier)
    return new_courier

def couriers_with_indexes(courier_indexes : list):

    # Loop through courier_list and print courier name with corresponding courier index value
    print("\n----------------Below are courier name with corresponding indexes-----------------")
    for index, courier_name in enumerate(courier_indexes):
        print(index,courier_name)
    return courier_indexes


def update_courier(courier : list):
    # Print courier names with its index value
    couriers_with_indexes(courier)

    """Prompt user to input courier index value
       Prompt user to input new courier name  
       Update existing courier name at index in couriers list"""

    indx = int(input("\nPlease enter the number associated with the courier name: "))
    new_courier = input("\nPlease enter a new courier name: ") 
    courier[indx] = new_courier  
    save_to_couriers_list(courier)
    return courier
