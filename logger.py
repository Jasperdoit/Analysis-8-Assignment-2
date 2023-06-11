from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from encryption import Encryption
from datetime import datetime

import os

DELIMITER = ','


class Logger:

    @staticmethod
    def write_to_log(lst: list[str]):
        file_to_check = os.path.abspath(f'./logs/Fitplus-{datetime.now().strftime("%Y-%m-%d")}.log')
        lst_to_string = ','.join(lst)
        encrypted_log = Encryption().encrypt(lst_to_string)
        if os.path.exists(file_to_check):
            with open(file_to_check, 'a') as file:
                file.write(encrypted_log + '\n')

        else:
            with open(file_to_check, 'w') as file:
                file.write(encrypted_log + '\n')

    @staticmethod
    def show_log():
        t = Table()
        data = list[list]()
        with open(os.path.abspath(f'./logs/Fitplus-{datetime.now().strftime("%Y-%m-%d")}.log'), 'r') as file:
            encoded_lines = file.readlines()
            for line in encoded_lines:
                decrypted_log = Encryption().decrypt(line)
                data.append(decrypted_log.split(DELIMITER))
        for line in data:
            t.add_row(line)
        t.print_table()


class LogMessage:
    def __init__(self):
        self.no = self._get_log_length()
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.time = datetime.now().strftime("%H:%M:%S")
        self.username = str
        self.activity = str
        self.info = str
        self.suspicious = str

    def set_username(self, username: str):
        self.username = username
        return self

    def set_activity(self, activity: str):
        self.activity = activity
        return self

    def set_info(self, info: str):
        self.info = info
        return self

    def set_not_suspicious(self):
        self.suspicious = "no"
        return self

    def set_suspicious(self):
        self.suspicious = "yes"
        return self

    def create_log(self) -> list[str]:
        log_message = f'{self.no},{self.date},{self.time},{self.username},{self.activity},{self.info},{self.suspicious}'.split(
            ',')
        Logger().write_to_log(log_message)

    def _get_log_length(self) -> int:
        try:
            with open(os.path.abspath(f'./logs/Fitplus-{datetime.now().strftime("%Y-%m-%d")}.log'), 'r') as file:
                return len(file.readlines()) + 1
        except:
            return 1


class LogMessages(LogMessage):
    @staticmethod
    def log_user_deleted(username: str, deleted_user: str):
        LogMessage() \
            .set_username(username) \
            .set_activity(f"User is deleted") \
            .set_info(f"username: {deleted_user}") \
            .set_not_suspicious() \
            .create_log()

    @staticmethod
    def log_user_modified(username: str, modified_user: str):
        LogMessage() \
            .set_username(username) \
            .set_activity("User is modified") \
            .set_info(f"username: {modified_user}") \
            .set_not_suspicious() \
            .create_log()

    @staticmethod
    def log_user_added(username: str, added_user: str):
        LogMessage() \
            .set_username(username) \
            .set_activity("User is created") \
            .set_info(f"username: {added_user}") \
            .set_not_suspicious() \
            .create_log()

    @staticmethod
    def log_user_logged_in(username: str):
        LogMessage() \
            .set_username(username) \
            .set_activity("Logged in") \
            .set_info(f"username: {username}") \
            .set_not_suspicious() \
            .create_log()

    @staticmethod
    def log_user_logged_out(username: str):
        LogMessage() \
            .set_username(username) \
            .set_activity("Logged out") \
            .set_info(f"username: {username}") \
            .set_not_suspicious() \
            .create_log()


class Table:
    def __init__(self, border=' | ', bot_char='-'):
        self.headers = ["No.", "Date", "Time", "Username", "Description of activity", "Additional Information",
                        "Suspicious"]
        self.columns = len(self.headers)
        self.border = border
        self.bot_char = bot_char
        self.data = []
        self.max_widths = [len(str(header)) for header in self.headers]

    def add_row(self, row):
        if len(row) != self.columns:
            raise ValueError("Number of elements in the row doesn't match the number of columns.")

        self.data.append(row)
        for i, element in enumerate(row):
            self.max_widths[i] = max(self.max_widths[i], len(str(element)))

    def print_table(self):
        total_width = sum(self.max_widths) + len(self.border) * (self.columns - 1) + 7
        border_row = self.bot_char * total_width

        print(border_row)

        # Print the headers
        header_str = self.border.join(header.center(self.max_widths[i]) for i, header in enumerate(self.headers))
        header_row = f"{self.border} {header_str} {self.border}"

        print(header_row)
        print(border_row)

        # Print the table rows
        for row in self.data:
            row_str = self.border.join(str(element).center(self.max_widths[i]) for i, element in enumerate(row))
            row_row = f"{self.border} {row_str} {self.border}"
            print(row_row)

        print(border_row)
