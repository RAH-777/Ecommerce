# add some product names 
# product_list = ['fanta', 'coke', 'sprite', 'lemonade', 'pepsi', 'miranda', 'soda']

userinput = input('MAIN MENU OPTIONS: 0. EXIT   1. PRODUCTS MENU')
if userinput == '0':
#EXIT app   
    exit()
elif userinput == '1':
    print('menu')
# 7777777777777777777777777777777777
# CreaTe new product
# Create an empty list to store product names
products = ['kiwi', 'lychee', 'passionfruit', 'strawberry'] 
 
while True:
    # Display the main menu options
    print('MAIN MENU OPTIONS:\n0. EXIT\n1. PRODUCTS MENU')
 
    # Get user input for main menu option
    main_menu_option = int(input('Enter your choice: '))
 
    if main_menu_option == 0:
        print('Exiting the application')
        break
    elif main_menu_option == 1:
        while True:
            #User input for products menu
            print('0. MAIN MENU\n1. PRODUCTS LIST\n2. CREATE NEW PRODUCT\n3. UPDATE EXISTING PRODUCT\n4. DELETING PRODUCT')
            #Products Menu
            user_input = int(input('Choose an option from 0-4 '))
            #Option 0: return to main menu
            if user_input == 0:
                print('Returning to main menu')
                break
            #Option 1: list products
            elif user_input == 1:
                print(products)
            #Option 2: add a product
            elif user_input == 2:
                new_product = input('Name the product you want to add: ')
                products.append(new_product)
                print(products)
            #Option 3: replace a product
            elif user_input == 3:
                print(products)
                for index, items in enumerate(products):
                    print(f'index {index}: {items}')
                position = int(input('enter the index you want to replace: '))
                if 0 <= position <= (len(products) - 1):
                    new_item = input('enter the new item you would like to add: ')
                    products[position] = new_item
                    print(f'Product added: {new_item}')
                    print (products)
                else:
                    print('Invalid index! Please try again.')
            #Option 4: delete a product
            elif user_input == 4:
                print(products)
                for index, items in enumerate(products):
                    print(f'index {index}: {items}')
                position = int(input('Enter the index of the product you want to delete: '))
                if 0 <= position < len(products):
                    removed_product = products.pop(position)
                    print(f'Product removed: {removed_product}')
                    print('Updated product list:', products)
                else:
                    print('Invalid index! Please try again.')
            else:
                print('Invalid option! Please try again.')
    else:
        print('Invalid option! Please try again.')




