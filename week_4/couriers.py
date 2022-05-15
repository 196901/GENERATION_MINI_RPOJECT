from re import U
import pandas as pd


from pyparsing import And
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

def load_couriers_list(filename): 
   return  pd.read_csv(filename)

def save_to_couriers_list(save_couriers):

    headers = ['Courier Name', 'Phone Number']
    write_data = pd.DataFrame(save_couriers)
    write_data.to_csv("couriers.csv", index = False, header = headers)
    return save_couriers

def display_couriers(couriers):
    message = "\n-------------------List of Couriers---------------------\n"
    print(message, couriers)
    return couriers


def add_new_courier(courier):
    # Prompt user to add new courier name and phone number
    # Append new courier to courier list
    display_couriers(courier)
    print("\n--------------- ADD NEW COURIER DETAILS ----------------")
    courier_name = str(input("\nEnter new Courier Name: "))
    phone_number = str(input(f"Please enter the phone number for [ {courier_name} ] : "))

    # Create new dictionary
    # Concatenate new courier to the couriers.csv file
    new_courier = pd.DataFrame({'Courier Name':[courier_name], 
                                'Phone Number':[phone_number]})
    courier = pd.concat([courier, new_courier], ignore_index = True, axis = 0)
    return courier

def enter_index_prompt():
    return int(input("\nPlease enter row number associated with the Courier Name you want to make changes (Update or Delete): "))

def update_courier(update_courier):
    
    display_couriers(update_courier)
    print("\n----------------- UPDATE COURIER DETAILS ----------------")
    """Assign axis for courier name and price columns
       Prompt user to input courier index value associated with the courier to be updated
       Prompt user to input new courier name and price
       Assign current courier name column associated to index value (row number)
       Assign current phone number column associated to index value (row number)"""

    courier_name_column, phone_number_column = 0, 1 # axis for courier name and price columns
    indx = enter_index_prompt()
    current_courier_name = update_courier.iloc[indx, courier_name_column] 
    current_phone_number = update_courier.iloc[indx, phone_number_column]

    """Prompt to enter 'Y' or 'N' if user wants to update both courier name and phone number or either of them
       Execute one of the if statement to update both courier name and phone number, or either of them
       Update existing both courier name and phone number or either at index value (row number) given"""

    update_courier_name = input(f"\nDo you want to update the name for [ {current_courier_name} ]  Y, N: ").upper()
    update_phone_number = input(f"Do you want to update the current phone number [ {current_phone_number} ] for [ {current_courier_name} ]  Y, N: ").upper()
    if update_courier_name == 'Y' and update_phone_number == 'Y':
        new_courier_name = input(f"\nPlease enter new name to replace [ {current_courier_name} ] : ") 
        new_phone_number = float(input(f"Please enter phone number for [ {new_courier_name} ]: "))
        update_courier.iloc[indx, :] = [new_courier_name, new_phone_number]
    elif update_courier_name == 'Y':
        new_courier_name = input(f"\nPlease enter new name to replace [ {current_courier_name} ]: ")
        update_courier.iloc[indx, courier_name_column] = new_courier_name
    elif update_phone_number == 'Y':
        new_phone_number = float(input(f"\nPlease enter new phone number for [ {current_courier_name} ]: "))
        update_courier.iloc[indx, phone_number_column] = new_phone_number
    
    display_couriers(update_courier)
    return update_courier

def delete_courier(delete_courier):
    """Print courier list to screen
       Prompt user to input courier index value associated with the courier to be deleted
       Remove the courier from the list of couriers"""

    display_couriers(delete_courier)
    print("\n------------------- DELETE COURIER  -------------------")
    indx = enter_index_prompt()
    delete_courier.drop(indx, axis=0, inplace=True)
    display_couriers(delete_courier)
    return delete_courier