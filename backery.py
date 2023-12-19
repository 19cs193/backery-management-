import csv
from datetime import datetime

class BakeryManagementSystem:
    def __init__(self):
        self.products = []
        self.orders = []

    def add_product(self, name, price):
        product = {'name': name, 'price': price}
        self.products.append(product)
        print(f"Product '{name}' added successfully!")

    def place_order(self, name, address, contact_number, product_name, quantity):
        product = next(p for p in self.products if p['name'] == product_name)
        amount = quantity * product['price']
        order = {'name': name, 'address': address, 'contact_number': contact_number,
                 'product_name': product_name, 'quantity': quantity, 'amount': amount,
                 'order_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        self.orders.append(order)
        print("Order placed successfully!")

    def search_buyers_details(self, name):
        matching_orders = [order for order in self.orders if order['name'] == name]
        if matching_orders:
            for order in matching_orders:
                print(f"Order Date: {order['order_date']}, Product: {order['product_name']}, Quantity: {order['quantity']}, Amount: {order['amount']}")
        else:
            print(f"No orders found for buyer: {name}")

    def export_to_excel(self, filename='orders.csv'):
        with open(filename, mode='w', newline='') as file:
            fieldnames = ['name', 'address', 'contact_number', 'product_name', 'quantity', 'amount', 'order_date']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.orders)
        print(f"Data exported to {filename} successfully!")

# Main Program
bakery_system = BakeryManagementSystem()

while True:
    print("\nBakery Management System\n")
    print("1. Add Product")
    print("2. Place Order")
    print("3. Search Buyer's Details")
    print("4. Export to Excel")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter product name: ")
        price = float(input("Enter product price in INR: "))
        bakery_system.add_product(name, price)

    elif choice == '2':
        name = input("Enter buyer's name: ")
        address = input("Enter buyer's address: ")
        contact_number = input("Enter buyer's contact number: ")
        product_name = input("Enter product name to order: ")
        quantity = int(input("Enter quantity: "))
        bakery_system.place_order(name, address, contact_number, product_name, quantity)

    elif choice == '3':
        name = input("Enter buyer's name to search: ")
        bakery_system.search_buyers_details(name)

    elif choice == '4':
        filename = input("Enter filename for export (default is orders.csv): ")
        bakery_system.export_to_excel(filename)

    elif choice == '5':
        print("Exiting the Bakery Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
