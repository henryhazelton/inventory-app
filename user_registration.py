# Allows the user to create a password

import sqlite3
import bcrypt

def register_user():
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # Insert new user into database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print("User registered successfully!")

    except sqlite3.IntegrityError:
        print("Username already exists! Try a different one.")
    
    finally:
        conn.close()

if __name__ == "__main__":
    register_user()