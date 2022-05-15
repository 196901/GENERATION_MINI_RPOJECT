from re import U
import pandas as pd


from pyparsing import And
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

def load_products_list(filename): 
    product = pd.read_csv(filename)
    return product 

def save_to_products_list(save_products):

    headers = ['Product Name', 'Price']
    write_data = pd.DataFrame(save_products)
    write_data.to_csv("products.csv", index = False, header = headers)
    return save_products

def display_products(products):
    message = "\n-------------------List of Products---------------------\n"
    print(message, products)
    return products


def add_new_product(product):
    # Prompt user to add new product name and price
    # Append new product to product list
    display_products(product)
    print("\n--------------- ADD NEW PRODUCT DETAILS ----------------")
    product_name = str(input("\nEnter new Product Name: "))
    product_price = float(input(f"\nPlease set the price for [ {product_name} ] : "))

    # Create new dictionary
    # Concatenate new product to the products.csv file
    new_product = pd.DataFrame({'Product Name':[product_name], 
                                'Price':[product_price]})
    product = pd.concat([product, new_product], ignore_index = True, axis = 0)
    return product

def enter_index_prompt():
    
    return int(input("\nPlease enter row number associated with the product name you want to make changes (Update or Delete): "))

def update_product(update_product):
    
    display_products(update_product)
    print("\n----------------- UPDATE PRODUCT DETAILS ----------------")
    """Assign axis for product name and price columns
       Prompt user to input product index value associated with the product to be updated
       Prompt user to input new product name and price
       Assign current product name column associated to index value (row number)
       Assign current product price column associated to index value (row number)"""

    prod_name_column, prod_price_column = 0, 1 # axis for product name and price columns
    indx = enter_index_prompt()
    current_product_name = update_product.iloc[indx, prod_name_column] 
    current_product_price = update_product.iloc[indx, prod_price_column]

    """Prompt to enter 'Y' or 'N' if user wants to update both product name and price or either of them
       Execute one of the if statement to update both product name and price, or either of them
       Update existing both product name and price or either at index value (row number) given"""

    update_product_name = input(f"\nDo you want to update the name for [ {current_product_name} ]  Y, N: ").upper()
    update_product_price = input(f"Do you want to update the current price of [{current_product_price}] for [{current_product_name}]  Y, N: ").upper()
    if update_product_name == 'Y' and update_product_price == 'Y':
        new_product = input(f"\nPlease enter new name to replace [ {current_product_name} ]: ") 
        new_price = float(input(f"Please set price for [ {new_product} ]: "))
        update_product.iloc[indx, :] = [new_product, new_price]
    elif update_product_name == 'Y':
        new_product = input(f"\nPlease enter new name to replace [ {current_product_name} ]: ")
        update_product.iloc[indx, prod_name_column] = new_product
    elif update_product_price == 'Y':
        new_price = float(input(f"\nPlease enter new price for [ {current_product_name} ]: "))
        update_product.iloc[indx, prod_price_column] = new_price
    
    display_products(update_product)
    return update_product

def delete_product(delete_product):
    """Print product list to screen
       Prompt user to input product index value associated with the product to make changes (update or delete)
       Remove the product from the list of products"""

    display_products(delete_product)
    print("\n------------------- DELETE PRODUCT  -------------------")
    indx = enter_index_prompt()
    delete_product.drop(indx, axis=0, inplace=True)
    display_products(delete_product)
    return delete_product



  
    
    

