# The authentication file to allow for password access

import sqlite3

def initialise_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Create users table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialise_db()
    print("Database initialised.")