import member
import sqlite3
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
        
    def get_members(keyword : str) -> Optional[list]:
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
        result = cursor.fetchall()
        if result is None or len(result) == 0:
            input("[!] No members found.")
        else:
            for i in range(len(result)):
                print(result)
            input("[!] Press 'Enter' to continue.")
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
            SELECT * FROM SystemAdmins
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
    def add_admin(admin) -> None:
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        # Insert the member data into the Members table
        cursor.execute(
            """
            INSERT INTO systemadmin (username, password_hash, first_name, last_name, registration_date, role)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (admin.username, admin.password, admin.firstName, admin.lastName, admin.registrationDate, admin.role))

        # Commit the changes and close the connection
        conn.commit()

        

    def delete_member():
        print("[!] Deleting member.")
        memberid = input("[+] Enter member ID:")

        # Connect to the database
        conn = sqlite3.connect("fitplus.db")
        cursor = conn.cursor()

        try:
            # Execute the deletion query
            cursor.execute("DELETE FROM Members WHERE member_id = ?", (memberid,))
            conn.commit()
            input("Member deleted successfully.")
        except sqlite3.Error as e:
            input(f"Error deleting member: {e}")
        finally:
            # Close the database connection
            conn.close()        







