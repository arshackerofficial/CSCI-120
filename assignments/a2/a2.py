# 815805

# Inventory Management System

import os


def clear_screen():
    command = "cls" if os.name == "nt" else "clear"
    os.system(command)


def welcome():
    welcome = "Welcome to Inventory Management System! \n\n\
    1. Add an item\n\
    2. Remove an item\n\
    3. Display current inventory.\n\
    4.Exit\n"
    clear_screen()
    print(welcome)


def add_item(inventory):
    name = input("Enter item name: ").lower()

    try:
        quantity = int(input("Enter quantity: "))

        if quantity < 0:
            return "Quantity can not be negative, Use 'Remove an item' option to reduce items"
        if quantity == 0:
            return "Quantity not be zero"

        inventory[name] = quantity if name not in inventory else inventory[name] + quantity
        return f'{name.capitalize()} ({quantity}) added to the inventory.'
    except:
        return "Quantity can only be in integers"


def remove_item(inventory):

    name = input("Enter item name: ").lower()

    if name not in inventory:
        return "Item not found in inventory."

    try:
        quantity = int(input("Enter quantity: "))

        if quantity < 0:
            return "Quantity can not be negative, Use 'Add an item' option to add items"
        if quantity == 0:
            return "Quantity not be zero"

        if inventory[name] == quantity:
            inventory.pop(name)
        else:
            inventory[name] -= quantity
        return f'{name.capitalize()} ({quantity}) removed from the inventory.'
    except:
        return "Quantity can only be in integers"


def display_inventory(inventory):
    welcome()

    if inventory:
        print("==========================")
        print('%-12s%-3s%-12s' % ("Item Names", "|", "Quantity"))
        print("--------------------------")
        for i in inventory:
            print('%-12s%-3s%-12s' % (i.capitalize(), "|", inventory[i]))
        print("==========================\n")
    else:
        print("Inventory is empty!\n")


break_loop, items = False, {}

welcome()

while not break_loop:
    choice = input("Enter your Choice: ")
    msg = ""
    match choice:
        case "1":
            msg = add_item(items)
        case "2":
            msg = remove_item(items)
        case "3":
            display_inventory(items)
        case "4":
            clear_screen()
            print("Exiting Program......\n")
            break_loop = True
        case default:
            msg = "Please choose a valid option!"

    if not break_loop and choice != "3":
        welcome()
        print(msg + "\n")
