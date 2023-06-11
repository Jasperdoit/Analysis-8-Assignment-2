import member
import sqlite3
from passwordmanager import passwordmanager
from typing import Optional
from encryption import Encryption

class database:
    def print_member(keyword : str):
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Query to search for a member based on various fields
        query = """
            SELECT * FROM Members
            WHERE member_id LIKE ? OR
                first_name LIKE ? OR
                last_name LIKE ? OR
                zipcode LIKE ? OR
                streetname LIKE ? OR
                email LIKE ?
        """

        keyword = f"%{keyword}%"

        cursor.execute(query, (keyword, keyword, keyword, keyword, keyword, keyword,))
        result = cursor.fetchone()
        if result is None:
            return None
        else:
            print(result)
            return
        
    import sqlite3

    def get_member_by_memberID(keyword: str):
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Retrieve the member from the Members table based on the member ID
        cursor.execute("SELECT * FROM Members WHERE member_id = ?", (keyword,))
        member = cursor.fetchone()

        if member is None:
            return None
        else:
            return member
    
    def get_member_by_keyword(keyword : str) -> tuple:
        """returns a tuple of the systemadmin's data if found, None otherwise."""
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Query to search for a member based on various fields
        query = """
            SELECT * FROM Members
            WHERE member_id LIKE ? OR
                first_name LIKE ? OR
                last_name LIKE ? OR
                zipcode LIKE ? OR
                streetname LIKE ? OR
                email LIKE ?
        """

        keyword = f"%{keyword}%"

        cursor.execute(query, (keyword, keyword, keyword, keyword, keyword, keyword,))
        result = cursor.fetchone()
        if result is None:
            return None
        else:
            return result


    def add_member(memberid, first_name, last_name, age, gender, weight,
                    streetname, zipcode, housenumber, city, email, phone,):
            # Connect to the SQLite database
            conn = sqlite3.connect("fitplus.db")
            cursor = conn.cursor()

            encryption = Encryption()

            first_name = encryption.encrypt(first_name)
            last_name = encryption.encrypt(last_name)
            age = encryption.encrypt(age)
            gender = encryption.encrypt(gender)
            weight = encryption.encrypt(weight)
            streetname = encryption.encrypt(streetname)
            zipcode = encryption.encrypt(zipcode)
            housenumber = encryption.encrypt(housenumber)
            city = encryption.encrypt(city)
            email = encryption.encrypt(email)
            phone = encryption.encrypt(phone)

            # Insert the member data into the Members table
            cursor.execute(
                """
                INSERT INTO Members (member_id, first_name, last_name, age, gender, weight, streetname, zipcode, housenumber, city, email, phone)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (memberid, first_name, last_name, age, gender, weight, streetname, zipcode, housenumber, city,
                email, phone,))

            # Commit the changes and close the connection
            conn.commit()

    def delete_member(memberid):
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Delete the member based on the entire row data
        cursor.execute("""
            DELETE FROM Members
            WHERE member_id = ?
        """, (memberid,))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
    
    def get_all_trainers() -> Optional[list]:
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Query to search for a member based on various fields
        query = """
            SELECT * FROM Trainers
        """

        cursor.execute(query)
        result = cursor.fetchall()
        if result is None or len(result) == 0:
            return None
        else:
            return result
    def get_all_systemadmins() -> Optional[list]:
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Query to search for a member based on various fields
        query = """
            SELECT * FROM systemadmin
        """

        cursor.execute(query)
        result = cursor.fetchall()
        if result is None or len(result) == 0:
            return None
        else:
            return result
        
    def get_superadmin():
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Query to search for a member based on various fields
        query = """
            SELECT * FROM systemadmin
            WHERE username = "super_admin"
        """

        cursor.execute(query)
        result = cursor.fetchone()
        if result is None:
            return None
        else:
            return result
    def add_admin(admin : tuple) -> None:
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Insert the member data into the Members table
        cursor.execute(
            """
            INSERT INTO systemadmin (username, password_hash, first_name, last_name, registration_date)
            VALUES (?, ?, ?, ?, ?)
        """, (admin[0], admin[1], admin[2], admin[3], admin[4],))

        # Commit the changes and close the connection
        conn.commit()

        

    def delete_member(memberid : str) -> None:
        # Connect to the database
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Insert the member data into the Members table
        cursor.execute(
            """
            DELETE FROM members WHERE member_id = ?
        """, (memberid,))

        # Commit the changes and close the connection
        conn.commit()

    def update_city(value, member) -> None:
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Insert the member data into the Members table
        cursor.execute(
            """
            UPDATE members SET city = ? WHERE member_id = ?
            """, (value, member[1],))


        # Commit the changes and close the connection
        conn.commit()

    def update_member(value, argument, member)-> None:
        # Connect to the database
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Insert the member data into the Members table
        cursor.execute(
            """
            UPDATE members SET {} = ? WHERE member_id = ?
            """.format(argument), (value, member[1],))


        # Commit the changes and close the connection
        conn.commit()


    def username_exists(username : str) -> bool:
        """returns True if the username exists, False otherwise."""
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Query to search for a member based on various fields
        query = """
            SELECT * FROM systemadmin
            WHERE username = ?
        """

        cursor.execute(query, (username,))
        result = cursor.fetchone()
        if not result is None:
            return True

        query = """
            SELECT * FROM Trainers
            WHERE username = ?
        """

        cursor.execute(query, (username,))
        result = cursor.fetchone()
        if not result is None:
            return True
        return False
    
    def get_trainer_by_username(username : str)-> tuple:

        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        query = """
            SELECT * FROM Trainers WHERE username = ?
        """
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        conn.close()

        if result is None:
            return None
        else:
            return result
        

    def get_admin_by_username(username : str)-> tuple:

        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        query = """
            SELECT * FROM systemadmin WHERE username = ?
        """
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        conn.close()

        if result is None:
            return None
        else:
            return result

    
    def get_trainer_by_keyword(keyword : str) -> tuple:
        """returns a tuple of the trainer's data if found, None otherwise."""
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Query to search for a member based on various fields
        query = """
            SELECT * FROM Trainers
            WHERE username LIKE ? OR
                first_name LIKE ? OR
                last_name LIKE ? OR
                registration_date LIKE ?
        """

        keyword = f"%{keyword}%"

        cursor.execute(query, (keyword, keyword, keyword, keyword,))
        result = cursor.fetchone()
        if result is None:
            return None
        else:
            return result

    def add_trainer(trainer : tuple):
        """adds a trainer to the database. Make sure all proper checks are done before calling this function."""
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        encryption = Encryption()

        # Insert the member data into the Members table
        cursor.execute(
            """
            INSERT INTO Trainers (username, password_hash, first_name, last_name, registration_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (encryption.encrypt(trainer[0]), encryption.encrypt(trainer[1]), encryption.encrypt(trainer[2]), encryption.encrypt(trainer[3]), encryption.encrypt(trainer[4]),))

        # Commit the changes and close the connection
        conn.commit()

    def update_trainer(username : str, trainer : tuple):
        """updates the information of a trainer in the database based on their username. Make sure all proper checks are done before calling this function."""
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Insert the member data into the Members table
        cursor.execute(
            """
            UPDATE Trainers SET username = ?, password_hash = ?, first_name = ?, last_name = ?, registration_date = ?
            WHERE username = ?
        """, (trainer[0], trainer[1], trainer[2], trainer[3], trainer[4], username,))

        # Commit the changes and close the connection
        conn.commit()

    def delete_trainer(username : str):
        """Deletes a trainer from the database based on their username."""
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Insert the member data into the Members table
        cursor.execute(
            """
            DELETE FROM Trainers WHERE username = ?
        """, (username,))

        # Commit the changes and close the connection
        conn.commit()

    def get_systemadmin_by_keyword(keyword : str) -> tuple:
        """returns a tuple of the systemadmin's data if found, None otherwise."""
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Query to search for a member based on various fields
        query = """
            SELECT * FROM systemadmin
            WHERE username LIKE ? OR
                first_name LIKE ? OR
                last_name LIKE ? OR
                registration_date LIKE ?
        """

        keyword = f"%{keyword}%"

        cursor.execute(query, (keyword, keyword, keyword, keyword,))
        result = cursor.fetchone()
        if result is None:
            return None
        else:
            if result[5] == "superadmin":
                return None
            return result

    def update_systemadmin(username : str, systemadmin : tuple):
        """Updates the information of a systemadmin in the database based on their username. Make sure all proper checks are done before calling this function."""
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Insert the member data into the Members table
        cursor.execute(
            """
            UPDATE systemadmin SET username = ?, password_hash = ?, first_name = ?, last_name = ?, registration_date = ?
            WHERE username = ?
        """, (systemadmin[0], systemadmin[1], systemadmin[2], systemadmin[3], systemadmin[4], username,))

        # Commit the changes and close the connection
        conn.commit()
    
    def delete_systemadmin(username : str):
        """Deletes a systemadmin from the database based on their username."""
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Insert the member data into the Members table
        cursor.execute(
            """
            DELETE FROM systemadmin WHERE username = ?
        """, (username,))

        # Commit the changes and close the connection
        conn.commit()

    # def get_all_users():
    #     conn = sqlite3.connect("fitplus.db")
    #     cursor = conn.cursor()

    #     # Query to retrieve all users from three tables
    #     query = """
    #         SELECT username FROM Trainers
    #         UNION
    #         SELECT username FROM systemadmin
    #     """

    #     cursor.execute(query)
    #     result = cursor.fetchall()

    #     # Close the connection
    #     conn.close()

    #     return result

    def get_user_role(username):
        if username == "super_admin":
            return username


        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Query to check the table name for a given username
        query = """
            SELECT 'trainer' AS table_name FROM Trainers WHERE username = ?
            UNION
            SELECT 'system_admin' AS table_name FROM systemadmin WHERE username = ?
        """

        cursor.execute(query, (username, username,))
        result = cursor.fetchone()

        # Close the connection
        conn.close()

        if result:
            return result[0]  # Return the table name
        else:
            return None  # Username not found in any table
        
    def check_password(username, password):
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Query to retrieve the password hash for the given username
        query = """
            SELECT password_hash FROM Trainers WHERE username = ?
            UNION
            SELECT password_hash FROM systemadmin WHERE username = ?
        """
        cursor.execute(query, (username, username,))
        result = cursor.fetchone()

        # Close the connection
        conn.close()

        if result is not None:
            # Compare the stored password hash with the provided password
            stored_password_hash = result[0]
            if stored_password_hash == passwordmanager.encrypt(password):
                return True

        return False











