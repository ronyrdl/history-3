from errores import errores

# List to store all products
inventory = []

# Add a new product using validated input
def add_products(inventory):
    name = errores("Please enter the product name: ")
    price = errores("Enter the product price: ", float)
    amount = errores("Enter the quantity: ", int)

    # Create product dictionary
    product = {
        "name": name,
        "price": price,
        "amount": amount
    }

    inventory.append(product)
    print("Product added successfully")


# Display all products in inventory
def show_products(inventory):
    if len(inventory) == 0:
        print("No products registered")
        return

    for product in inventory:
        print(f"Product: {product['name']}\nPrice: {product['price']}\nQuantity: {product['amount']}\n")


# Search a product by name
def search_product(inventory):
    if len(inventory) == 0:
        print("Inventory is empty")
        return

    name = errores("Enter product name to search: ")

    # Compare names ignoring case
    for product in inventory:
        if product["name"].lower() == name.lower():
            print("Product found:")
            print(f"Name: {product['name']}")
            print(f"Price: {product['price']}")
            print(f"Quantity: {product['amount']}")
            return

    print("Product not found")


# Update price and quantity of a product
def update_products(inventory):
    if len(inventory) == 0:
        print("Inventory is empty")
        return

    name = errores("Enter the product name to update: ")
    exist = False

    for product in inventory:
        if product["name"].lower() == name.lower():
            exist = True

            # Validate new price (no negatives)
            new_price = errores("Enter the new price: ", float)
            while new_price < 0:
                print("Price cannot be negative")
                new_price = errores("Enter the new price: ", float)

            # Validate new quantity (no negatives)
            new_amount = errores("Enter the new quantity: ", int)
            while new_amount < 0:
                print("Quantity cannot be negative")
                new_amount = errores("Enter the new quantity: ", int)

            product["price"] = new_price
            product["amount"] = new_amount

            print("Product updated successfully")
            break

    if not exist:
        print("Product not found")


# Delete a product from inventory
def delete_product(inventory):
    if len(inventory) == 0:
        print("Inventory is empty")
        return

    name = errores("Enter the product name to delete: ")
    exist = False

    for product in inventory:
        if product["name"].lower() == name.lower():
            inventory.remove(product)
            exist = True
            print("Product deleted successfully")
            break

    if not exist:
        print("Product not found")


# Calculate statistics of the inventory
def calculate_statistics(inventory):
    if len(inventory) == 0:
        print("Inventory is empty")
        return

    total_units = 0
    total_value = 0

    # Initialize with first product
    most_expensive = inventory[0]
    highest_stock = inventory[0]

    for product in inventory:
        subtotal = product["price"] * product["amount"]

        total_units += product["amount"]
        total_value += subtotal

        # Find most expensive product
        if product["price"] > most_expensive["price"]:
            most_expensive = product

        # Find product with highest stock
        if product["amount"] > highest_stock["amount"]:
            highest_stock = product

    print("\n--- STATISTICS ---")
    print(f"Total units: {total_units}")
    print(f"Total value: {total_value}")
    print(f"Most expensive product: {most_expensive['name']} - {most_expensive['price']}")
    print(f"Highest stock product: {highest_stock['name']} - {highest_stock['amount']}")


# Save inventory data into a CSV file
def save_csv(inventory, path):
    if len(inventory) == 0:
        print("Inventory is empty, nothing to save")
        return

    try:
        # Open file in write mode
        with open(path, "w", encoding="utf-8") as file:
            file.write("name,price,amount\n")

            # Write each product as a line
            for product in inventory:
                line = f"{product['name']},{product['price']},{product['amount']}\n"
                file.write(line)

        print(f"Inventory saved in: {path}")

    except PermissionError:
        print("Error: No permission to write file")
    except Exception as e:
        print(f"Error saving file: {e}")