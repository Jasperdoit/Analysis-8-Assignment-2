# from database import Database
import base64
import os
from datetime import datetime


class Logger:
    def __init__(self):
        self.key = "g"
        self.delimiter = ","

    def _encrypt_message(self, lst: list[str]) -> str:
        # XOR encryption
        encrypted_message = ""
        message = self.delimiter.join(lst)
        for char in message:
            encrypted_char = chr(ord(char) ^ ord(self.key))
            encrypted_message += encrypted_char
        return encrypted_message

    def _decrypt_message(self, encrypted_message: str) -> str:
        # XOR decryption
        decrypted_message = ""
        for char in encrypted_message:
            decrypted_char = chr(ord(char) ^ ord(self.key))
            decrypted_message += decrypted_char
        return decrypted_message

    @staticmethod
    def write_to_log(self, lst: list[str]):
        file_to_check = os.path.abspath(f'./logs/Fitplus-{datetime.now().strftime("%Y-%m-%d")}.log')
        encrypted_log = self._encrypt_message(lst)
        encoded_log = base64.b64encode(encrypted_log.encode())
        if os.path.exists(file_to_check):
            with open(file_to_check, 'ab') as file:
                file.write(encoded_log + b'\n')

        else:
            with open(file_to_check, 'wb') as file:
                file.write(encoded_log + b'\n')

    @staticmethod
    def read_from_log(self):
        t = Table()
        data = list[list]()
        with open(os.path.abspath(f'./logs/Fitplus-{datetime.now().strftime("%Y-%m-%d")}.log'), 'rb') as file:
            encoded_lines = file.readlines()
            for line in encoded_lines:
                decoded_log = base64.b64decode(line)
                decrypted_log = self._decrypt_message(decoded_log.decode())
                data.append(decrypted_log.split(self.delimiter))
        for line in data:
            t.add_row(line)
        t.print_table()


class LogMessage:
    def __init__(self):
        self.no = LogMessage.get_log_length()
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.time = datetime.now().strftime("%H:%M:%S")
        self.username = str
        self.activity = str
        self.info = str
        self.suspicious = str

    def set_username(self, username: str):
        self.username = username

    def set_activity(self, activity: str):
        self.activity = activity

    def set_info(self, info: str):
        self.info = info

    def set_sussy(self, suspicious: str):
        self.suspicious = suspicious

    def create_log(self) -> list[str]:
        return f'{self.no},{self.date},{self.time},{self.username},{self.activity},{self.info},{self.suspicious}'.split(
            ',')

    @staticmethod
    def get_log_length() -> int:
        try:
            with open(os.path.abspath(f'./logs/Fitplus-{datetime.now().strftime("%Y-%m-%d")}.log'), 'r') as file:
                return len(file.readlines()) + 1
        except:
            return 1


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


