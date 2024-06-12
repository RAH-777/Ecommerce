products = ['fanta', 'coke', 'sprite', 'lemonade', 'pepsi']
orders = [{
            'customer_name':'Raheem', 
            'customer_address':'sse4re', 
            'customer_phone_number':'0987654321',
            'order':'coke',
            "order_status": "preparing",
}]
while True:
    print('MAIN MENU OPTION:\n0.Exit\n1.PRODUCTS MENU\n2.ORDERS MENU')
    main_menu_option = int(input('choose an option from 0-2: '))
    if main_menu_option == 0:
        exit()
    elif main_menu_option == 1:
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
            new_product_input = input ('Enter new product ')
            products.append(new_product_input)
            print('is there anything else we can help you with?')
        #update product
        elif user_input == 3:
            for index,item in enumerate(products):
                print(index,item)
        #get index value from user and store in variable      
            user_input_index = int (input ('Enter product index value'))
        #get product name from user and store in variable   
            user_input_product_name = input ('Enter new product name')
        #from products get item with requested index and assign requested new name 
            products[user_input_index] =  user_input_product_name
            print('is there anything else we can help you with?')


        #delete product
        elif user_input == 4:
            for index,item in enumerate(products):
                print(index,item)
                # GET user input for product index value
            user_input_index = int (input ('Enter product index value'))
            #  DELETE product at index in products list
            del products[user_input_index] 
        # GET user input for product index value
            print('is there anything else we can help you with?')


# orders menu

    elif main_menu_option == 2:
        print('ORDER MENU OPTIONS:\n0. RETURN TO MAIN \n1. LIST ORDERS \n2. NEW ORDER\n3. UPDATE ORDER STATUS\n4. UPDTAE ORDER\n5. DELETE ORDER')
        order_menu_option = int(input('choose an option from 0-5: '))
        #option 0: main menu
        if order_menu_option == 0:
            print('return to main menu')
        # option 1: order menu option2

        elif order_menu_option == 1:
            print(orders)
            print('is there anything else we can help you with?')
        # option 2:
        elif order_menu_option == 2:
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

 # UPDATE existing order status

        elif order_menu_option == 3:
        #     PRINT orders list with its index values
            for index,item in enumerate (orders):
                print(index,item['customer_name'])

        # GET user input for order index value
            user_input_index = int (input('ENTER order index value to update status'))
        
        
        # PRINT order status list with index values
            for index,item in enumerate(orders):
                print(index,item['order_status'] )

        # GET user input for order status index value
            status_update = input('What do you want to UPDATE status to')
            # UPDATE status for order
            orders[user_input_index]['order_status'] = status_update
            print('is there anything else we can help you with?')

         # ELSE IF user input is 4:
        elif order_menu_option == 4:
            # STRETCH - UPDATE existing order
            #     PRINT orders list with its index values
            for index,item in enumerate (orders):
                print(index,item['customer_name'])
        #GET user input for order index value
            user_input_index = int ( input("ENTER order index value to update existing order"))
            if user_input_index < 0 or user_input_index >= len(orders):
                print("Invalid order index")

            order_to_update = orders[user_input_index]

            for key, value in order_to_update.items():
                new_value = input(f"Enter new value for {key} (press Enter to keep '{value}'): ")
            if new_value.strip() != "":
                order_to_update[key] = new_value

            print("Order updated successfully!")
            print(orders)

    #     FOR EACH key-value pair in selected order:
    #         GET user input for updated property
    #         IF user input is blank:
    #             do not update this property
    #         ELSE:
    #             update the property value with user input



       
        