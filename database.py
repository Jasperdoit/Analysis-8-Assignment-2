import member
import sqlite3
from passwordmanager import passwordmanager
from typing import Optional

class database:
    def get_member(keyword : str) -> Optional[member.Member]:
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

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

        keyword = f"%{keyword}%"

        cursor.execute(query, (keyword, keyword, keyword, keyword, keyword, keyword))
        result = cursor.fetchone()
        if result is None:
            return None
        else:
            return member.Member(result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])
        
    
    def get_member_by_keyword(keyword : str) -> tuple:
        """returns a tuple of the systemadmin's data if found, None otherwise."""
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Query to search for a member based on various fields
        query = """
            SELECT * FROM Members
            WHERE username LIKE ? OR
                first_name LIKE ? OR
                last_name LIKE ? OR
                address LIKE ? OR
                email LIKE ? OR
                registration_date LIKE ?
        """

        keyword = f"%{keyword}%"

        cursor.execute(query, (keyword, keyword, keyword, keyword, keyword, keyword))
        result = cursor.fetchone()
        if result is None:
            return None
        else:
            return result


    def add_member(first_name, last_name, age, gender, weight,
                    address, email, phone):
            # Connect to the SQLite database
            conn = sqlite3.connect("fitplus.db")
            cursor = conn.cursor()

            # Insert the member data into the Members table
            cursor.execute(
                """
                INSERT INTO Members (first_name, last_name, age, gender, weight, address, email, phone)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (first_name, last_name, age, gender, weight, address,
                email, phone))

            # Commit the changes and close the connection
            conn.commit()
    
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
            WHERE role = "super_admin"
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
            INSERT INTO systemadmin (username, password_hash, first_name, last_name, registration_date, role)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (admin[0], admin[1], admin[2], admin[3], admin[4], admin[5]))

        # Commit the changes and close the connection
        conn.commit()

        

    def delete_member(memberid : str):
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
                registration_date LIKE ? OR
                role LIKE ?
        """

        keyword = f"%{keyword}%"

        cursor.execute(query, (keyword, keyword, keyword, keyword, keyword))
        result = cursor.fetchone()
        if result is None:
            return None
        else:
            return result

    def add_trainer(trainer : tuple):
        """adds a trainer to the database. Make sure all proper checks are done before calling this function."""
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Insert the member data into the Members table
        cursor.execute(
            """
            INSERT INTO Trainers (username, password_hash, first_name, last_name, registration_date, role)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (trainer[0], trainer[1], trainer[2], trainer[3], trainer[4], trainer[5]))

        # Commit the changes and close the connection
        conn.commit()

    def update_trainer(username : str, trainer : tuple):
        """updates the information of a trainer in the database based on their username. Make sure all proper checks are done before calling this function."""
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Insert the member data into the Members table
        cursor.execute(
            """
            UPDATE Trainers SET username = ?, password_hash = ?, first_name = ?, last_name = ?, registration_date = ?, role = ?
            WHERE username = ?
        """, (trainer[0], trainer[1], trainer[2], trainer[3], trainer[4], trainer[5], username))

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
                registration_date LIKE ? OR
                role LIKE ?
        """

        keyword = f"%{keyword}%"

        cursor.execute(query, (keyword, keyword, keyword, keyword, keyword))
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
            UPDATE systemadmin SET username = ?, password_hash = ?, first_name = ?, last_name = ?, registration_date = ?, role = ?
            WHERE username = ?
        """, (systemadmin[0], systemadmin[1], systemadmin[2], systemadmin[3], systemadmin[4], systemadmin[5], username))

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

    import sqlite3

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











