# MINI PROJECT WEEK 3

from products import product_menu, load_products_list, save_to_products_list,\
add_new_product, update_product
from couriers import courier_menu, load_couriers_list, save_to_couriers_list,\
add_new_courier, update_courier
from orders import order_menu, orders_list, append_order, update_order_status,\
update_existing_order, delete_order  

# Load the PRODUCT list
products_list = load_products_list("week_3/products.txt")
print(products_list)

# Load the COURIERS list
couriers_list = load_couriers_list("week_3/couriers.txt")
print(couriers_list)

order_list = [] 
order_list = orders_list()


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
        save_to_products_list(products_list)
        
        # Save couriers list to couriers.txt
        save_to_couriers_list(couriers_list)
       
         # EXIT LOOP after done with saving to products.txt and couriers.txt 
        print("\n----------------------------- EXITING APP ------------------------------\n")
        options = False

    elif main_menu_option == 1:
        # PRODUCT MENU OPTIONS
        products_options = ''
        product_options = product_menu(products_options)
        

        if product_options == 0:
            # Go to the main menu options
            continue

        elif product_options == 1:
            # This will print the product list
            print("\n----------------------------List of Products------------------------------\n")
            print(products_list)
        
        elif product_options == 2:
            # This will create a new product
            add_new_product(products_list)
             
        elif product_options == 3:
            # UPDATE existing product name at index in product list
            update_product(products_list)
           
        elif product_options == 4:

            #products_with_indexes(products_list)
            for indx, product_name in enumerate(products_list):
                print(indx , product_name)

            # Prompt user to input product index value 
            # Remove product at index in products list"""          
            indx = int(input("\nPlease enter the number associated with the product name:: "))
            products_list.pop(indx) 
            print(products_list)
            
    elif main_menu_option == 2:
        # COURIERS MENU
        couriers_options = ''
        courier_options = courier_menu(couriers_options)
        
        if courier_options == 0:
            # Go to the main menu options
            continue

        elif courier_options == 1:
            # This will print the courier list
            print("\n----------------------------List of couriers------------------------------\n")
            print(couriers_list)
        
        elif courier_options == 2:
            # This will create a new courier
            add_new_courier(couriers_list)
             
        elif courier_options == 3:
            # UPDATE existing courier name at index in courier list
            update_courier(couriers_list)
           
        elif courier_options == 4:

            #couriers_with_indexes(couriers_list)
            for indx, courier_name in enumerate(couriers_list):
                print(indx , courier_name)
            # Prompt user to input courier index value 
            # Remove courier at index in couriers list"""          
            indx = int(input("\nPlease enter the number associated with the courier name:: "))
            couriers_list.pop(indx) 
            print(couriers_list)

    elif main_menu_option == 3:
        # ORDERS MENU
        options = ''
        order_options = order_menu(options)

        if order_options == 0:
            # Go to the main menu options
            continue

        elif order_options == 1:
            print("\n-------------------------------------------------ORDERS----------------------------------------------------")
            # This will print the ORDERS Dictionary
            for order in order_list:
                print(order)
            options = True
           
        
        elif order_options == 2:
            # Append order to order list
            append_order(order_list)
            options = True
        

        elif order_options == 3:
            # Update existing order status
            update_order_status(order_list)
            print(order_list)
            options = True
        
        elif order_options == 4:

            # Update existing order
            update_existing_order(order_list)
            options = True


        elif order_options == 5:
            # Delete order 
            delete_order(order_list)
            options = True

