# MINI PROJETC WEEK 1

# List of products 
products = ["Capuccino", "Late", "Mocha", "Espresso","Hot Chocolate"]
options = True
while options:
    # main manu options
    main_menu = """\n--------------------------MAIN MENU OPTIONS--------------------------------\n
                Choose option 0/1/2
                -------------------
                0. To EXIT app
                1. For Products Menu
                -------------------"""
    print(main_menu)
    
    # Prompt user to choose option
    main_menu_option = int(input("Please enter one of the above options: "))

    if main_menu_option == 0:

        # This will exit loop
        print("\n----------------------------- EXITING APP ------------------------\n")
        options = False

    elif main_menu_option == 1:
        # Continue to the Products Options
        print("\n--------------------------PRODUCT OPTIONS----------------------------")
        print("Enter 0 to go to Main Menu options: ")
        print("Enter 1 to print Product List: ")
        print("Enter 2 to add a new product: ")
        print("Enter 3 to update existing Product: ")
        print("Enter 4 to delete from existing Product: ")
        product_options = int(input("Please enter one of the above options from 1-4: "))

        if product_options == 0:
            # Go to the main menu options
            continue

        elif product_options == 1:
            # This will print the product list
            print("\n----------------------------List of Products------------------------")
            for product in products:
                print(product)
        
        elif product_options == 2:
            # This will create a new product
            new_product = input("\nPlease enter a new product: ")
            products.append(new_product)
            print(products)
        
        elif product_options == 3:
            # Update existing product name at index in product list

            print("\nBelow is the product list (number, product name")
            for idx, product_name in enumerate(products):
                print(idx, product_name)                      
            idx = int(input("\nPlease enter the number associated with the product name: "))
            new_product = input("\nPlease enter a new product: ")
            products[idx] = new_product
            print(products)
       
        elif product_options == 4:
            # Delete product at index in product 

            for idx, product_name in enumerate(products):
                print(idx, product_name)                      
            idx = int(input("\nPlease enter the number associated with the product name:: "))
            products.pop(idx)
            print(products)

                









    



