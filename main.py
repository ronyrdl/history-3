from app import *

# Display menu and return selected option
def menu():
    print("\n--- MENU ---")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Show statistics")
    print("7. Save CSV")
    print("8. Load CSV")
    print("9. Exit")

    try:
        # Convert user input to integer
        return int(input("Choose an option: "))
    except ValueError:
        # Handle invalid input
        print("Invalid input")
        return 0


# Control variable for main loop
valid = 0

# Main program loop
while valid == 0:
    option = menu()

    # Call functions based on user option
    if option == 1:
        add_products(inventory)

    elif option == 2:
        show_products(inventory)

    elif option == 3:
        search_product(inventory)

    elif option == 4:
        update_products(inventory)

    elif option == 5:
        delete_product(inventory)

    elif option == 6:
        calculate_statistics(inventory)

    elif option == 7:
        save_csv(inventory)
    
    elif option == 8:
        load_csv(inventory)

    elif option == 9:
        # Exit program
        print("Goodbye")
        valid = 1

    else:
        # Handle invalid menu option
        print("Invalid option")
