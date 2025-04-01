# View the inventory

import inventory

def view_inventory():
    # Load the existing inventory
    inventory_data = inventory.import_inventory('inventory.csv')

    # Display the current inventory
    print("Current Inventory:")
    for item in inventory_data:
        print(f"{item[0]} - {item[1]}") 