import os
import re
import sqlite3
import hashlib
import database
from datetime import datetime


class Trainer:

    def __init__(self, username : str, password : str, firstName : str, lastName : str, registrationDate : datetime = datetime.now()):
        self.username : str = username
        self.password : str = password
        self.firstName : str = firstName
        self.lastName : str = lastName
        self.registrationDate : datetime = registrationDate
        self.role : str = "Trainer"

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

    def update_password():
        while True:
            print("[!] Changing password.")
            new_password = input("[+] Enter your new password:")
            if Trainer.is_valid_password(new_password):
                # Hash the password
                hashed_password = hashlib.sha256(
                    new_password.encode()).hexdigest()

                # Update the password in the database for the logged-in user
                cursor.execute(
                    "UPDATE Trainers SET password = ? WHERE username = ?",
                    (hashed_password, logged_in_user))
                connection.commit()

                print("[!] Password changed successfully.")
                input("Press any key to continue.")
                break
            else:
                print(
                    "[!] Invalid password format. Password must contain at least one uppercase letter, one lowercase letter, one digit, one special character, and be 12-30 characters long."
                )

    def modify_member():
        # Implement the logic to modify a member's information
        Trainer.search_member()
        print("[!] Selecting member.")
        search_key = input("[+] Choose a member by ID:")
        #TODO: ADD CHECKS TO SEE IF KEY IS NUMBER


        while True:
            print(f"\n[1] Edit firstname: '{mem.givenName}'")
            print(f"[2] Edit surname: '{mem.surname}'")
            print(f"[3] Edit age: '{mem.surname}'")
            print(f"[4] Edit gender: '{mem.surname}'")
            print(f"[5] Edit weight: '{mem.surname}'")
            print(f"[6] Edit address: '{mem.streetAddress}'")
            print(f"[7] Edit email address: '{mem.zipcode}'")
            print(f"[8] Edit phone number: '{mem.city}'")
            print(f"[9] Go back.")
            inp = input("\n[?] Option: ")

            if inp == "1":
                print(f"\n[+] Current value: {mem.givenName}")
                mem.givenName = input("[+] New value: ")
            elif inp == "2":
                print(f"[+] Current value: {mem.surname}")
                mem.surname = input("[+] New value: ")
                break
            elif inp == "3":
                print(f"[+] Current value: {mem.streetAddress}")
                mem.streetAddress = input("[+] New value: ")
                break
            elif inp == "4":
                print(f"[+] Current value: {mem.zipcode}")
                mem.zipcode = input("[+] New value: ")
                break
            elif inp == "5":
                print(f"[+] Current value: {mem.city}")
                mem.city = input("[+] New value: ")
                break
            elif inp == "6":
                print(f"[+] Current value: {mem.emailAddress}")
                mem.emailAddress = input("[+] New value: ")
                break
            elif inp == "7":
                print(f"[+] Current value: {mem.username}")
                username = input("[+] New value: ")
                for mem in Member.get_Members():
                    if username == mem.username:
                        input(
                            "[!] A username with the same name was found, please pick a different username."
                        )
                        break
                else:
                    mem.username = username
            elif inp == "8":
                print(f"[+] Current value: {mem.password}")
                mem.password = input("[+] New value: ")
                break
            elif inp == "9":
                print(f"[+] Current value: {mem.phoneNumber}")
                mem.phoneNumber = input("[+] New value: ")
                break
            elif inp == "10":
                return
            else:
                continue
        print("\n[!] Member value was successfully changed!")
        return input("[!] Press 'Enter' to continue.")

    def search_member():
        print("[!] Searching member.")
        search_key = input("[+] Search for member:")
        database.database.get_members(search_key)

    def adding_member():
        print("[!] Adding member.")
        first_name = input("[+] Enter first name:")
        last_name = input("[+] Enter first name:")
        age = input("[+] Enter age (number):")
        gender = input("[+] Enter first name:")
        weight = input("[+] Enter weight (kg):")
        address = input("[+] Enter address:")
        email = input("[+] Enter email address:")
        phone = input("[+] Enter phone number:")

        database.database.add_member(first_name, last_name, age, gender, weight, address, email, phone)   

