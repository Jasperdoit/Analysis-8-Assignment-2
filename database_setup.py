import sqlite3
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
                registration_date TIMESTAMP NOT NULL
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
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                weight REAL NOT NULL,
                streetname TEXT NOT NULL,
                housenumber INTEGER NOT NULL,
                zipcode TEXT NOT NULL,
                city TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Commit the changes and close the connection
        conn.commit()



    def create_test_trainer():
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        password = "Test123456789!"

        # Username doesn't exist, insert the test trainer into the Trainers table
        hashed_password = passwordmanager.encrypt(password)
        registration_date = datetime.now()

        cursor.execute("""
            INSERT INTO Trainers (username, password_hash, first_name, last_name, registration_date)
            VALUES (?, ?, ?, ?, ?)
        """, ("super_train1", hashed_password, "John", "Doe", registration_date))
        conn.commit()
        conn.close()


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
