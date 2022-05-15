# MINI PROJECT WEEK 4

from pandas import DataFrame
from products import product_menu, load_products_list, save_to_products_list,\
add_new_product, update_product, display_products, delete_product
from couriers import courier_menu, delete_courier, display_couriers, load_couriers_list, save_to_couriers_list,\
add_new_courier, update_courier
from orders import order_menu, load_orders_list, display_orders, save_orders, append_order, update_order_status,\
update_existing_order, delete_order  

# Load the PRODUCT list
products_list = load_products_list("products.csv")

# Load the COURIERS list
couriers_list = load_couriers_list("couriers.csv")

orders_list = load_orders_list("orders.json")
print(type(orders_list))


# order_list = [] 
# order_list = orders_list()

options = True
while options:
    # main manu options
    main_menu = """
    \n----------------MAIN MENU OPTIONS----------------------\n
    Choose option 0/1/2/3
    -------------------
    0. To EXIT app
    1. For Products Menu
    2. For Couriers Menu 
    3. For Orders Menu
    -------------------"""
    print(main_menu)
    # Prompt user to choose on of the above options
    main_menu_option = int(input("Please enter one of the above Main Menu Options: "))

    if main_menu_option == 0:
        # Save product list to products.csv
        save_to_products_list(products_list)
        
        # Save couriers list to couriers.csv
        save_to_couriers_list(couriers_list)

        # Save couriers list to orders.json
        save_orders(orders_list)
       
         # EXIT LOOP after done with saving to products.txt and couriers.txt 
        print("\n------------------- EXITING APP -----------------------\n")
        options = False

    elif main_menu_option == 1:
        # PRODUCT MENU OPTIONS
        products_options = ''
        product_options = product_menu(products_options)
        

        if product_options == 0:
            # Go to the main menu options
            continue

        elif product_options == 1:
            display_products(products_list)
        
        elif product_options == 2:
            # This will create a new product
            new_product_list = DataFrame
            new_product_list = add_new_product(products_list)
            products_list = new_product_list
            
             
        elif product_options == 3:
            # UPDATE existing product name at index in product list
            update_product(products_list)
             
        elif product_options == 4:
            # DELETE product
            delete_product(products_list)
            
    elif main_menu_option == 2:
        # COURIERS MENU
        couriers_options = ''
        courier_options = courier_menu(couriers_options)
        
        if courier_options == 0:
            # Go to the main menu options
            continue

        elif courier_options == 1:
            # This will print the courier list
            display_couriers(couriers_list)
        
        elif courier_options == 2:
            # This will create a new courier
            new_courier_list = DataFrame
            new_courier_list = add_new_courier(couriers_list)
            couriers_list = new_courier_list
             
        elif courier_options == 3:
            # UPDATE existing courier name at index in courier list
            update_courier(couriers_list)
           
        elif courier_options == 4:
            # DELETE courier
            delete_courier(couriers_list)

    elif main_menu_option == 3:
        # ORDERS MENU
        options = ''
        order_options = order_menu(options)

        if order_options == 0:
            # Go to the main menu options
            continue

        elif order_options == 1:
            print("\n----------------------------------ORDERS--------------------------------")
            display_orders(orders_list)
            
            # # This will print the ORDERS Dictionary
            # for order in order_list:
            #     print(order)
            options = True
           
        
        elif order_options == 2:
            # Append order to order list
            append_order(orders_list)
            options = True
        

        elif order_options == 3:
            # Update existing order status
            update_order_status(orders_list)
            options = True
        
        elif order_options == 4:

            # Update existing order
            update_existing_order(orders_list)
            options = True


        elif order_options == 5:
            # Delete order 
            delete_order(orders_list)
            options = True

