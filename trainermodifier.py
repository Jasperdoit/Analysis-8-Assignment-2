from trainer import Trainer
from security import security
from database import database
from passwordmanager import passwordmanager
from display import display
class trainermodifier:
    def update_trainer(trainer : Trainer, old_username : str) -> None:
        trainer : tuple = Trainer.to_tuple(trainer)
        database.update_trainer(old_username, trainer)

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
