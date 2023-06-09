from trainer import Trainer
from security import security
from database import database
from passwordmanager import passwordmanager
from display import display
class trainermodifier:
    def update_trainer(trainer : Trainer, old_username : str) -> None:
        trainer : tuple = Trainer.to_tuple(trainer)
        database.update_trainer(old_username, trainer)

    def reset_trainer_password(trainer : Trainer):
        display.clearConsole()
        print("[!] Resetting password.")
        print("[!] This will generate a new password. Make sure to write it down.")
        confirmation = input(f"[+] Are you sure you want to reset the password of trainer {trainer.username}? (y/n):")
        if confirmation.lower() != "y":
            return
        # generate a new password that conforms to the password policy
        trainer.password = passwordmanager.generate_password()
        display_password : str = trainer.password
        # encrypt the password
        trainer.password = passwordmanager.encrypt(trainer.password)
        # update the trainer in the database
        trainermodifier.update_trainer(trainer, trainer.username)
        # display the new password to the user
        display.clearConsole()
        print("[+] Password reset.")
        print(f"[+] New password: {display_password}")
        input("Press enter to continue...")

    def modify_trainer_username(trainer : Trainer):
        previous_username : str = trainer.username
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
        trainer.username = new_username
        trainermodifier.update_trainer(trainer, previous_username)
        display.clearConsole()
        print("[+] Username changed.")
        input("Press enter to continue...")

    def modify_trainer_password(trainer : Trainer):
        previous_username : str = trainer.username
        display.clearConsole()
        print("[!] Changing password.")
        new_password = input("[+] Enter your new password:")
        if not security.is_valid_password(new_password):
            display.clearConsole()
            input("Invalid password.")
            return
        trainer.password = new_password
        trainer.password = passwordmanager.encrypt(trainer.password)
        trainermodifier.update_trainer(trainer, previous_username)
        display.clearConsole()
        print("[+] Password changed.")
        input("Press enter to continue...")

    def modify_trainer_firstname(trainer : Trainer):
        previous_username : str = trainer.username
        display.clearConsole()
        print("[!] Changing first name.")
        new_firstname = input("[+] Enter your new first name:")
        trainer.firstName = new_firstname
        trainermodifier.update_trainer(trainer, previous_username)
        display.clearConsole()
        print("[+] First name changed.")
        input("Press enter to continue...")

    def modify_trainer_lastname(trainer : Trainer):
        previous_username : str = trainer.username
        display.clearConsole()
        print("[!] Changing last name.")
        new_lastname = input("[+] Enter your new last name:")
        trainer.lastName = new_lastname
        trainermodifier.update_trainer(trainer, previous_username)
        display.clearConsole()
        print("[+] Last name changed.")
        input("Press enter to continue...")
    
    def delete_trainer(trainer : Trainer):
        display.clearConsole()
        print(f"[!] You are about to delete the trainer {trainer.username}. This action cannot be undone.")
        confirmation = input("[+] Are you sure you want to continue? (y/n):")
        if confirmation.lower() != "y":
            return
        database.delete_trainer(trainer.username)
        display.clearConsole()
        print("[+] Trainer removed.")
        input("Press enter to continue...")