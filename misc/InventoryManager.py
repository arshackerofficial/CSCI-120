def show_menu():
    print("\n\nWelcome to the Inventory Manager!")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display inventory")
    print("4. Exit\n")


def add_item(inventory):
    name = input("Enter item name: ").lower()
    try:
        quantity = int(input("How many do you want to add? "))
        if quantity <= 0:
            print("You can't add 0 or negative items!")
            return
        inventory[name] = quantity if name not in inventory else inventory[name] + quantity
        print(f'{name.capitalize()} ({quantity}) added successfully.')
    except:
        print("Invalid input! Please enter a number.")


def remove_item(inventory):
    name = input("Enter item name: ").lower()
    if name not in inventory:
        print("Item not found!")
        return
    try:
        quantity = int(input("How many do you want to remove? "))
        if quantity <= 0:
            print("You can't remove 0 or negative items!")
            return
        if inventory[name] == quantity:
            inventory.pop(name)
        else:
            inventory[name] -= quantity
        print(f'{name.capitalize()} ({quantity}) removed successfully.')
    except:
        print("Invalid input! Please enter a number.")


def display_inventory(inventory):
    if inventory:
        print("\nCurrent Inventory:")
        for item, quantity in inventory.items():
            print(f"{item.capitalize()}: {quantity}")
    else:
        print("\nInventory is empty!")


items = {}

while True:
    show_menu()
    choice = input("What do you want to do? ")
    if choice == "1":
        add_item(items)
    elif choice == "2":
        remove_item(items)
    elif choice == "3":
        display_inventory(items)
    elif choice == "4":
        print("Exiting program...\n")
        break
    else:
        print("Invalid choice! Please choose from 1 to 4.")
