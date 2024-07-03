# sdSS_SSSSSSbs   .S    S.     sSSs                             
# YSSS~S%SSSSSP  .SS    SS.   d%%SP                             
#      S%S       S%S    S%S  d%S'                               
#      S%S       S%S    S%S  S%S                                
#      S&S       S%S SSSS%S  S&S                                
#      S&S       S&S  SSS&S  S&S_Ss                             
#      S&S       S&S    S&S  S&S~SP                             
#      S&S       S&S    S&S  S&S                                
#      S*S       S*S    S*S  S*b                                
#      S*S       S*S    S*S  S*S.                               
#      S*S       S*S    S*S   SSSbs                             
#      S*S       SSS    S*S    YSSP                             
#      SP               SP                                      
#      Y                Y                                       
                                                              
#   sSSs    sSSs_sSSs      sSSs    sSSs    sSSs    sSSs         
#  d%%SP   d%%SP~YS%%b    d%%SP   d%%SP   d%%SP   d%%SP         
# d%S'    d%S'     `S%b  d%S'    d%S'    d%S'    d%S'           
# S%S     S%S       S%S  S%S     S%S     S%S     S%S            
# S&S     S&S       S&S  S&S     S&S     S&S     S&S            
# S&S     S&S       S&S  S&S_Ss  S&S_Ss  S&S_Ss  S&S_Ss         
# S&S     S&S       S&S  S&S~SP  S&S~SP  S&S~SP  S&S~SP         
# S&S     S&S       S&S  S&S     S&S     S&S     S&S            
# S*b     S*b       d*S  S*b     S*b     S*b     S*b            
# S*S.    S*S.     .S*S  S*S     S*S     S*S.    S*S.           
#  SSSbs   SSSbs_sdSSS   S*S     S*S      SSSbs   SSSbs         
#   YSSP    YSSP~YSSY    S*S     S*S       YSSP    YSSP         
#                        SP      SP                             
#                        Y       Y                              
                                                              
#   sSSs   .S_SSSs     .S_sSSs    sdSS_SSSSSSbs    sSSs  S.     
#  d%%SP  .SS~SSSSS   .SS~YS%%b   YSSS~S%SSSSSP   d%%SP  SS.    
# d%S'    S%S   SSSS  S%S   `S%b       S%S       d%S'    S%S    
# S%S     S%S    S%S  S%S    S%S       S%S       S%S     S%S    
# S&S     S%S SSSS%S  S%S    d*S       S&S       S&S     S&S    
# S&S     S&S  SSS%S  S&S   .S*S       S&S       S&S_Ss  S&S    
# S&S     S&S    S&S  S&S_sdSSS        S&S       S&S~SP  S&S    
# S&S     S&S    S&S  S&S~YSY%b        S&S       S&S     S&S    
# S*b     S*S    S&S  S*S   `S%b       S*S       S*b     S*b    
# S*S.    S*S    S*S  S*S    S%S       S*S       S*S.    S*S.   
#  SSSbs  S*S    S*S  S*S    S&S       S*S        SSSbs   SSSbs 
#   YSSP  SSS    S*S  S*S    SSS       S*S         YSSP    YSSP 
#                SP   SP               SP                       
#                Y    Y                Y                      


import csv
import os 

orders = [{}]
products = [{}]
courier = [{}]

def load_csv(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
    
        return list(reader)

def save_csv(filename, data, fieldnames):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def get_products():
   
    with open("products.csv","r",newline="") as file:
        reader = csv.DictReader(file)
        product_list = [row for row in reader]
    return(product_list)

def get_couriers():
    with open("couriers.csv","r",newline="") as file:
        reader = csv.DictReader(file)
        courier_list = [row for row in reader]
    return(courier_list)

# Function to load orders from a CSV file
def get_orders():
    with open("orders.csv","r",newline="") as file:
        reader = csv.DictReader(file)
        order_list = [row for row in reader]
    return(order_list)




def update_couriers(couriers):
    with open("couriers.csv", "w",newline='') as file:
        field_names = ["name","phone","index"]
        writer = csv.DictWriter(file,fieldnames=field_names)
        writer.writeheader()
        index = 0
        for courier in couriers:
            #rewrite index's
            courier['index'] = index
            index += 1
            writer.writerow(courier)

def update_products(products):
    with open("products.csv", "w",newline='') as file:
        field_names = ["name","price","index"]
        writer = csv.DictWriter(file,fieldnames=field_names)
        writer.writeheader()
        index = 0
        for product in products:
            #rewrite index's
            product['index'] = index
            index += 1
            writer.writerow(product)
# Function to save orders to a CSV file
def update_orders(orders):
    with open("orders.csv", "w",newline='') as file:
        field_names = ["customer name", "customer address", "customer phone number", "courier", "status", "items"]
        writer = csv.DictWriter(file,fieldnames=field_names)
        writer.writeheader()
        index = 0
        for order in orders:
            #rewrite index's
            product['index'] = index
            index += 1
            writer.writerow(order)





PRODUCT_FILE = 'C:\\Users\\lordr\\Documents\\Python\\Raheem-miniproject\\mini-project\\week-4\\products.csv'
COURIERS_FILE = 'C:\\Users\\lordr\\Documents\\Python\\Raheem-miniproject\\mini-project\\week-4\\couriers.csv'
ORDER_FILE = 'C:\\Users\\lordr\\Documents\\Python\\Raheem-miniproject\\mini-project\\week-4\\orders.csv'




# Load products, couriers, and orders
products = load_csv(PRODUCT_FILE)
couriers = load_csv(COURIERS_FILE)
orders = load_csv(ORDER_FILE)


order_status_list = ["Preparing", "Ready for delivery", "Dispatched"]


orders = []
orders = [{
            "customer_name": "Lord Raheem",
            "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
            "customer_phone": "0789887334",
            "courier": 2, # Courier index
            "status": "preparing",
            "items": "1, 3, 4" # Product index
}]




while True:
    print('MAIN MENU OPTION:\n0.Exit\n1.PRODUCTS MENU\n2.COURIER MENU\n3.ORDERS MENU')
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
                new_product_price = input ('\nEnter product price:\n')
            
                products.append({"name":new_product_input,
                                 "price":new_product_price
                                 })
                
                update_products(products)

                products = get_products()
                
                print("Updated list of products:\n")
                for product in products:
                    print(product["index"],product["name"],product["price"])
                
                print("\nNew product added. Is there something else we can help you with?\n")
                break
            
            #update product
            elif user_input == 3:
                products = get_products()
                for product in products:
                    print(f"{product['name']} at index {product['index']}")


                #get index value from user and store in variable      
                user_input_index = int (input ('\nEnter product index value you would you like to replace:\n'))
                #get product name from user and store in variable   
                user_input_product_name = input (f"\nWhich item will replace {products[user_input_index]["name"]}?\n")
                user_input_price = input (f"\nWhich price\n")

                #from products get item with requested index and assign requested new name 
                products[user_input_index]["name"] =  user_input_product_name
                products[user_input_index]["price"] = user_input_price
                
                update_products(products)

                print("\nUpdated products:\n")
               
                for product in products:
                     print(f"{product['name']}, {product['price']} at index {product['index']}")
                print("\nProducts updated successfully. Is there something else we can help you with?\n")
                break

            


             #delete product
            elif user_input == 4:
                products = get_products()
                for product in products:
                    print(f"{product['name']} at index {product['index']}")
                # GET user input for product index value
                user_input_index = int (input ('Enter product index would you like to delete:\n'))
                #DELETE product at index in products listi
                del products[user_input_index] 
                #GET user input for product index value
                update_products(products)

                print("\nUpdated products:\n")
                
                for product in products:
                    print(product["index"],product["name"],product["price"])
                print("\nProduct deleted. Is there something else we can help you with?")
                break

    elif main_menu_option == 2:
        while True:
            print("Choose from the following options:\n")
            user_input = int(input(f"COURIER MENU OPTIONS:\n0 - RETURN to main menu\n1 - PRINT couriers \n2 - CREATE new courier\n3 - UPDATE existing courier\n4 - DELETE courier\n"))
            #return to main menu
            if user_input == 0:
                break
            #print couriers list
            elif user_input == 1:
                get_couriers_list = get_couriers()
                for courier in get_couriers_list:
                    print(courier["index"],courier["name"],courier["phone"])

                print("\nIs there anything else we can help you with?\n")
                break


            #create new courier
            elif user_input == 2:
                new_courier_input = input ('\nEnter new courier:\n')
                new_courier_phone = input ('\nEnter courier phone:\n')
            
                couriers.append({"name":new_courier_input,
                                 "phone":new_courier_phone
                                 })
                
                update_couriers(couriers)

                couriers = get_couriers()
                
                print("Updated list of couriers:\n")
                for courier in couriers:
                    print(courier["index"],courier["name"],courier["phone"])
                
                print("\nNew courier added. Is there something else we can help you with?\n")
                break
            
            #update courier
            elif user_input == 3:
                couriers = get_couriers()
                for courier in couriers:
                    print(f"{courier['name']} at index {courier['index']}")

                #get index value from user and store in variable      
                user_input_index = int (input ('\nEnter courier index value you would you like to replace:\n'))
                #get courier name from user and store in variable   
                user_input_courier_name = input (f"\nWhich item will replace {couriers[user_input_index]["name"]}?\n")
                user_input_phone = input (f"\nWhich phone\n")

                #from couriers get item with requested index and assign requested new name 
                couriers[user_input_index]["name"] =  user_input_courier_name
                couriers[user_input_index]["phone"] = user_input_phone
                
                update_couriers(couriers)

                print("\nUpdated couriers:\n")
               
                for courier in couriers:
                     print(f"{courier['name']}, {courier['phone']} at index {courier['index']}")
                print("\ncourier updated successfully. Is there something else we can help you with?\n")
                break

            


             #delete courier
            elif user_input == 4:
                couriers = get_couriers()
                for courier in couriers:
                    print(f"{courier['name']} at index {courier['index']}")
                # GET user input for courier index value
                user_input_index = int (input ('Enter courier index would you like to delete:\n'))
                #DELETE courier at index in couriers list
                del couriers[user_input_index] 
                #GET user input for courier index value
                update_couriers(couriers)

                print("\nUpdated couriers:\n")
                
                for courier in couriers:
                    print(courier["index"],courier["name"],courier["phone"])
                print("\ncourier deleted. Is there something else we can help you with?")
                break


# # orders menu
    elif main_menu_option == 3:

        while True:
            print("Choose from the following options:\n")
            print('ORDER MENU OPTIONS:\n0. RETURN TO MAIN MENU \n1. PRINT ORDERS \n2. NEW ORDER\n3. UPDATE ORDER STATUS\n4. UPDATE EXISTING ORDER\n5. DELETE ORDER')       
            order_menu_option = int(input('choose an option from 0-5: '))
            #return to main menu
            if order_menu_option == 0:
                break
            

            elif order_menu_option == 1:
                for order in orders:
                    print(order)
                    print("\nIs there anything else we can help you with?\n")
                    break

                print("current orders:\n")
                for order in orders:
                        for k,v in order.items():
                            print(f"{k} : {v}")
                        print()
                print("\nThanks for viewing the orders. Is there anything else we can help you with?\n")
                break
            # create orders  
            # option 2:
            # Assuming orders is already defined as an empty list
            orders = []

            if order_menu_option == 2:
                customer_name = input('Enter customer name: ')
                customer_address = input('Enter customer address: ')
                customer_phone_number = input('Please enter your phone no: ')
                courier = int(input("Choose the courier index: "))
                status = input("What is the order status?: ")

                # Initialize an empty list for items
                items = []

                # Loop to add items to the order
                while True:
                    for idx, product in enumerate(products):
                        print(f"{idx}: {product['name']} - {product['price']}")
                    item_index = input('Please input the item number (or type "done" to finish): ')
                    if item_index.lower() == 'done':
                        break
                    else:
                        try:
                            item_index = int(item_index)
                            if 0 <= item_index < len(products):
                                items.append(item_index)
                            else:
                                print("Invalid item number. Please try again.")
                        except ValueError:
                            print("Invalid input. Please enter a number or 'done'.")

                # Create the order dictionary
                order = {
                    'customer name': customer_name,
                    'customer address': customer_address,
                    'customer phone number': customer_phone_number,
                    'courier': courier,
                    'status': status,
                    'items': items
                    }

                # Append the order dictionary to the orders list
                orders.append(order)

                update_orders(orders)

                orders = get_orders()
                
                print("Updated list of orders:\n")
                for order in orders:
                    print(order["customer name"],order["customer address"],order["customer phone number"],order["courier"],order["status"],order["items"])
                
                print("\nNew order added successfully!.\n Is there something else we can help you with?\n")
                break

            # UPDATE existing order status
            elif order_menu_option == 3:

                
                # # PRINT orders list with its index values
                # for index, item in enumerate(orders):
                #     print(f"{index}: {item['customer_name']} (Status: {item['status']})")

                # # GET user input for order index value
                # user_input_index = int(input('ENTER order index value to update status: '))

                # # CHECK if the provided index is valid
                # if 0 <= user_input_index < len(orders):
                #     # PRINT current status of the selected order
                #     print(f"Current status of order {user_input_index} ({orders[user_input_index]['customer_name']}): {orders[user_input_index]['status']}")

                #     # GET user input for new order status value
                #     status_update = input('What do you want to UPDATE status to: ')

                #     # UPDATE status for the selected order
                #     orders[user_input_index]['status'] = status_update
                #     print('Order status updated successfully!')

                # else:
                #     print('Invalid order index value.')

                # print('Is there anything else we can help you with?')






    # # UPDATE existing order status

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

    #         # ELSE IF user input is 4:
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

    #     FOR EACH key-value pair in selected order:
    #         GET user input for updated property
    #         IF user input is blank:
    #             do not update this property
    #         ELSE:
    #             update the property value with user input