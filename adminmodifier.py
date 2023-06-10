from systemadmin import SystemAdmin
from database import database
from display import display
from passwordmanager import passwordmanager
from security import security
class adminmodifier:
    def update_systemadmin(systemadmin : SystemAdmin, old_username : str) -> None:
        """Updates a systemadmin in the database. The old username is used to identify the systemadmin in the database."""
        systemadmin : tuple = SystemAdmin.to_tuple(systemadmin)
        database.update_systemadmin(old_username, systemadmin)

    def reset_systemadmin_password(systemadmin : SystemAdmin):
        """Prompts the user to confirm the reset of the password of the systemadmin. If the user confirms, a new password is generated and displayed to the user. The new password is displayed to the user."""
        display.clearConsole()
        print("[!] Resetting password.")
        print("[!] This will generate a new password. Make sure to write it down.")
        confirmation = input(f"[+] Are you sure you want to reset the password of SystemAdmin {systemadmin.username}? (y/n):")
        if confirmation.lower() != "y":
            return
        # generate a new password that conforms to the password policy
        systemadmin.password = passwordmanager.generate_password()
        display_password : str = systemadmin.password
        # encrypt the password
        systemadmin.password = passwordmanager.encrypt(systemadmin.password)
        # update the systemadmin in the database
        adminmodifier.update_systemadmin(systemadmin, systemadmin.username)
        # display the new password to the user
        display.clearConsole()
        print("[+] Password reset.")
        print(f"[+] New password: {display_password}")
        input("Press enter to continue...")

    def modify_systemadmin_username(systemadmin : SystemAdmin):
        """promts the user to enter a new username. If the username is valid and not already taken, the username is changed."""
        previous_username : str = systemadmin.username
        display.clearConsole()
        print("[!] Changing username.")
        new_username = input("[+] Enter your new username:")
        if not security.is_valid_username(new_username):
            display.clearConsole()
            input("Invalid username.")
            return
        if database.username_exists(new_username):
            display.clearConsole()
            input("Username already exists.")
            return
        systemadmin.username = new_username
        adminmodifier.update_systemadmin(systemadmin, previous_username)
        display.clearConsole()
        print("[+] Username changed.")
        input("Press enter to continue...")

    def modify_systemadmin_password(systemadmin : SystemAdmin):
        """prompts the user to enter a new password. If the password is valid, the password is changed."""
        previous_username : str = systemadmin.username
        display.clearConsole()
        print("[!] Changing password.")
        new_password = input("[+] Enter your new password:")
        if not security.is_valid_password(new_password):
            display.clearConsole()
            input("Invalid password.")
            return
        systemadmin.password = new_password
        systemadmin.password = passwordmanager.encrypt(systemadmin.password)
        adminmodifier.update_systemadmin(systemadmin, previous_username)
        display.clearConsole()
        print("[+] Password changed.")
        input("Press enter to continue...")

    def modify_systemadmin_firstname(systemadmin : SystemAdmin):
        """prompts the user to enter a new first name. The first name is changed regardless of input."""
        previous_username : str = systemadmin.username
        display.clearConsole()
        print("[!] Changing first name.")
        new_firstname = input("[+] Enter your new first name:")
        systemadmin.firstName = new_firstname
        adminmodifier.update_systemadmin(systemadmin, previous_username)
        display.clearConsole()
        print("[+] First name changed.")
        input("Press enter to continue...")

    def modify_systemadmin_lastname(systemadmin : SystemAdmin):
        """prompts the user to enter a new last name. The last name is changed regardless of input."""
        previous_username : str = systemadmin.username
        display.clearConsole()
        print("[!] Changing last name.")
        new_lastname = input("[+] Enter your new last name:")
        systemadmin.lastName = new_lastname
        adminmodifier.update_systemadmin(systemadmin, previous_username)
        display.clearConsole()
        print("[+] Last name changed.")
        input("Press enter to continue...")
    
    def delete_systemadmin(systemadmin : SystemAdmin):
        """prompts the user to confirm the deletion of the systemadmin. If the user confirms, the systemadmin is deleted from the database."""
        display.clearConsole()
        print(f"[!] You are about to delete the SystemAdmin {systemadmin.username}. This action cannot be undone.")
        confirmation = input("[+] Are you sure you want to continue? (y/n):")
        if confirmation.lower() != "y":
            return
        database.delete_systemadmin(systemadmin.username)
        display.clearConsole()
        print("[+] SystemAdmin removed.")
        input("Press enter to continue...")