
# MINI PROJECT WEEK 2

# Load the PRODUCT list
products = []
with open("week_2/products.txt", "r") as product:
    for product_name in product.readlines():
        products.append(product_name.strip())
    print(products)

# Load the COURIERS list
couriers = []
with open("week_2/couriers.txt", "r") as courier:
    for courier_name in courier.readlines():
        couriers.append(courier_name.strip())
    print(couriers)

order_list = [{
                "customer_name" : "Mike",
                "customer_address" : "16 London Road, London, E10 2HR",
                "customer_phone" : "078957253617",
                "courier" : "John",
                "status" : "preparing"},
                {
                "customer_name" : "David",
                "customer_address" : "345 Old Street, London, SE5 8AT",
                "customer_phone" : "078957253617",
                "courier" : "Claire",
                "status" : "preparing"},
                {
                "customer_name" : "Arben",
                "customer_address" : "28 Old Kent Road, London, SE1 5TY",
                "customer_phone" : "078957253617",
                "courier" : "Micheal",
                "status" : "preparing"}
]

order_status_list = ["preparing" , "shipped" , "delivered"]

options = True
while options:
    # main manu options
    main_menu = """\n--------------------------MAIN MENU OPTIONS--------------------------------\n
                Choose option 0/1/2/3
                -------------------
                0. To EXIT app
                1. For Products Menu
                2. For Couriers Menu 
                3. For Orders Menu
                -------------------"""
    print(main_menu)
    # Prompt user to choose on of the above options
    main_menu_option = int(input("Please enter one of the above options: "))

    if main_menu_option == 0:
        # Save product list to product.txt
        with open("week_2/products.txt", "w") as save_products:
            for product in products:
                save_products.write(product + "\n")
        
        # Save couriers list to couriers.txt
        with open("week_2/couriers.txt", "w") as save_couriers:
            for courier in couriers:
                save_couriers.write(courier + "\n")
       
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
            # Update existing product name at index in product list

            # Print product names with its index value
            for idx, product_name in enumerate(products):
                print(idx, product_name)  
            # Prompt user to input product index value
            # Prompt user to input new product name  
            # Update existing product name at index in products list                 
            idx = int(input("\nPlease enter the number associated with the product name: "))
            new_product = input("\nPlease enter a new product: ") 
            products[idx] = new_product  
       
        elif product_options == 4:
            # Delete product at index in product list

            # Print product names with its index value
            # Prompt user to input product index value  
            # Remove product at index in products list
            for idx, product_name in enumerate(products):
                print(idx, product_name)                   
            idx = int(input("\nPlease enter the number associated with the product name:: "))
            products.pop(idx) 
            
    elif main_menu_option == 2:
        # COURIERS MENU
        courier_menu = """\n--------------------------COURIER MENU OPTIONS--------------------------------\n
                Choose option 0/1/2/3/4
                -------------------
                0. RETURN TO MAIN MENU
                1. For Couriers List
                2. Create new courier
                3. Update existing courier
                4. Delete existing courier
                -------------------"""
        print(courier_menu)
        
        courier_options = int(input("Please enter one of the above Courier Menu Options: "))

        if courier_options == 0:
            # Go to the main menu options
            continue

        elif courier_options == 1:
            # This will print the couriers list
            print("\n----------------------------List of Couriers------------------------")
            for courier in couriers:
                print(courier)
        
        elif courier_options == 2:
            # This will create a new courier 

            # Prompt user to enter new courier name
            # Add new courier to courier list
            new_courier = input("\nPlease enter a new courier: ")
            couriers.append(new_courier.strip()) 

            # Add new courier to the couriers file
            with open("week_2/couriers.txt", "a") as add_new_courier:
                for courier in couriers:
                    add_new_courier.write(courier)
        
        elif courier_options == 3:
            # Update existing courier name at index in couriers list

            # Print couriers names with its index value
            for idx, courier_name in enumerate(couriers):
                print(idx, courier_name)  

            # Prompt user to input courier index value
            # Prompt user to input new courier name  
            # Update existing courier name at index in couriers list                     
            idx = int(input("\nPlease enter the index value associated with the courier name: "))
            new_courier = input("\nPlease enter a new courier: ")
            couriers[idx] = new_courier
       
        elif courier_options == 4:
            # Delete courier at index in courier list

            # Print courier names with its index value
            # Prompt user to input courier index value  
            # Remove courier at index in courier list
            for idx,courier_name in enumerate(couriers):
                print(idx, courier_name)                      
            idx = int(input("\nPlease enter the index value associated with the courier name:: "))
            couriers.pop(idx)

    elif main_menu_option == 3:
        # ORDERS MENU
        order_menu = """\n--------------------------ORDER MENU OPTIONS--------------------------------\n
                Choose option 0/1/2/3/4
                -------------------
                0. RETURN TO MAIN MENU
                1. For Order List
                2. Create new courier
                3. Update existing courier
                4. Delete existing courier
                -------------------"""
        print(order_menu)
        
        order_options = int(input("Please enter one of the above Order Menu Options: "))

        if order_options == 0:
            # Go to the main menu options
            continue

        elif order_options == 1:
            # This will print the ORDERS Dictionary
            print("\n-------------------------------------------------ORDERS----------------------------------------------------")
            for order in order_list:
                print(order)




