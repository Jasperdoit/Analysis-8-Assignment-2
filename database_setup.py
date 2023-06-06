import sqlite3

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
            role TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Trainers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
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


    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Call the setup_database function
setup_database()
