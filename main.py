# main.py

import inventory
import addToInventory
import editInventory
import removeFromInventory
import viewInventory

def main():
    while True:
        print("1. Add new item")
        print("2. Remove item")
        print("3. Edit item quantity")
        print("4. View inventory")
        print("5. Exit")

        # add a choice variable to allow the user to enter their choice
        choice = input("Enter your choice: ")
        print(f"You have picked option: {choice}")

        if choice == '1':
            addToInventory.add_item()
        elif choice == '2':
            removeFromInventory.remove_item()
        elif choice == '3':
            editInventory.edit_item()
        elif choice == '4':
            viewInventory.view_inventory()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again")



if __name__ == "__main__":
    main()