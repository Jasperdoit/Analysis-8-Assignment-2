import os
import re
import sqlite3
import hashlib
from database import database as db
from datetime import datetime


class Trainer:

    def __init__(self, username : str, password : str, firstName : str, lastName : str, registrationDate : datetime = datetime.now()):
        self.username : str = username
        self.password : str = password
        self.firstName : str = firstName
        self.lastName : str = lastName
        self.registrationDate : datetime = registrationDate
        self.role : str = "trainer"

    def set_first_name(self, firstName : str):
        self.firstName = firstName

    def set_last_name(self, lastName : str):
        self.lastName = lastName

    def set_registration_date(self, registrationDate : datetime):
        self.registrationDate = registrationDate

        # Checks if the password is correct and uses allowed characters.
    def is_valid_password(password):
        # Regex pattern to validate password
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,30}$'
        return re.match(pattern, password) is not None
    
    
        # Checks for valid username.
    def is_valid_username(username):
        # Regex pattern to validate username
        pattern = r'^[a-zA-Z_][a-zA-Z0-9_]{7,11}$'
        return re.match(pattern, username) is not None
    
    def is_valid_gender(gender):
        # List of valid gender options
        valid_genders = ['M', 'F']
        return gender.lower() in valid_genders

    def is_valid_number(value):
        try:
            float(value)
            return True
        except ValueError:
            return False


    def update_password():
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()
        while True:
            print("[!] Changing password.")
            new_password = input("[+] Enter your new password:")
            if Trainer.is_valid_password(new_password):
                # Hash the password
                hashed_password = hashlib.sha256(
                    new_password.encode()).hexdigest()

                # Update the password in the database for the logged-in user
                cursor.execute(
                    "UPDATE Trainers SET password_hash = ? WHERE username = ?",
                    (hashed_password, "testtest1"))
                conn.commit()

                print("[!] Password changed successfully.")
                input("Press 'Enter' to continue.")
                break
            else:
                print(
                    "[!] Invalid password format. Password must contain at least one uppercase letter, one lowercase letter, one digit, one special character, and be 12-30 characters long."
                )

    def modify_member():
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()
        # Implement the logic to modify a member's information
        Trainer.search_member()
        print("[!] Selecting member.")

        while True:
            search_key = input("[+] Choose a member by ID:")
            if Trainer.is_valid_number(search_key) == False:
                input("[!] Not a valid ID. Try again.")
            else:
                break


        while True:
            print(f"[1] Edit firstname.")
            print(f"[2] Edit surname.'")
            print(f"[3] Edit age.")
            print(f"[4] Edit gender.")
            print(f"[5] Edit weight.")
            print(f"[6] Edit address.")
            print(f"[7] Edit email address.")
            print(f"[8] Edit phone number.")
            print(f"[9] Go back.")
            inp = input("\n[?] Option: ")

            if inp == "1":
                value = input("[+] New value: ")
                query = f"UPDATE Members SET first_name = ? WHERE id = {search_key}"
                cursor.execute(query, (value))
                break
            elif inp == "2":
                value = input("[+] New value: ")
                query = f"UPDATE Members SET last_name = ? WHERE id = {search_key}"
                cursor.execute(query, (value))
                break
            elif inp == "3":
                value = input("[+] New value: ")
                query = f"UPDATE Members SET age = ? WHERE id = {search_key}"
                cursor.execute(query, (value))
                break
            elif inp == "4":
                value = input("[+] New value: ")
                query = f"UPDATE Members SET gender = ? WHERE id = {search_key}"
                cursor.execute(query, (value))
                break
            elif inp == "5":
                value = input("[+] New value: ")
                query = f"UPDATE Members SET weight = ? WHERE id = {search_key}"
                cursor.execute(query, (value))
                break
            elif inp == "6":
                value = input("[+] New value: ")
                query = f"UPDATE Members SET address = ? WHERE id = {search_key}"
                cursor.execute(query, (value))
                break
            elif inp == "7":
                value = input("[+] New value: ")
                query = f"UPDATE Members SET email = ? WHERE id = {search_key}"
                cursor.execute(query, (value))
            elif inp == "8":
                value = input("[+] New value: ")
                query = f"UPDATE Members SET phone = ? WHERE id = {search_key}"
                cursor.execute(query, (value))
            elif inp == "9":
                return
            else:
                continue
        conn.commit()
        print("\n[!] Member value was successfully changed!")
        input("[!] Press 'Enter' to continue.")

    def search_member():
        print("[!] Searching member.")
        search_key = input("[+] Search for member:")
        db.get_members(search_key)

    def adding_member():
        print("[!] Adding member.")
        first_name = input("[+] Enter first name:")
        last_name = input("[+] Enter last name:")

        while True:
            age = input("[+] Enter age (number):")
            if Trainer.is_valid_number(age) == False:
                input("[!] Not a valid number")
            else:
                break
        
        while True:
            gender = input("[+] Enter gender:")
            if Trainer.is_valid_gender(gender) == False:
                input("[!] Not a gender. Enter 'M' or 'F'")
            else: 
                break

        while True:
            weight = input("[+] Enter weight (kg):")
            if Trainer.is_valid_number(weight) == False:
                input("[!] Not a valid number")
            else:
                break

        address = input("[+] Enter address:")
        email = input("[+] Enter email address:")
        phone = input("[+] Enter phone number:")

        db.add_member(first_name, last_name, age, gender, weight, address, email, phone)   
    
    def to_tuple(self):
        return (self.username, self.password, self.firstName, self.lastName, self.registrationDate, self.role)
    
    def from_tuple(tuple) -> 'Trainer':
        trainer = Trainer(tuple[1], tuple[2], tuple[3], tuple[4], tuple[5])
        trainer.id = tuple[0]
        return trainer

