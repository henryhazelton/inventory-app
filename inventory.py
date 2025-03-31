# inventory.py file

import csv

# a function to import an inventory from a csv file
def import_inventory(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file) #this reads the file, denoted from the little 'r' in the with open line, and the contents that were read were stored in the variable file
            inventory = list(reader) #this creates a new variable called inventory and this stores a list of the read contents
        return inventory
    except FileNotFoundError:
        print("File not found. Creating now...")
        return [] #returns an empty list, currently unsure how this fits in
    
# a function to export the inventory as a csv file
def export_inventory(file_name, inventory):
    try:
        with open(file_name, 'w', newline='') as file: #this line creates a new variable called file and it has in it written content (i think? not too sure how the newline='' works)
            writer = csv.writer(file)
            writer.writerows(inventory)
        print("Inventory exported successfully")
    except Exception as e:
        print(f"Error exporting inventory: {e}")