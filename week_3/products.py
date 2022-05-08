from os.path import exists
def product_menu(product__menu_options : str):
    product_menu = """\n--------------------------PRODUCT MENU OPTIONS-----------------------------\n
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
    products = []
    # Open file and load products list from products.txt
    with open(filename, "r") as product:
        for product_name in product.readlines():
            products.append(product_name.strip())
    return products

def save_to_products_list(save_products : list):
    
    file_exists = exists("week_3/products.txt")

    # Save product list to products.txt
    # Check if file exists
    if file_exists:
        with open("week_3/products.txt", "r+") as file:
                for product in save_products:
                    file.write(product + "\n")    
    else:
        with open("week_3/products.txt", "w") as file:
            for product in save_products:
                file.write(product + "\n")
    return save_products

def add_new_product(new_product : list):
    
    # Prompt user to add new product
    # Append new product to product list
    add_new_product = input("\nPlease enter a new product to add: ")
    new_product.append(add_new_product)

    # Save new product to products.txt
    save_to_products_list(new_product)
    return new_product

def products_with_indexes(product_indexes : list):

    # Loop through product_list and print product name with corresponding product index value
    print("\n----------------Below are product name with corresponding indexes-----------------")
    for index, product_name in enumerate(product_indexes):
        print(index,product_name)
    return product_indexes


def update_product(product : list):
    # Print product names with its index value
    products_with_indexes(product)

    """Prompt user to input product index value
       Prompt user to input new product name  
       Update existing product name at index in products list"""

    indx = int(input("\nPlease enter the number associated with the product name: "))
    new_product = input("\nPlease enter a new product name: ") 
    product[indx] = new_product  
    save_to_products_list(product)
    return product

  
    
    

