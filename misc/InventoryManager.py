# A87654321

def display_menu():
    print("\nInventory Management System")
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Display current inventory")
    print("4. Exit")


def add_item(inventory):
    item_name = input("Enter the name of the item: ")
    if item_name in inventory:
        quantity = int(input("Enter the quantity to add: "))
        inventory[item_name] += quantity
    else:
        quantity = int(input("Enter the quantity: "))
        inventory[item_name] = quantity
    print(f"{quantity} {item_name}(s) added to inventory.")


def remove_item(inventory):
    item_name = input("Enter the name of the item to remove: ")
    if item_name in inventory:
        quantity = int(input("Enter the quantity to remove: "))
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
            print(f"{quantity} {item_name}(s) removed from inventory.")
        else:
            print("Insufficient quantity in inventory.")
    else:
        print("Item not found in inventory.")


def display_inventory(inventory):
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")


def main():
    inventory = {}

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            remove_item(inventory)
        elif choice == '3':
            display_inventory(inventory)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


main()
