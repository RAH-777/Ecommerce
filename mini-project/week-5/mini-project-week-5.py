from functions import clear_screen,update_products, show_updated_products, show_main_menu, show_orders_menu,get_products,get_couriers,update_couriers,get_orders,update_orders

def main():

    while True:
        clear_screen()
        opening_response = show_main_menu()

        if opening_response == 0:
            clear_screen()
            print("Program Exited.")
            exit()

        elif opening_response == 1:
            clear_screen()
            show_product_menu()

        elif opening_response == 2:
            clear_screen()
            show_orders_menu()

        elif opening_response == 3:
            clear_screen()
            show_courier_menu()

        else:
            print("Please choose from one of the options")


def show_product_menu():
    clear_screen()
    #product_list_of_dicts = []
    while True:
        try:
            main_menu_response = int(input("Product menu:\n\n0 - Go back to main menu\n1 - See product list\n2 - Add product \n3 - Replace product \n4 - Delete product \n"))
            if 0 < main_menu_response > 4:
                raise ValueError

        except ValueError:
            clear_screen()
            print("Please choose from the options.")
            continue

        #if 0 go back to opening menu
        if main_menu_response == 0:
            clear_screen()
            return

        #if 1
        elif main_menu_response == 1:
            products = get_products()
            clear_screen()
            if len(products) < 1:
                print("No items currently in product list.")
                print("\nIs there something else we can help you with?\n")
                #break
            else:
                print("Menu: \n")
                for product in products:
                    #print name and price to 2 decimal places

                    print(f"{product['product_id']} {product['name']}: £{float(product['price']) :. 2f} qty: {product['qty']}")

                print("\nProducts printed. Is there something else we can help you with?\n")

        #add new product
        elif main_menu_response == 2:
            clear_screen()
            while True:
                new_product = input("\nEnter new product name:\n")
                clear_screen()
                if len(new_product) < 1:
                    print("You did not enter a name.")
                else:
                    break
            while True:
                try:
                    #make sure price is a float
                    new_price = float(input("Enter price: £"))

                    #check range of price
                    if new_price <= 0:
                        raise ValueError
                    elif new_price >= 100_000_000.00:
                        raise ValueError
                    break

                except ValueError:
                    clear_screen()
                    print("The price was not accepted.")
                    print(f"\nEnter valid price for {new_product}.\n")

            while True:
                try:
                    #make sure price is a float
                    new_qty = int(input("Enter quantity:\n"))

                    #check range of price
                    if new_price <= 0:
                        raise ValueError
                    elif new_price >= 100_000_000.00:
                        raise ValueError
                    break
                except ValueError:
                    clear_screen()
                    print("The price was not accepted.")
                    print(f"\nEnter valid price for {new_product}. \n")

            #format price
            new_price = float(new_price)
            new_price = format(new_price, '.2f')

            #store new product info in dict
            products = get_products()
            new_product_index = len(products)
            new_product_dict = {"name":new_product.capitalize(),"price":new_price, "index": new_product_index}

            #ADD THAT TO LIST OF PRODUCTS (WHICH IS A LIST OF DICTS)
            products.append(new_product_dict)
            #WRITE UPDATED LIST OF DICTS TO THE DATA BASE

            update_products(products)

            clear_screen()
            print(f"{new_product.capitalize()} added to products at a price of f{float(new_price) :. 2f}\n\nIs there something else we can help you with?")

        #replace product
        elif main_menu_response == 3:
            #get updated list of products
            products = get_products()
            clear_screen()
            #check there are products in on the menu
            if len(products) < 1:
                print("No items currently in product list.")
                print("\nIs there something else we can help you with?\n")
                break

            #print each item name with index in product list
            for idx, product_dict in enumerate(products):
                print(f"{product_dict['name']} at index : {idx}")

            #until user gives valid index needs to work for decimals/out of range/non numeric
            while True:
                try:
                    #take input
                    idx_replace = input("\nWhich index would you like to replace:\n")

                    #try to convert
                    idx_replace = int(idx_replace)

                    #check range
                    if idx_replace < 0 or idx_replace >- len(products):
                        raise ValueError("Value error raised")
                    clear_screen()
                    break

                except ValueError:
                    clear_screen()
                    for idx, product_dict in enumerate(products):
                        print(f"{product_dict['name']} at index : {idx}")
                    print(f"\nPlease input an index value between 0 and {len(products)-1}")
            
            while True:
                #take item name
                item_replace = input(f"\nWhich item will replace {products[idx_replace]['name']}?\n")
                clear_screen()

                #check they input something
                if len(item_replace) < 1:
                    print("You did not enter a name.")

                #if they did fill it out break
                else:
                    break

            while True:
                try:                   
                    #make sure price is a float
                    new_price = float(input("Enter price: f"))

                    #check range of price
                    if new_price <= 0:
                        raise ValueError
                    elif new_price >= 100_000_000.00:
                        raise ValueError
                    break

                except ValueError:
                    clear_screen()
                    print("The price was not accepted.")
                    print(f"\nEnter valid price for {new_product}. \n")

            #update new vals in dict
            products[idx_replace]['name'] = item_replace.capitalize()
            products[idx_replace]['price'] = new_price

            update_products(products)
            show_updated_products()
            print("\nProduct updated. Is there something else we can help you with?\n")

        #delete product
        elif main_menu_response == 4:

            products = get_products()
            while True:
                clear_screen()
                for idx, product in enumerate(products):
                    print(f"{product['name']} at index : {idx}")

                try:
                    #take input
                        idx_replace - input("\nWhich index would you like to delete:\n")

                        #try to convert
                        idx_replace = int(idx_replace)

                        #check range
                        if idx_replace < 0 or idx_replace >= len(products):
                            raise ValueError("Value error raised")
                        clear_screen()
                        break

                except ValueError:
                        clear_screen()
                        for idx, product_dict in enumerate(products):
                            print(f"{product_dict['name']} at index : {idx}")
                        print(f"\nPlease input an index value between 0 and {len(products)-1}")
            #remove product from list
            del products[idx_replace]

            #update csv file
            update_products(products)
            clear_screen()
            print("Product deleted. Is there something else we can help you with?\n")

        else:
            clear_screen()
            print("Please choose from the options")



# def show_orders_menu():
#     def show_orders_menu():
#     clear_screen()
#     #orders will be dict in this list
#     orders = []

#     #keep asking for input
#     while True:

#         try:
#             order_menu_response = int(input("Orders menu\n\n0 - Go back to main menu\n1 - List orders\n2 - New order\n3 - Update order status\n4 - Update order items\n5 - Delete order\n6 - "))
#             if 0 < order_menu_response > 6:
#                 raise ValueError

#             except ValueError:
#                 clear_screen()
#                 print("Please choose from the options.")
#                 ontinue

#                 #return to main menu
#             if order_menu_response == 0:
#                 return

#             #show orders
#             elif order_menu_response -- 1:
#                 orders = get_orders()
#                 print()
#                 if len(orders) < 1:
#                     clear_screen()
#                     print("There are currently no orders\n")
#                     print("Is there something else we can help you with?\n")

#                 else:
#                     clear_screen()
#                     for order in orders:






# def show_courier_menu(): ...







if __name__ == "__main__":
    main()


