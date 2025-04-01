# Allows the user to login to the app

import sqlite3
import bcrypt

def login_user():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Retrieve stored hash for the given username
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result:
        stored_hash = result[0]

        # Verify the entered password against the stored hash
        if bcrypt.checkpw(password.encode(), stored_hash):
            print("Login successful, welcome, " + username)
            return True
        else:
            print("invalid password")
    else:
        print("user not found")

    conn.close()
    return False

if __name__ == "__main__":
    login_user()