import os
import sys
import sqlite3
import hashlib
import re
import random
from trainer import Trainer
from membermodifier import membermodifier
from database import database as db
from systemadmin import SystemAdmin
from superadmin import SuperAdmin
from string import ascii_letters, digits, punctuation
from database_setup import database_setup
from display import display
import os
import sys
from passwordmanager import passwordmanager
from security import security
import getpass
from trainer import TrainerPass
from backup import Backup

def Login() -> None:
    print("[!] Log in to Fitplus.")
    username = input("[+] Enter your username: ")
    display.clearConsole()
    if not security.is_valid_username(username) or db.username_exists(username) == False:
        menuOptions = { "1": Login, "2": ShowMenu }
        print("[!] Sorry this is not right please try again.")
        print("[1] Try again.")
        print("[2] Go back.")
        showMenuOptions(menuOptions, Login)
            
    password = getpass.getpass("[+] Enter your password: ")

    display.clearConsole()


    if username != "super_admin":
        if security.is_valid_password(password) == False or db.check_password(username, password) == False:
            menuOptions = { "1": Login, "2": ShowMenu }
            print("[!] Sorry this is not right please try again.")
            print("[1] Try again.")
            print("[2] Go back.")
            showMenuOptions(menuOptions, Login)
    else:
        if db.check_password(username, password) == False:
            menuOptions = { "1": Login, "2": ShowMenu }
            print("[!] Sorry this is not right please try again.")
            print("[1] Try again.")
            print("[2] Go back.")
            showMenuOptions(menuOptions, Login)

    role = db.get_user_role(username)

    # Proceed with the appropriate actions based on the user's role
    if role == "trainer":
        showTrainerMenu()
    elif role == "system_admin":
        showSystemAdminMenu()
    elif role == "super_admin":
        showSuperAdminMenu()
    else:
        DisplayError("Invalid user role.")
        
def ShowMenu() -> None:
    menuOptions = { "1": Login, "2": Exit }
    display.clearConsole()

    print("[!] Welcome to Fitplus!")
    print("[+] Please Choose an option.")
    print("[1] Log in")
    print("[2] Exit")
    showMenuOptions(menuOptions, ShowMenu)

def showMenuOptions(menuOptions, func):
    try:
        userInput = input("[?] Option: ")
        assert 0 < int(userInput) <= len(menuOptions)
        display.clearConsole()
        menuOptions[userInput]()
    except Exception as e:
        customError(func, e)
    display.clearConsole()
    return func()

def customError(func, e):
    display.clearConsole()
    print("[!] Invalid input, please try again.")
    print('An exception occurred: {}'.format(e))
    input("show error 1")

def DisplayError(error):
    print(f"ERROR: {error}")

def showTrainerMenu() -> None:
    trainerOptions = { "1": TrainerPass.update_password, "2": Trainer.add_member, "3": Trainer.view_member, "4": Trainer.view_member, "5": Login }
    print("[!] This is the trainer menu.")
    print("[+] Please Choose an option.")
    print("[1] Update password.")
    print("[2] Add member.")
    print("[3] Modify member.")
    print("[4] Search member.")
    print("[5] Logout.")
    showMenuOptions(trainerOptions, showTrainerMenu)

def showSystemAdminMenu() -> None:
    systemAdminOptions = { "1": SystemAdmin.update_password, "2": SystemAdmin.check_users, "3": SystemAdmin.add_trainer, "4": SystemAdmin.view_trainer, "5": SystemAdmin.view_trainer, "6": SystemAdmin.view_trainer, "9": SystemAdmin.add_member, "10": SystemAdmin.view_member, "11": SystemAdmin.delete_memberrecord, "12": SystemAdmin.view_member, "13": Login}
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
    print("[2] Add trainer.")
    print("[3] Modify trainer.")
    print("[4] Delete trainers.")
    print("[5] Reset trainer password.")
    print("[6] Add admin.")
    print("[7] Modify admin.")
    print("[8] Delete admin")
    print("[9] Reset admin password.")
    print("[10] Make backup.")
    print("[11] Restore backup.")
    print("[12] See logs.")
    print("[13] Add member.")
    print("[14] Modify member.")
    print("[15] Delete member record.")
    print("[16] Search member.")
    print("[17] Logout.")
    showMenuOptions(superAdminOptions, Login)

def Exit() -> None:
    sys.exit()

if __name__ == "__main__":
    if not os.path.exists('./logs'):
        os.mkdir('./logs')
    if not os.path.exists('./backup'):
        os.mkdir('./backup')

    database_setup.setup_database()
    database_setup.setup_superadmin("super_admin", "Admin_123!")
    database_setup.create_test_trainer()
    ShowMenu()
