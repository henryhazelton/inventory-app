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
        print("3. Edit item")
        print("4. View inventory")
        print("5. Exit")

        # add a choice variable to allow the user to enter their choice
        choice = input("Enter your choice: ")
        print(f"You have picked option: {choice}")


if __name__ == "__main__":
    main()