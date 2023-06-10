import os
import re
import sqlite3
import hashlib
from database import database as db
from datetime import datetime
from display import display
from membermodifier import membermodifier
#from trainermodifier import trainermodifier

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

    
    def add_member() -> None:
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

    def update_password() -> None:
        trainer : Trainer = Trainer.from_tuple(trainer)
        trainermodifier.modify_trainer_password(trainer)


    def modify_member() -> None:
        print("[!] Modifying member.")
        print("[1] Modify firstnae")
        print("[2] Modify lastname")
        print("[3] Modify phone")
        print("[4] Modify email")
        print("[5] Go back")

        choice = input("Enter choice: ")

        if choice == "1":
            membermodifier.modify_member_username(trainer)
        elif choice == "2":
            membermodifier.modify_member_password(trainer)
        elif choice == "3":
            membermodifier.modify_member_firstname(trainer)
        elif choice == "4":
            membermodifier.modify_member_lastname(trainer)
        elif choice == "5":
            return
        else:
            input("[!] Invalid choice.")
            return
    
    def view_member() -> None:
        print("[!] Viewing Member.")
        keyword = input("[+] Enter keyword: ")

        member = db.get_member_by_keyword(keyword)

        if member is None:
            input("Member not found.")
            return
        
        member : Member = Member.from_tuple(trainer)

        display.clearConsole()

        print("[!] Member found.")
        print(f"MemberID: {member.memberID}")
        print(f"First name: {member.firstName}")
        print(f"Last name: {member.lastName}")
        print(f"Registration date: {member.registrationDate}")
        print("")
        print("[1] Modify member")
        print("[2] Delete member")
        print("[3] Go back")

        choice = input("Enter choice: ")

        if choice == "1":
            Trainer.modify_member(member)
        elif choice == "2":
            membermodifier.delete_member(member)
        elif choice == "3":
            return
        else:
            input("[!] Invalid choice.")
            return

    def to_tuple(self):
        return (self.username, self.password, self.firstName, self.lastName, self.registrationDate, self.role)
    
    def from_tuple(tuple) -> 'Trainer':
        trainer = Trainer(tuple[1], tuple[2], tuple[3], tuple[4], tuple[5])
        trainer.id = tuple[0]
        return trainer