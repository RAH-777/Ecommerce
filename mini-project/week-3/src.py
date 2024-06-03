
'''
additions to make
-what happening if no couriers in courist.txt

bugs-
when i have more than one order and i assign a courier the last letter
from the list of couriers is removed

'''

#product list

def get_products():
    with open("products.txt","r") as file:
        products = file.readlines()
        
    
    return(products)
    
loaded_products = get_products()

#remove newline at the end of each word
products = [i[:-1] for i in loaded_products]






orders = []
#keep asking for input
while True:

    #get response
    opening_response = int(input(f"0 - Exit\n1 - Product Menu\n2 Order Menu \n"))

    if opening_response == 0:
        exit("Program has exited")
       

    elif opening_response == 1:
        while True:
            #give user options and store response
            response = int(input("\n0 - Go back to main menu\n1 - See product list\n2 - Add product \n3 - Replace product \n4 - Delete product \n"))
            #go back to main menu
            if response == 0:
                break
            #show products 
            elif response == 1:
                
                for product in products:
                    print(product)
                print("\nProducts printed. Is there something else we can help you with?\n")
                break

            #add new product
            elif response == 2:
                new_product = input("\nEnter new products:\n")

                with open("products.txt", "a") as file:
                    file.write(f"{new_product}\n".capitalize())

                products = get_products()
                products = [i.strup() for i in products]
                print("Updated list of products:\n")
                for product in products:
                    print(product,end = "")
                
                print("\nNew product added. Is there something else we can help you with?\n")
                break
            
            #replace product
            elif response == 3:
                for idx, product in enumerate(products):
                    print(f"{product} at index : {idx}")
                
                idx_replace = int(input("\nWhich index would you like to replace:\n"))
                item_replace = input(f"\nWhich item will replace {products[idx_replace]}?\n")
                products[idx_replace] = item_replace
                with open("products.txt", "w") as file:
                    for product in products:
                        file.write(f"{product}\n".capitalize())

                print("\nUpdated products:\n")
                updated_products =get_products()
                for product in updated_products:
                    print(product, end = "")
                print("\nProduct updated. Is there something else we can help you with?\n")
                break
            
            #delete product
            elif response == 4:
                for idx, product in enumerate(products):
                    print(f"{product} at index : {idx}")

                idx_replace = int(input("\nWhich index would you like to delete:\n"))
                
                del products[idx_replace]

                with open("products.txt", "w") as file:
                    for product in products:
                        file.write(f"{product}\n".capitalize())

                print("\nUpdated products:\n")
                updated_products =get_products()
                for product in updated_products:
                    print(product, end = "")
                print("\nProduct deleted. Is there something else we can help you with?")
                break
            

    elif opening_response == 2:
       # orders = {"person": "apple",}
        while True:
            print("Choose from the following options:\n")
            user_input = int(input(f"0 - Return to main menu\n1 - Print orders\n2 - New order\n3 - Update order status\n4 - Update existing order\n5 - Delete order\n6 - Add Courier to order\n7 - Edit Couriers\n"))

            #return to main menu
            if user_input == 0:
                break
            #print orders 
            if user_input == 1:
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
              
            #add new customer
            if user_input == 2:
                new_customer = input("Enter new customer name:\n").lower()
                products = get_products()
                #show menu
                print("\nMenu:\n")

                # for product in products:
                products = [i.strip() for i in products]
                for product in products:
                    print(product)

                
                new_order = input(f"\nHello {new_customer.capitalize()}. What item would you like?\n")
                #check if on the menu
                if new_order.capitalize() not in products:
                    print("\nSorry that product is unavailable")
                    print("\nIs there anything else we can help you with?\n")
                    break
                
                
                new_phone = input("Input phone number:\n")
                new_address = input("Input address:\n")
                status = "accepted"

                orders.append({"Name": new_customer,
                              "Order": new_order,
                              "Contact number": new_phone,
                              "Address": new_address,
                              "Status": status,
                              "Courier" : "Unassigned",


                              })
                
                print("\nThanks for your order, is there anything else we can help you with?\n")
                break
                        
                
            #update order status
            if user_input == 3:
                update_customer = input("Which order would you like to update the status of? \n")
                #check if order is in orders
                order_names = [i["Name"] for i in orders]
                if update_customer.lower() not in order_names:
                    print("\nSorry, there is no order under that name\n")
                    print("Is there anything else we can help you with?\n")
                    break
                print("\nOur update status options are:\naccepted\npreparing\nout for delivery\ndelivered\n")
                status_update = input(f"What would you like to update status to?\n").lower()
                update_options = ["accepted","preparing","out for delivery", "delivered"]
                if status_update.lower() not in update_options:
                    print("\nThat is not an accepted status. Is there anything else we can help you with?\n")
                    break
                

                #get index to find correct order in the list
                name_idx = order_names.index(update_customer.lower())



                orders[name_idx]["Status"] = status_update
                #if status == deliered add the courier back to list of courriers
                if status_update == "delivered":
                    with open("couriers.txt" , "a") as file:
                        file.write(F"{orders[name_idx]['Courier']}\n")



                print()
                for k,v in orders[name_idx].items():
                    print(f"{k} : {v}")

                print("\nThanks for updating the status the order, is there anything else we can help you with?\n")
                break
            


        
            #update existing order
            if user_input == 4:
                update_customer = input("Which order would you like to update? \n")
                #check if order is in orders
                order_names = [i["Name"] for i in orders]
                if update_customer.lower() not in order_names:
                    print("Sorry, there is no order under that name\n")
                    print("Is there anything else we can help you with?\n")
                    break
                print("\nMenu: \n")
                for product in products:
                    print(product)

                order_update = input(f"\nWhich product would you like instead?\n")
                if order_update.capitalize() not in products:
                    print("\nSorry that product is unavailable")
                    print("\nIs there anything else we can help you with?\n")
                    break

                #get index to find correct order in the list
                name_idx = order_names.index(update_customer.lower())

                orders[name_idx]["Order"] = order_update

                for k,v in orders[name_idx].items():
                    print(f"{k} : {v}")

                print("\nThanks for updating the order, is there anything else we can help you with?\n")
                break
            
                    
            #delete order
            if user_input == 5:
                update_customer = input("Which order would you like to delete? \n")
                #check if order is in orders
                order_names = [i["Name"] for i in orders]
                if update_customer.lower() not in order_names:
                    print("Sorry, there is no order under that name\n")
                    print("Is there anything else we can help you with?\n")
                    break

                #get index to find correct order in the list
                name_idx = order_names.index(update_customer.lower())

                del orders[name_idx]

            

                print("\nOrder deleted, is there anything else we can help you with?\n")
                break

            #add courier to order
            if user_input == 6:
                #read in the list of couriers
                with open("couriers.txt", "r") as file:
                    top_courier = file.readlines()
                
                couriers = [i[:-1] for i in top_courier]

                update_customer = input("Which order would you like to add courier to?\n")
                order_names = [i["Name"] for i in orders]
                if update_customer.lower() not in order_names:
                    print("Sorry, there is no order under that name\n")
                    print("Is there anything else we can help you with?\n")
                    break

                #get index to find correct order in the list
                name_idx = order_names.index(update_customer.lower())
                #assign courier 
                orders[name_idx]["Courier"] = couriers[0]

                #update status
                orders[name_idx]["Status"] = "out for delivery"

                print(f"\n{couriers[0]} was assigned the order for {orders[name_idx]['Name']} ")
                print("Is there anything else we can help you with?\n")

                #remove top courier from couriers.txt
                with open("couriers.txt", "w") as file:
                    for courier in couriers[1:]:
                        file.write(f"{courier}\n")
                
                break

            #add or delete a courier
            if user_input == 7:
                answer = input("Enter del to delete  or add to add a Courier:\n").strip()
                
                if answer == "add":
                    #add courier
                    new_courier = input("Input name of new Courier: \n")
                    with open("couriers.txt","a") as file:
                        file.write(f"{new_courier}\n".capitalize())
                    
                    print(f"\n{new_courier.capitalize()} was added as a Courier")
                    print("Is there anything else we can help you with?\n")
                    break



                elif answer == "del":
                    #list_of_courriers = []
                    with open("couriers.txt","r") as file:
                        list_of_courriers = file.readlines()
                    list_of_courriers = [i[:-1] for i in list_of_courriers]
                    print("Current Couriers:\n")
                    for courier in list_of_courriers:

                        print(courier)

                    who_del = input("\nWho would you like to remove from the list?\n")
                    #get index of that person in list and remove
                    if who_del.capitalize() not in list_of_courriers:
                        print("Sorry, there is no order under that name\n")
                        print("Is there anything else we can help you with?\n")
                        break

                    #get index of that person in list and remove  
                    del_idx = list_of_courriers.index(who_del.capitalize())
                    del list_of_courriers[del_idx]

                    #rewrite the list to the file
                    with open("couriers.txt","w") as file:
                        for courier in list_of_courriers:
                            file.write(f"{courier}\n")
                    print(f"\n{who_del.capitalize()} was deleted as a Courier")
                    print("Is there anything else we can help you with?\n")
                    break


                else:
                    print("Command not recognized")
                    print("Is there anything else we can help you with?\n")
                    break






        