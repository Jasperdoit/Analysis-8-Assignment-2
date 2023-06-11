import os
import re
import sqlite3
import hashlib
from database import database as db
from datetime import datetime
from display import display
from membermodifier import membermodifier
import getpass
from security import security
# from trainermodifier import trainermodifier

class Trainer:
    def __init__(self, username : str, password : str, firstName : str, lastName : str, registrationDate : datetime = datetime.now()):
        self.username : str = username
        self.password : str = password
        self.firstName : str = firstName
        self.lastName : str = lastName
        self.registrationDate : datetime = registrationDate

    def set_first_name(self, firstName : str):
        self.firstName = firstName

    def set_last_name(self, lastName : str):
        self.lastName = lastName

    def set_registration_date(self, registrationDate : datetime):
        self.registrationDate = registrationDate

    
    def add_member() -> None:
        print("[!] Adding member.")

        memberid = security.make_memberid()
        first_name = security.get_valid_input("[+] Enter first name: ", lambda value: value.strip() != "")
        last_name = security.get_valid_input("[+] Enter last name: ", lambda value: value.strip() != "")
        age = security.get_valid_input("[+] Enter age (number): ", security.is_valid_number)
        gender = security.get_valid_input("[+] Enter gender (M/F/O): ", security.is_valid_gender)
        weight = security.get_valid_input("[+] Enter weight (kg): ", security.is_valid_number)
        street = security.get_valid_input("[+] Enter street name: ", lambda value: value.strip() != "")
        housenumber = security.get_valid_input("[+] Enter housenumber: ", security.is_valid_number)
        zipcode = security.get_valid_input("[+] Enter zipcode (DDDDXX): ", lambda value: value.strip() != "")
        city = security.choose_city()
        email = security.get_valid_input("[+] Enter email address: ", security.is_valid_email)
        phone = security.get_valid_input("[+] Enter phone number: ", security.is_valid_phone_number)

        db.add_member(memberid, first_name, last_name, age, gender, weight, street, housenumber, zipcode, city, email, phone)
        input("Added member succesfully.")


    def modify_member() -> None:
        print("[!] Modifying member.")
        print("[1] Modify firstname")
        print("[2] Modify lastname")
        print("[3] Modify phone")
        print("[4] Modify email")
        print("[5] Modify address")
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
        

        display.clearConsole()

        print("[!] Member found.")
        db.print_member(keyword)
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
        return (self.username, self.password, self.firstName, self.lastName, self.registrationDate)
    
    def from_tuple(tuple) -> 'Trainer':
        trainer = Trainer(tuple[1], tuple[2], tuple[3], tuple[4], tuple[5])
        trainer.id = tuple[0]
        return trainer
    
    
class TrainerPass:
    def update_password() -> None:
        username = input("[!] Enter username: ")
        password = getpass.getpass("[!] Enter current password: ")

        if db.check_password(username, password) == False:
            input("Wrong credentials.")
            return

        trainer = db.get_trainer_by_username(username)

        if trainer is None:
            input("Trainer not found.")
            return

        trainer : Trainer = Trainer.from_tuple(trainer)

        from trainermodifier import trainermodifier
        trainermodifier.modify_trainer_password(trainer)