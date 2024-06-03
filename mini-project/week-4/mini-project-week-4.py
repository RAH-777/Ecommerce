products = []

def get_product_list():
#open file in read mode
    with open("products.txt","r") as file:
        product_list = file.readlines()
#store products in python list
    stripped_product_list = []
    for item in product_list:
        stripped_product_list.append(item.strip())   
#return the product list    
    return(stripped_product_list )

products = get_product_list()


def get_courier_list():
    with open("couriers.txt","r") as file:
        couriers_list = file.readlines()
    stripped_courier_list = []
    for item in couriers_list:
        stripped_courier_list.append(item.strip())
    return(stripped_courier_list)

couriers = get_courier_list()



orders = []
orders = [{
            'customer_name':'Raheem', 
            'customer_address':"Unit 2, 12 Main Street, LONDON, WH1 2ER", 
            'customer_phone_number':'0987654321',
            "courier": 2, # Courier index
            "order_status": "preparing",
}]




while True:
    print('MAIN MENU OPTION:\n0.Exit\n1.PRODUCTS MENU\n2.ORDERS MENU')
    main_menu_option = int(input('choose an option from 0-2: '))
    if main_menu_option == 0:
        exit("Program has exited")


    elif main_menu_option == 1:
        while True:
            user_input = int(input('RETURN to main menu:0\nPRINT product list:1\nCREATE new product:2\nUPDATE existing product:3\nDELETE product:4\n'))
            #return to main menu
            if user_input == 0:
                break
            
            #print product list
            elif user_input == 1:
                for item in products:
                    print(item)
                print('is there anything else we can help you with?')
            #create new product
            elif user_input == 2:
                new_product_input = input ('\nEnter new product:\n')

                with open("products.txt", "a") as file:
                    file.write(f"{new_product_input}\n".capitalize())

                products = get_product_list()
                products = [i.strip() for i in products]
                print("Updated list of products:\n")
                for product in products:
                    print(product,end = "")
                
                print("\nNew product added. Is there something else we can help you with?\n")
                break
            
            #update product
            elif user_input == 3:
                for index,item in enumerate(products):
                    print(f"{item} at index : {index}")
                #get index value from user and store in variable      
                user_input_index = int (input ('\nEnter product index value you would you like to replace:\n'))
                #get product name from user and store in variable   
                user_input_product_name = input (f"\nWhich item will replace {products[user_input_index]}?\n")
                #from products get item with requested index and assign requested new name 
                products[user_input_index] =  user_input_product_name
                with open("products.txt", "w") as file:
                    for product in products:
                        file.write(f"{product}\n".capitalize())


                print("\nUpdated products:\n")
                updated_products = get_product_list()
                for product in updated_products:
                    print(product, end = "")
                print("\nProduct updated successfully. Is there something else we can help you with?\n")
                break

            


             #delete product
            elif user_input == 4:
                for index,item in enumerate(products):
                    print(index,item)
                # GET user input for product index value
                user_input_index = int (input ('Enter product index would you like to delete:\n'))
                #DELETE product at index in products listi
                del products[user_input_index] 
                #GET user input for product index value
                with open("products.txt", "w") as file:
                    for product in products:
                        file.write(f"{product}\n".capitalize())

                print("\nUpdated products:\n")
                updated_products = get_product_list()
                for product in updated_products:
                    print(product, end = "")
                print("\nProduct deleted. Is there something else we can help you with?")
                break

    elif main_menu_option == 2:
        while True:
            print("Choose from the following options:\n")
            user_input = int(input(f"COURIER MENU OPTIONS:\n0 - RETURN to main menu\n1 - PRINT couriers list\n2 - CREATE new courier\n3 - UPDATE existing courier\n4 - DELETE courier\n"))
            #return to main menu
            if user_input == 0:
                break
            #print couriers list
            if user_input == 1:
                if len(couriers) < 1:
                    print("\nSorry, there are currently no couriers.")
                    print("\nIs there anything else we can help you with?\n")
                    break


            #create new courier
            elif user_input == 2:
                new_courier_input = input ('\nEnter new courier:\n')

                with open("couriers.txt", "a") as file:
                    file.write(f"{new_courier_input}\n".capitalize())

                couriers = get_courier_list()
                couriers = [i.strip() for i in couriers]
                print("Updated list of couriers:\n")
                for courier in couriers:
                    print(courier,end = "")
                
                print("\nNew courier added. Is there something else we can help you with?\n")
                break
            
            #update courier
            elif user_input == 3:
                for index,courier in enumerate(couriers):
                    print(f"{courier} at index : {index}")
                #get index value from user and store in variable      
                user_input_index = int (input ('\nEnter courier index value you would you like to replace:\n'))
                #get courier name from user and store in variable   
                user_input_courier_name = input (f"\nWhich courier will replace {couriers[user_input_index]}?\n")
                #from couriers get courier with requested index and assign requested new name 
                couriers[user_input_index] =  user_input_courier_name
                with open("couriers.txt", "w") as file:
                    for courier in couriers:
                        file.write(f"{courier}\n".capitalize())


                print("\nUpdated couriers:\n")
                updated_couriers = get_courier_list()
                for courier in updated_couriers:
                    print(courier, end = "")
                print("\ncourier updated successfully. Is there something else we can help you with?\n")
                break

            


             #delete courier
            elif user_input == 4:
                for index,courier in enumerate(couriers):
                    print(index,courier)
                # GET user input for courier index value
                user_input_index = int (input ('Enter courier index would you like to delete:\n'))
                #DELETE courier at index in couriers listi
                del couriers[user_input_index] 
                #GET user input for courier index value
                with open("couriers.txt", "w") as file:
                    for courier in couriers:
                        file.write(f"{courier}\n".capitalize())

                print("\nUpdated couriers:\n")
                updated_couriers = get_courier_list()
                for courier in updated_couriers:
                    print(courier, end = "")
                print("\ncourier deleted. Is there something else we can help you with?")
                break


# # orders menu
    elif main_menu_option == 3:

        while True:
            print("Choose from the following options:\n")
            print('ORDER MENU OPTIONS:\n0. RETURN TO MAIN \n1. LIST ORDERS \n2. NEW ORDER\n3. UPDATE ORDER STATUS\n4. UPDATE EXISTING ORDER\n5. DELETE ORDER')       
            order_menu_option = int(input('choose an option from 0-5: '))
            #return to main menu
            if order_menu_option == 0:
                print('return to main menu')
            

            elif order_menu_option == 1:
                if len(orders) < 1:
                    print("\nSorry, there are currently no orders.")
                    print("\nIs there anything else we can help you with?\n")
                    break

                print("current orders:\n")
                for order in orders:
                        for k,v in order.items():
                            print(f"{k} : {v}")
                        print()
                print("\nThanks for viewing the orders. Is there anything else we can help you with?\n")
                break
                
            # option 2:
            if order_menu_option == 2:




                customer_name = input('enter your name')
                customer_address = input('enter your address')
                customer_phone_number = input('enter your phone number')
                for item in products:
                    print(item)
                customer_order = input('Enter order')
                orders.append ( {
                'customer_name':customer_name, 
                'customer_address':customer_address, 
                'customer_phone_number':customer_phone_number,
                'order':customer_order,
                "order_status": "preparing",
                })
                
                print("Order added.")
                print('is there anything else we can help you with?')

#  # UPDATE existing order status

#         elif order_menu_option == 3:
#         #     PRINT orders list with its index values
#             for index,item in enumerate (orders):
#                 print(index,item['customer_name'])

#         # GET user input for order index value
#             user_input_index = int (input('ENTER order index value to update status'))
        
        
#         # PRINT order status list with index values
#             for index,item in enumerate(orders):
#                 print(index,item['order_status'] )

#         # GET user input for order status index value
#             status_update = input('What do you want to UPDATE status to')
#             # UPDATE status for order
#             orders[user_input_index]['order_status'] = status_update
#             print('is there anything else we can help you with?')

#          # ELSE IF user input is 4:
#         elif order_menu_option == 4:
#             # STRETCH - UPDATE existing order
#             #     PRINT orders list with its index values
#             for index,item in enumerate (orders):
#                 print(index,item['customer_name'])
#         #GET user input for order index value
#             user_input_index = int ( input("ENTER order index value to update existing order"))
#             if user_input_index < 0 or user_input_index >= len(orders):
#                 print("Invalid order index")
#                     return

#             order_to_update = orders[user_input_index]

#             for key, value in order_to_update.items():
#             new_value = input(f"Enter new value for {key} (press Enter to keep '{value}'): ")
#             if new_value.strip() != "":
#             order_to_update[key] = new_value

#             print("Order updated successfully!")
#             print_orders(orders)

#     #     FOR EACH key-value pair in selected order:
#     #         GET user input for updated property
#     #         IF user input is blank:
#     #             do not update this property
#     #         ELSE:
#     #             update the property value with user input