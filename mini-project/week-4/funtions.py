import csv

# Define file paths
PRODUCT_FILE = 'C:\\Users\\lordr\\Documents\\Python\\Raheem-miniproject\\mini-project\\week-4\\products.csv'
COURIER_FILE = 'C:\\Users\\lordr\\Documents\\Python\\Raheem-miniproject\\mini-project\\week-4\\couriers.csv'
ORDER_FILE = 'C:\\Users\\lordr\\Documents\\Python\\Raheem-miniproject\\mini-project\\week-4\\orders.csv'

def load_products():
    products = []
    with open(PRODUCT_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({'name': row['name'], 'price': float(row['price'])})
    return products

def load_couriers():
    couriers = []
    with open(COURIER_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            couriers.append({'name': row['name'], 'phone': row['phone']})
    return couriers

def load_orders():
    orders = []
    with open(ORDER_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            orders.append({
                'customer_name': row['customer_name'],
                'customer_address': row['customer_address'],
                'customer_phone': row['customer_phone'],
                'courier': int(row['courier']),
                'status': row['status'],
                'items': row['items']
            })
    return orders

def save_data(file_path, data, fieldnames):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

def save_products(products):
    save_data(PRODUCT_FILE, products, ['name', 'price'])

def save_couriers(couriers):
    save_data(COURIER_FILE, couriers, ['name', 'phone'])

def save_orders(orders):
    save_data(ORDER_FILE, orders, ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items'])

# Example usage
products = load_products()
couriers = load_couriers()
orders = load_orders()

# Save data back to files (ensure to call these at appropriate places in your application)
save_products(products)
save_couriers(couriers)
save_orders(orders)








# Load data from CSV files
def load_data(filename):
    data = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Save data to CSV files
def save_data(filename, data, fieldnames):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)





# Initialize data
products = load_data(PRODUCT_FILE)
couriers = load_data(COURIER_FILE)
orders = load_data(ORDER_FILE)
order_status_list = ["preparing", "out for delivery", "delivered"]

# Main menu options
def print_main_menu():
    print("\nMain Menu:")
    print("1. Products")
    print("2. Couriers")
    print("3. Orders")
    print("0. Exit")

# Product menu options
def print_product_menu():
    print("\nProduct Menu:")
    print("1. View Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("0. Return to Main Menu")

# Courier menu options
def print_courier_menu():
    print("\nCourier Menu:")
    print("1. View Couriers")
    print("2. Add Courier")
    print("3. Update Courier")
    print("4. Delete Courier")
    print("0. Return to Main Menu")

# Order menu options
def print_order_menu():
    print("\nOrder Menu:")
    print("1. View Orders")
    print("2. Add Order")
    print("3. Update Order Status")
    print("4. Update Order")
    print("5. Delete Order")
    print("0. Return to Main Menu")

# Main program loop
while True:
    print_main_menu()
    user_input = int(input("\nEnter your choice: "))

    if user_input == 0:
        save_data('C:\Users\lordr\Documents\Python\Raheem-miniproject\mini-project\week-4\products.csv', products, ['name', 'price'])
        save_data('couriers.csv', couriers, ['name', 'phone'])
        save_data('orders.csv', orders, ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items'])
        print("Data saved. Exiting the application.")
        break

    elif user_input == 1:
        while True:
            print_product_menu()
            product_input = int(input("\nEnter your choice: "))
            
            if product_input == 0:
                break
            elif product_input == 1:
                print("\nCurrent Products:")
                for product in products:
                    print(f"{product['name']} - ${product['price']}")
            elif product_input == 2:
                name = input("Enter product name: ")
                price = input("Enter product price: ")
                products.append({'name': name, 'price': price})
                print("Product added successfully.")
            elif product_input == 3:
                for i, product in enumerate(products):
                    print(f"{i}. {product['name']} - ${product['price']}")
                index = int(input("Enter product index to update: "))
                if 0 <= index < len(products):
                    for key in products[index]:
                        new_value = input(f"Enter new value for {key} (leave blank to keep '{products[index][key]}'): ")
                        if new_value:
                            products[index][key] = new_value
                    print("Product updated successfully.")
                else:
                    print("Invalid index.")
            elif product_input == 4:
                for i, product in enumerate(products):
                    print(f"{i}. {product['name']} - ${product['price']}")
                index = int(input("Enter product index to delete: "))
                if 0 <= index < len(products):
                    products.pop(index)
                    print("Product deleted successfully.")
                else:
                    print("Invalid index.")
            else:
                print("Invalid option. Please try again.")

    elif user_input == 2:
        while True:
            print_courier_menu()
            courier_input = int(input("\nEnter your choice: "))
            
            if courier_input == 0:
                break
            elif courier_input == 1:
                print("\nCurrent Couriers:")
                for courier in couriers:
                    print(f"{courier['name']} - {courier['phone']}")
            elif courier_input == 2:
                name = input("Enter courier name: ")
                phone = input("Enter courier phone number: ")
                couriers.append({'name': name, 'phone': phone})
                print("Courier added successfully.")
            elif courier_input == 3:
                for i, courier in enumerate(couriers):
                    print(f"{i}. {courier['name']} - {courier['phone']}")
                index = int(input("Enter courier index to update: "))
                if 0 <= index < len(couriers):
                    for key in couriers[index]:
                        new_value = input(f"Enter new value for {key} (leave blank to keep '{couriers[index][key]}'): ")
                        if new_value:
                            couriers[index][key] = new_value
                    print("Courier updated successfully.")
                else:
                    print("Invalid index.")
            elif courier_input == 4:
                for i, courier in enumerate(couriers):
                    print(f"{i}. {courier['name']} - {courier['phone']}")
                index = int(input("Enter courier index to delete: "))
                if 0 <= index < len(couriers):
                    couriers.pop(index)
                    print("Courier deleted successfully.")
                else:
                    print("Invalid index.")
            else:
                print("Invalid option. Please try again.")

    elif user_input == 3:
        while True:
            print_order_menu()
            order_input = int(input("\nEnter your choice: "))
            
            if order_input == 0:
                break
            elif order_input == 1:
                print("\nCurrent Orders:")
                for order in orders:
                    for key, value in order.items():
                        print(f"{key}: {value}")
                    print()
            elif order_input == 2:
                customer_name = input("Enter customer name: ")
                customer_address = input("Enter customer address: ")
                customer_phone = input("Enter customer phone number: ")

                print("\nAvailable Products:")
                for i, product in enumerate(products):
                    print(f"{i}. {product['name']} - ${product['price']}")
                items = input("Enter product indexes (comma-separated): ")

                print("\nAvailable Couriers:")
                for i, courier in enumerate(couriers):
                    print(f"{i}. {courier['name']} - {courier['phone']}")
                courier_index = int(input("Enter courier index: "))
                
                status = "preparing"

                new_order = {
                    'customer_name': customer_name,
                    'customer_address': customer_address,
                    'customer_phone': customer_phone,
                    'courier': courier_index,
                    'status': status,
                    'items': items
                }
                orders.append(new_order)
                print("Order added successfully.")
            elif order_input == 3:
                for i, order in enumerate(orders):
                    print(f"{i}. {order['customer_name']} - {order['status']}")
                index = int(input("Enter order index to update status: "))
                if 0 <= index < len(orders):
                    for i, status in enumerate(order_status_list):
                        print(f"{i}. {status}")
                    status_index = int(input("Enter status index: "))
                    if 0 <= status_index < len(order_status_list):
                        orders[index]['status'] = order_status_list[status_index]
                        print("Order status updated successfully.")
                    else:
                        print("Invalid status index.")
                else:
                    print("Invalid order index.")
            elif order_input == 4:
                for i, order in enumerate(orders):
                    print(f"{i}. {order['customer_name']} - {order['status']}")
                index = int(input("Enter order index to update: "))
                if 0 <= index < len(orders):
                    for key in orders[index]:
                        new_value = input(f"Enter new value for {key} (leave blank to keep '{orders[index][key]}'): ")
                        if new_value:
                            orders[index][key] = new_value
                    print("Order updated successfully.")
                else:
                    print("Invalid order index.")
            elif order_input == 5:
                for i, order in enumerate(orders):
                    print(f"{i}. {order['customer_name']} - {order['status']}")
                index = int(input("Enter order index to delete: "))
                if 0 <= index < len(orders):
                    orders.pop(index)
                    print("Order deleted successfully.")
                else:
                    print("Invalid order index.")
            else:
                print("Invalid option. Please try again.")
