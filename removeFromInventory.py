# Remove items from inventory

import inventory

def remove_item():
    # Load the current inventory
    inventory_data = inventory.import_inventory('inventory.csv')

    # Display the current inventory 
    print("Current Inventory:")
    for i, item in enumerate(inventory_data):
        print(f"{i+1}. {item[0]} - {item[1]}")

    # Get item to remove
    index = int(input("Enter the index of the item to edit: ")) - 1

    # Remove the item from the inventory
    if 0 <= index <= len(inventory_data):
        del inventory_data[index] # Deletes the item at the index the user specified
        # Now update the csv file
        inventory.export_inventory('inventory.csv', inventory_data)
        print("Item successfully removed")
    else:
        print("Invalid Index")