from trainer import Trainer
from database import database as db
from systemadmin import SystemAdmin
from superadmin import SuperAdmin
from database_setup import database_setup
from display import display
import os
import sys
from security import security
import getpass
from trainer import TrainerPass
from backup import Backup
from logger import Logger


def Login() -> None:
    print("[!] Log in to Fitplus.")
    username = input("[+] Enter your username: ")
    display.clearConsole()
    if not security.is_valid_username(username) or not db.username_exists(username):
        menu_options = {"1": Login, "2": show_menu}
        print("[!] Sorry this is not right please try again.")
        print("[1] Try again.")
        print("[2] Go back.")
        show_menu_options(menu_options, Login)

    password = getpass.getpass("[+] Enter your password: ")

    display.clearConsole()

    if username != "super_admin":
        if not security.is_valid_password(password) or not db.check_password(username, password):
            menu_options = {"1": Login, "2": show_menu}
            print("[!] Sorry this is not right please try again.")
            print("[1] Try again.")
            print("[2] Go back.")
            show_menu_options(menu_options, Login)
    else:
        if not db.check_password(username, password):
            menu_options = {"1": Login, "2": show_menu}
            print("[!] Sorry this is not right please try again.")
            print("[1] Try again.")
            print("[2] Go back.")
            show_menu_options(menu_options, Login)

    role = db.get_user_role(username)

    # Proceed with the appropriate actions based on the user's role
    if role == "trainer":
        show_trainer_menu()
    elif role == "system_admin":
        show_system_admin_menu()
    elif role == "super_admin":
        show_super_admin_menu()
    else:
        display_error("Invalid user role.")


def show_menu() -> None:
    menu_options = {"1": Login, "2": exit}
    display.clearConsole()

    print("[!] Welcome to Fitplus!")
    print("[+] Please Choose an option.")
    print("[1] Log in")
    print("[2] Exit")
    show_menu_options(menu_options, show_menu)


def show_menu_options(menu_options, func):
    try:
        user_input = input("[?] Option: ")
        assert 0 < int(user_input) <= len(menu_options)
        display.clearConsole()
        menu_options[user_input]()
    except Exception as e:
        custom_error(func, e)
    display.clearConsole()
    return func()


def custom_error(func, e):
    display.clearConsole()
    print("[!] Invalid input, please try again.")
    print('An exception occurred: {}'.format(e))
    input("show error 1")


def display_error(error):
    print(f"ERROR: {error}")


def show_trainer_menu() -> None:
    trainer_options = {"1": TrainerPass.update_password, "2": Trainer.add_member, "3": Trainer.view_member,
                       "4": Trainer.view_member, "5": Login}
    print("[!] This is the trainer menu.")
    print("[+] Please Choose an option.")
    print("[1] Update password.")
    print("[2] Add member.")
    print("[3] Modify member.")
    print("[4] Search member.")
    print("[5] Logout.")
    show_menu_options(trainer_options, show_trainer_menu)


def show_system_admin_menu() -> None:
    system_admin_options = {"1": SystemAdmin.update_password, "2": SystemAdmin.check_users,
                            "3": SystemAdmin.add_trainer,
                            "4": SystemAdmin.view_trainer, "5": SystemAdmin.view_trainer, "6": SystemAdmin.view_trainer,
                            "9": SystemAdmin.add_member, "10": SystemAdmin.view_member,
                            "11": SystemAdmin.delete_memberrecord, "12": SystemAdmin.view_member, "14": Login}
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
    print("[14] Logout" )
    show_menu_options(system_admin_options, show_trainer_menu)


def show_super_admin_menu():
    super_admin_options = {"1": SuperAdmin.check_users, "2": SuperAdmin.add_trainer, "3": SuperAdmin.view_trainer, "4": SuperAdmin.view_trainer,
                           "5": SuperAdmin.view_trainer, "6": SuperAdmin.add_systemadmin, "7": SuperAdmin.modify_admin, "8": SuperAdmin.view_systemadmin,
                           "9": SuperAdmin.view_systemadmin, "10": Backup.create_backup, "11": Backup.restore_backup, "12": Logger.read_from_log,
                           "13": SuperAdmin.add_member, "14": SuperAdmin.view_member, "15": SuperAdmin.delete_memberrecord, "16": SuperAdmin.view_member, 
                           "17": Login}
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
    show_menu_options(super_admin_options, Login)


def exit() -> None:
    sys.exit()


if __name__ == "__main__":
    if not os.path.exists('./logs'):
        os.mkdir('./logs')
    if not os.path.exists('./backup'):
        os.mkdir('./backup')

    database_setup.setup_database()
    database_setup.setup_superadmin("super_admin", "Admin_123!")
    #database_setup.create_test_trainer()
    show_menu()
