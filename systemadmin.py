from trainer import Trainer
from datetime import datetime
from security import security
from database import database
from passwordmanager import passwordmanager
from display import display
from trainermodifier import trainermodifier


class SystemAdmin(Trainer):
  def __init__(self, username, password, firstName, lastName, registrationDate = datetime.now()):
    super().__init__(username, password, firstName, lastName, registrationDate)

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
    print(f"Role: {trainer.role}")
    print("")
    print("[1] Modify trainer")
    print("[2] Delete trainer")
    print("[3] Go back")

    choice = input("Enter choice: ")

    if choice == "1":
      SystemAdmin.modify_trainer(trainer)
    elif choice == "2":
      SystemAdmin.delete_trainer(trainer)
    elif choice == "3":
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