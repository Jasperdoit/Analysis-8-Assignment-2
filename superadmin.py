from display import display
from systemadmin import SystemAdmin
from trainer import Trainer
from security import security
from passwordmanager import passwordmanager
from database import database
from adminmodifier import adminmodifier
import datetime

class SuperAdmin(SystemAdmin):

  def __init__(self, username, password, firstName = "", lastName = "", registrationDate = datetime.datetime.now()):
    super().__init__(username, password, firstName, lastName, registrationDate)
    self.role = "superadmin"

  def add_systemadmin() -> None:
    print("[!] Adding systemadmin.")
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
    systemadmin = SystemAdmin(username, password, firstName, lastName)
    database.add_admin(systemadmin.to_tuple())
    print("[+] SystemAdmin added.")
    input("Press enter to continue...")
  
  def view_systemadmin() -> None:
    print("[!] Viewing System Admin.")
    keyword = input("[+] Enter keyword: ")

    
    admin = database.get_systemadmin_by_keyword(keyword)

    if admin is None:
      input("SystemAdmin not found.")
      return
    
    
    admin : SystemAdmin = SystemAdmin.from_tuple(admin)

    display.clearConsole()

    print("[!] SystemAdmin found.")
    print(f"Username: {admin.username}")
    print(f"First name: {admin.firstName}")
    print(f"Last name: {admin.lastName}")
    print(f"Registration date: {admin.registrationDate}")
    print(f"Role: {admin.role}")
    print("")
    print("[1] Modify SystemAdmin")
    print("[2] Delete SystemAdmin")
    print("[3] Reset password")
    print("[4] Go back")

    choice = input("Enter choice: ")

    if choice == "1":
      SuperAdmin.modify_admin(admin)
    elif choice == "2":
      adminmodifier.delete_systemadmin(admin)
    elif choice == "3":
      adminmodifier.reset_systemadmin_password(admin)
    elif choice == "4":
      return
    else:
      input("[!] Invalid choice.")
      return
    
  def modify_admin(admin : SystemAdmin) -> None:
    print("[!] Modifying SystemAdmin.")
    print("[1] Modify username")
    print("[2] Modify password")
    print("[3] Modify first name")
    print("[4] Modify last name")
    print("[5] Go back")

    choice = input("Enter choice: ")

    if choice == "1":
      adminmodifier.modify_systemadmin_username(admin)
    elif choice == "2":
      adminmodifier.modify_systemadmin_password(admin)
    elif choice == "3":
      adminmodifier.modify_systemadmin_firstname(admin)
    elif choice == "4":
      adminmodifier.modify_systemadmin_lastname(admin)
    elif choice == "5":
      return
    else:
      input("[!] Invalid choice.")
      return
  