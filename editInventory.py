# Edit the inventory

import inventory

def edit_item():
    # First, load the current inventory
    inventory_data = inventory.import_inventory('inventory.csv')

    # Now display the current inventory so the user can choose what to edit
    print("Current Inventory:")
    for i, item in enumerate(inventory_data):
        print(f"{i+1}. {item[0]} - {item[1]}") # This displays the current inventory such as 

    # Get input for item that will be edited
    index = int(input("Enter the index of the item to edit: ")) - 1 # The -1 at the end is so that the computer is editing the human intended, as computers count from zero

    # Edit the item in the inventory
    if 0 <= index <= len(inventory_data):
        new_quantity = int(input("Enter the new quantity: "))
        inventory_data[index][1] = new_quantity
        inventory.export_inventory('inventory.csv', inventory_data)
        print("Item edited successfully")
    else:
        print("Invalid Index")