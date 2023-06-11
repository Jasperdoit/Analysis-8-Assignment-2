import sqlite3

from logger import LogMessage
from datetime import datetime
from passwordmanager import passwordmanager

class database_setup:
    def setup_database():
        # Connect to the SQLite database
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Create tables for users, trainers, and members
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS systemadmin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                first_name TEXT NULL,
                last_name TEXT NULL,
                registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Trainers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id TEXT UNIQUE NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                age TEXT NOT NULL,
                gender TEXT NOT NULL,
                weight REAL NOT NULL,
                streetname TEXT NOT NULL,
                housenumber TEXT NOT NULL,
                zipcode TEXT NOT NULL,
                city TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Commit the changes and close the connection
        conn.commit()


    def setup_superadmin(username, password):
        newpass = passwordmanager.encrypt(password)
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Check if the username already exists in the system_admin table
        cursor.execute("SELECT * FROM systemadmin WHERE username = ?", (username,))
        result = cursor.fetchone()

        if result is None:
            cursor.execute("""
                INSERT INTO systemadmin (username, password_hash, registration_date)
                VALUES (?, ?, ?)
            """, (username, newpass, datetime.now()))
            conn.commit()
        conn.close()

        # LogMessage()\
        #     .set_username(username)\
        #     .set_activity("New admin user is created.")\
        #     .set_info(f"Created with username: {username}")\
        #     .set_not_suspicious()\
        #     .create_log()
