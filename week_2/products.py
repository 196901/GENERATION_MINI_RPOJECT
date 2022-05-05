def load_products_list(filename):

    products_list = []
    with open(filename, 'r+') as products_file:
        for product in products_file.readlines():
            products_list.append(product.strip())
    return products_list
products_file = load_products_list("week_2/prod_test.txt")
print(products_file)

def test_product(products):
    
    for indx, product_name in enumerate(products):
        print(indx, product_name)
    idx = int(input("\nPlease enter the number associated with the product name: "))
    new_product = input("\nPlease enter a new product: ") 
    products[idx] = new_product  
    with open("week_2/prod_test.txt", "r+") as f:
        for product in products:
            f.write(product + "\n")
    return products
# test = test_product(products_file)
# print(test)

options = True
while options:
    # main manu options
    main_menu = """\n--------------------------MAIN MENU OPTIONS--------------------------------\n
                Choose option 0/1/2
                -------------------
                0. To EXIT app
                1. For Products Menu
                2. For Couriers Menu 
                -------------------"""
    print(main_menu)
    # Prompt user to choose on of the above options
    main_menu_option = int(input("Please enter one of the above options: "))

    if main_menu_option == 0:
        # # Save product list to product.txt
        # with open("week_2/prod_test.txt", "w") as save_products:
        #     for product in products:
        #         save_products.write(product + "\n")
        
        # # Save couriers list to couriers.txt
        # with open("week_2/couriers.txt", "w") as save_couriers:
        #     for courier in couriers:
        #         save_couriers.write(courier + "\n")
       
         # EXIT LOOP after done with saving to products.txt and couriers.txt 
        print("\n----------------------------- EXITING APP ------------------------------\n")
        options = False

    elif main_menu_option == 1:
        # Products Menu
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
        
        product_options = int(input("Please enter one of the above Product Menu Options: "))

        if product_options == 0:
            # Go to the main menu options
            continue

        elif product_options == 1:
            # This will print the product list
            print("\n----------------------------List of Products------------------------------")
            for product in products:
                print(product)
        
        elif product_options == 2:
            # This will create a new product

            # Prompt user to enter new product
            new_product = input("\nPlease enter a new product: ")
            products.append(new_product.strip()) # Add new product to products list

            # Add new product to the products file
            with open("week_2/products.txt", "a") as add_new_product:
               for product in products:
                    add_new_product.write(product)
             
        elif product_options == 3:
            test = test_product(products_file)
            print(test)
            # # Update existing product name at index in product list

            # # Print product names with its index value
            # for idx, product_name in enumerate(products):
            #     print(idx, product_name)  
            # # Prompt user to input product index value
            # # Prompt user to input new product name  
            # # Update existing product name at index in products list                 
            # idx = int(input("\nPlease enter the number associated with the product name: "))
            # new_product = input("\nPlease enter a new product: ") 
            # products[idx] = new_product  
       