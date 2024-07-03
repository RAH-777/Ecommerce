import csv

# Function to load orders from a CSV file
def load_orders_from_csv(file_path):
    orders = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['items'] = [int(item) for item in row['items'].split(',')]
            orders.append(row)
    return orders

# Function to save orders to a CSV file
def save_orders_to_csv(file_path, orders):
    with open(file_path, mode='w', newline='') as file:
        fieldnames = ['customer_name', 'customer_address', 'customer_phone_number', 'courier', 'status', 'items']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for order in orders:
            order['items'] = ','.join(map(str, order['items']))
            writer.writerow(order)

# Load the existing orders from the CSV file
orders_file_path = 'orders.csv'
orders = load_orders_from_csv(orders_file_path)

# Function to print all orders
def print_orders(orders):
    for index, order in enumerate(orders):
        print(f"{index}: {order}")

# Main code
order_menu_option = int(input("Enter order menu option (2 to create, 3 to update status, 4 to update order): "))

if order_menu_option == 2:
    customer_name = input('Enter customer name: ')
    customer_address = input('Enter customer address: ')
    customer_phone_number = input('Please enter your phone number: ')
    courier = int(input("Choose the courier index: "))
    status = input("What is the order status?: ")

    items = []
    while True:
        item = input('Please input the item number (or type "done" to finish): ')
        if item.lower() == 'done':
            break
        try:
            item_index = int(item)
            items.append(item_index)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    order = {
        'customer_name': customer_name,
        'customer_address': customer_address,
        'customer_phone_number': customer_phone_number,
        'courier': courier,
        'status': status,
        'items': items
    }

    orders.append(order)
    print("Order added successfully!")
    save_orders_to_csv(orders_file_path, orders)

elif order_menu_option == 3:
    for index, item in enumerate(orders):
        print(index, item['customer_name'])

    user_input_index = int(input('ENTER order index value to update status: '))
    if user_input_index < 0 or user_input_index >= len(orders):
        print("Invalid order index")
    else:
        status_update = input('What do you want to update status to: ')
        orders[user_input_index]['status'] = status_update
        print('Status updated successfully!')
        save_orders_to_csv(orders_file_path, orders)

elif order_menu_option == 4:
    for index, item in enumerate(orders):
        print(index, item['customer_name'])

    user_input_index = int(input("ENTER order index value to update existing order: "))
    if user_input_index < 0 or user_input_index >= len(orders):
        print("Invalid order index")
    else:
        order_to_update = orders[user_input_index]

        for key, value in order_to_update.items():
            if key != 'items':
                new_value = input(f"Enter new value for {key} (press Enter to keep '{value}'): ")
                if new_value.strip():
                    order_to_update[key] = new_value
            else:
                new_items = input(f"Enter new items (comma separated) or press Enter to keep '{value}': ")
                if new_items.strip():
                    order_to_update[key] = [int(item) for item in new_items.split(',')]

        print("Order updated successfully!")
        save_orders_to_csv(orders_file_path, orders)

else:
    print("Invalid menu option")

print_orders(orders)
