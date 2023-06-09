import member
import sqlite3
from typing import Optional
class database:
    def get_member(keyword : str) -> Optional[member.Member]:
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
            return None
        else:
            for i in range(len(result)):
                result[i] = member.Member(result[i][1], result[i][2], result[i][3], result[i][4], result[i][5], result[i][6], result[i][7], result[i][8])

    def add_member(first_name, last_name, age, gender, weight,
                    address, email, phone):
            # Connect to the SQLite database
            conn = sqlite3.connect("fitplus.db")
            cursor = conn.cursor()

            # Insert the member data into the Members table
            cursor.execute(
                """
                INSERT INTO Members (member_id, first_name, last_name, age, gender, weight, address, email, phone, registration_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (first_name, last_name, age, gender, weight, address,
                email, phone))

            # Commit the changes and close the connection
            conn.commit()






