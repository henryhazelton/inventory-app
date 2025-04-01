import unittest
import sqlite3
import tempfile
import bcrypt
from unittest.mock import patch
import os

import login
import user_registration
import addToInventory
import removeFromInventory
import editInventory
import viewInventory
import main

class TestLogin(unittest.TestCase):
    def setUp(self):
        # Create a temporary database for testing
        self.temp_db = tempfile.NamedTemporaryFile(delete=False).name
        self.conn = sqlite3.connect(self.temp_db)
        self.cursor = self.conn.cursor()
        
        # Create users table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password BLOB NOT NULL
        )
        ''')
        
        # Add a test user
        hashed_password = bcrypt.hashpw("testpass".encode(), bcrypt.gensalt())
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                           ("testuser", hashed_password))
        self.conn.commit()
        
        # Patch the database connection in login module
        self.db_patcher = patch('login.sqlite3.connect')
        self.mock_connect = self.db_patcher.start()
        self.mock_connect.return_value = self.conn

    def tearDown(self):
        self.db_patcher.stop()
        self.conn.close()
        os.unlink(self.temp_db)
        
    @patch('builtins.input', side_effect=["testuser", "testpass"])
    def test_successful_login(self, mock_input):
        self.assertTrue(login.login_user())
        
    @patch('builtins.input', side_effect=["testuser", "wrongpass"])
    def test_failed_login_wrong_password(self, mock_input):
        self.assertFalse(login.login_user())
        
    @patch('builtins.input', side_effect=["nonexistentuser", "testpass"])
    def test_failed_login_no_user(self, mock_input):
        self.assertFalse(login.login_user())

class TestMain(unittest.TestCase):
    