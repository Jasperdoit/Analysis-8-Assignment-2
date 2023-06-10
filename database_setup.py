import sqlite3
from datetime import datetime

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
                first_name TEXT,
                last_name TEXT,
                registration_date TIMESTAMP NOT NULL,
                role TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Trainers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                role TEXT NOT NULL
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
                address TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


        
        # cursor.execute("""
        #     INSERT INTO Trainers (username, password_hash, first_name, last_name, registration_date ,role)
        #     VALUES (?, ?, ?, ?, ?, ?)
        # """, ("testtest1", "Password123!", "JOHN",
        #     "DOE", datetime.now(),"role"))


        # Commit the changes and close the connection
        conn.commit()

    def setup_superadmin(username, password) -> None:
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Check if the username already exists in the system_admin table
        cursor.execute("SELECT * FROM systemadmin WHERE username = ?", (username,))
        result = cursor.fetchone()

        if result is None:
            cursor.execute("""
                INSERT INTO systemadmin (username, password_hash, registration_date)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (username, password, datetime.date, ))
            conn.commit()
        conn.close()
