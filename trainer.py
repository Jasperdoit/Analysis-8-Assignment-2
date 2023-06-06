import os
import re
import sqlite3
import hashlib


class Trainer:

    def __init__(self, username, options):
        self.username = username
        self.options = options

        # Checks if the password is correct and uses allowed characters.
    def is_valid_password(password):
        # Regex pattern to validate password
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,30}$'
        return re.match(pattern, password) is not None

    def update_password():
        while True:
            print("[!] Changing password.")
            new_password = input("[+] Enter your new password:")
            if is_valid_password(new_password):
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

    def add_member(self, member_id, first_name, last_name, age, gender, weight,
                   address, email, phone):
        # Connect to the SQLite database
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Insert the member data into the Members table
        cursor.execute(
            """
            INSERT INTO Members (member_id, first_name, last_name, age, gender, weight, address, email, phone, registration_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (member_id, first_name, last_name, age, gender, weight, address,
              email, phone, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        # Commit the changes and close the connection
        conn.commit()

    def modify_member():
        # Implement the logic to modify a member's information
        search_member()

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
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()
        print("[!] Searching member.")
        search_key = input("[+] Search for member:")

        # Query to search for a member based on various fields
        query = """
            SELECT * FROM Members
            WHERE id LIKE ? OR
                  first_name LIKE ? OR
                  last_name LIKE ? OR
                  address LIKE ? OR
                  email LIKE ? OR
                  phone LIKE ?
        """

        # Prepare the search key with wildcard characters for partial matching
        search_key = '%' + search_key + '%'

        # Execute the query with the search key for each field
        cursor.execute(query, (search_key, search_key, search_key, search_key,
                               search_key, search_key))
        result = cursor.fetchall()

        if result:
            print("Search results:")
            # Process the search results as needed
            for row in result:
                print(row)  # Example: Print the member details
        else:
            print("No matching members found.")

        input("Press any key to continue.")
