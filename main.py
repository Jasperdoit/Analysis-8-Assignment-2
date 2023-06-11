import os
import sys
import sqlite3
import hashlib
import re
import random
import database as db

from backup import Backup
from trainer import Trainer as tr
from systemadmin import SystemAdmin
from superadmin import SuperAdmin
from string import ascii_letters, digits, punctuation
from database_setup import setup_database


def get_user_role(username):
    cursor.execute("SELECT role FROM systemadmin WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

    # Checks if the password is correct and uses allowed characters.


def is_valid_password(password):
    # Regex pattern to validate password
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,30}$'
    return re.match(pattern, password) is not None


# Hashes the password of the user.
def hash_password(password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return password_hash


# Checks for valid username.
def is_valid_username(username):
    # Regex pattern to validate username
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]{7,11}$'
    return re.match(pattern, username) is not None


def username_exists(username):
    cursor.execute("SELECT COUNT(*) FROM systemadmin WHERE username = ?", (username,))
    count = cursor.fetchone()[0]
    return count > 0


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


def Login():
    print("[!] Log in to Fitplus.")
    username = input("[+] Enter your username: ")
    clearConsole()
    if not validate_username(username):
        menuOptions = {"1": Login, "2": ShowMenu}
        print("[!] Sorry this is not right please try again.")
        print("[1] Try again.")
        print("[2] Go back.")
        showMenuOptions(menuOptions, Login)

    password = input("[+] Enter your password: ")
    clearConsole()
    if not validate_password(password, username):
        menuOptions = {"1": Login, "2": ShowMenu}
        print("[!] Sorry this is not right please try again.")
        print("[1] Try again.")
        print("[2] Go back.")
        showMenuOptions(menuOptions, Login)

    role = get_user_role(username)

    # Proceed with the appropriate actions based on the user's role
    if role == "trainer":
        showTrainerMenu()
    elif role == "system_admin":
        showSystemAdminMenu()
    elif role == "superadmin":
        showSuperAdminMenu()
    else:
        DisplayError("Invalid user role.")


def validate_username(username):
    if not is_valid_username(username):
        return False
    if not username_exists(username):
        return False
    return True


def validate_password(password, username):
    cursor.execute("SELECT password_hash FROM systemadmin WHERE username = ?", (username,))
    result = cursor.fetchone()
    if hash_password(password) == result:
        return False
    return True


def DisplayError(error):
    print(f"ERROR: {error}")


def ShowMenu():
    menuOptions = {"1": Login, "2": Exit}
    clearConsole()

    print("[!] Welcome to Fitplus!")
    print("[+] Please Choose an option.")
    print("[1] Log in")
    print("[2] Exit")
    showMenuOptions(menuOptions, ShowMenu)


def showMenuOptions(menuOptions, func):
    try:
        userInput = input("[?] Option: ")
        assert 0 < int(userInput) <= len(menuOptions)
        clearConsole()
        menuOptions[userInput]()
    except Exception as e:
        customError(func, e)
    clearConsole()

    return func()


def customError(func, e):
    clearConsole()
    print("[!] Invalid input, please try again.")
    print('An exception occurred: {}'.format(e))
    input("show error 1")


def Exit():
    sys.exit()


def showTrainerMenu():
    trainerOptions = {"1": tr.update_password, "2": tr.adding_member, "3": tr.modify_member, "4": tr.search_member,
                      "5": Login}
    print("[!] This is the trainer menu.")
    print("[+] Please Choose an option.")
    print("[1] Update password.")
    print("[2] Add member.")
    print("[3] Modify member.")
    print("[4] Search member.")
    print("[5] Back.")
    showMenuOptions(trainerOptions, showTrainerMenu)

def showSystemAdminMenu():
    systemAdminOptions = {"1": tr.update_password, "2": tr.add_member, "3": tr.modify_member, "4": tr.search_member,
                          "5": Login, "7": Backup.create_backup, "8": Backup.restore_backup(), "12": db.delete_member}
    print("[!] This is the system admin menu.")
    print("[+] Please choose an option.")
    print("[1] Update password.")
    print("[2] Check users.")
    print("[3] Add trainers.")
    print("[4] Modify trainers.")
    print("[5] Delete trainers.")
    print("[6] Reset trainer password.")
    print("[7] Make backup.")
    print("[8] Restore backup.")
    print("[9] See logs.")
    print("[10] Add member.")
    print("[11] Modify members.")
    print("[12] Delete member record.")
    print("[13] Search member.")
    showMenuOptions(systemAdminOptions, showTrainerMenu)

def showSuperAdminMenu():
    superAdminOptions = {"1": tr.update_password, "2": tr.add_member, "3": tr.modify_member, "4": tr.search_member,
                         "5": Login, "10": Backup.create_backup, "11": Backup.restore_backup(), "15": db.delete_member}
    print("[!] This is the super admin menu.")
    print("[+] Please choose an option.")
    print("[1] Check users.")
    print("[2] Add trainers.")
    print("[3] Modify trainers.")
    print("[4] Delete trainers.")
    print("[5] Reset trainer password.")
    print("[6] Add admin.")
    print("[7] Modify admin.")
    print("[8] Delete admin.")
    print("[9] Reset admin password.")
    print("[10] Make backup.")
    print("[11] Restore backup.")
    print("[12] See logs.")
    print("[13] Add member.")
    print("[14] Modify member.")
    print("[15] Delete member record.")
    print("[16] Search member.")
    showMenuOptions(superAdminOptions, showTrainerMenu)


def add_test_trainer():
    username = "testtest1"
    password = "test"
    password_hash = hash_password(password)
    role = "trainer"

    cursor.execute("INSERT INTO systemadmin (username, password_hash, role) VALUES (?, ?, ?)",
                   (username, password_hash, role))
    conn.commit()
    print("Test trainer added successfully.")


def add_test_member():
    # Connect to the database
    conn = sqlite3.connect("fitplus.db")
    cursor = conn.cursor()

    try:
        # Insert a test member
        cursor.execute("""
            INSERT INTO Members (member_id, first_name, last_name, age, gender, weight, address, email, phone)
            VALUES ('001', 'John', 'Doe', 25, 'Male', 70.5, '123 Street', 'john@example.com', '123456789')
        """)
        conn.commit()
        print("Test member added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding test member: {e}")
    finally:
        # Close the database connection
        conn.close()


if __name__ == "__main__":
    if not os.path.exists('./logs'):
        os.mkdir('./logs')
    if not os.path.exists('./backup'):
        os.mkdir('./backup')

    conn = sqlite3.connect("fitplus.db")
    cursor = conn.cursor()
    setup_database()
    # add_test_trainer()
    add_test_member()
    # Backup.create_backup()
    # Backup.restore_backup()
    ShowMenu()
