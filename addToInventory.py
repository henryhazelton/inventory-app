# Add to inventory 

import inventory

def add_item():
    # Get the input for the new item
    item_name = input("Enter item name: ")
    item_quantity = int(input("Enter item quantity: "))

    # Load the existing inventory 
    inventory_data = inventory.import_inventory('inventory.csv')

    # Add new item to inventory 
    inventory_data.append([item_name, item_quantity])

    # Export updated inventory
    inventory.export_inventory('inventory.csv', inventory_data)