from trainer import Trainer
from datetime import datetime
from security import security
from database import database
from passwordmanager import passwordmanager
from display import display
from trainermodifier import trainermodifier
import getpass


class SystemAdmin(Trainer):
  def __init__(self, username, password, firstName, lastName, registrationDate = datetime.now()):
    super().__init__(username, password, firstName, lastName, registrationDate)

  def check_users():
    # List all trainers, systemadmins in the system and their role.
    trainers : list[Trainer] = database.get_all_trainers() or list()
    systemadmins : list[SystemAdmin] = database.get_all_systemadmins() or list()
    for trainer in trainers:
      print(f"Trainer: {trainer[1]} - {trainer[3]}")
    for systemadmin in systemadmins:
      print(f"SystemAdmin: {systemadmin[1], systemadmin[6]}")
    input("Press enter to continue...")

  def add_trainer() -> None:
    print("[!] Adding trainer.")
    username = input("[+] Enter username: ")
    if not security.is_valid_username(username):
      input("Invalid username.")
      return
    if database.username_exists(username):
      input("Username already exists.")
      return
    password = input("[+] Enter password: ")
    if not security.is_valid_password(password):
      input("Invalid password.")
      return
    password = passwordmanager.encrypt(password)
    firstName = input("[+] Enter first name: ")
    lastName = input("[+] Enter last name: ")
    trainer = Trainer(username, password, firstName, lastName)
    database.add_trainer(trainer.to_tuple())
    print("[+] Trainer added.")
    input("Press enter to continue...")

  def view_trainer() -> None:
    print("[!] Viewing trainer.")
    keyword = input("[+] Enter keyword: ")

    
    trainer = database.get_trainer_by_keyword(keyword)

    if trainer is None:
      input("Trainer not found.")
      return
    
    
    trainer : Trainer = Trainer.from_tuple(trainer)

    display.clearConsole()

    print("[!] Trainer found.")
    print(f"Username: {trainer.username}")
    print(f"First name: {trainer.firstName}")
    print(f"Last name: {trainer.lastName}")
    print(f"Registration date: {trainer.registrationDate}")
    print("")
    print("[1] Modify trainer")
    print("[2] Delete trainer")
    print("[3] Reset password")
    print("[4] Go back")

    choice = input("Enter choice: ")

    if choice == "1":
      SystemAdmin.modify_trainer(trainer)
    elif choice == "2":
      trainermodifier.delete_trainer(trainer)
    elif choice == "3":
      trainermodifier.reset_trainer_password(trainer)
    elif choice == "4":
      return
    else:
      input("[!] Invalid choice.")
      return
    
  def modify_trainer(trainer : Trainer) -> None:
    print("[!] Modifying trainer.")
    print("[1] Modify username")
    print("[2] Modify password")
    print("[3] Modify first name")
    print("[4] Modify last name")
    print("[5] Go back")

    choice = input("Enter choice: ")

    if choice == "1":
      trainermodifier.modify_trainer_username(trainer)
    elif choice == "2":
      trainermodifier.modify_trainer_password(trainer)
    elif choice == "3":
      trainermodifier.modify_trainer_firstname(trainer)
    elif choice == "4":
      trainermodifier.modify_trainer_lastname(trainer)
    elif choice == "5":
      return
    else:
      input("[!] Invalid choice.")
      return
    
  def delete_memberrecord() -> None:
    database.delete_member()


class AdminPass:
    def update_password() -> None:
        username = input("[!] Enter username: ")
        password = getpass.getpass("[!] Enter current password: ")

        if database.check_password(username, password) == False:
            input("Wrong credentials.")
            return

        admin = database.get_admin_by_username(username)

        if admin is None:
            input("Trainer not found.")
            return

        from adminmodifier import adminmodifier
        adminmodifier.modify_systemadmin_password(admin)