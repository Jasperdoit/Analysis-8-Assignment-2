# from database import Database
import logging
import base64
import os
from datetime import datetime


class Logger:
    def __init__(self):
        # self.key = "dhg74n3fg2"
        self.key = "g"
        self.delimiter = ","

    def _encrypt_message(self, lst: list[str]) -> str:
        # Simple XOR encryption
        encrypted_message = ""
        message = self.delimiter.join(lst)
        for char in message:
            encrypted_char = chr(ord(char) ^ ord(self.key))
            encrypted_message += encrypted_char
        return encrypted_message

    def _decrypt_message(self, encrypted_message: str) -> str:
        # Simple XOR decryption
        decrypted_message = ""
        for char in encrypted_message:
            decrypted_char = chr(ord(char) ^ ord(self.key))
            decrypted_message += decrypted_char
        return decrypted_message

    def write_to_log(self, lst: list[str]):
        fileToCheck = f'{datetime.now().strftime("%Y-%m-%d")}.log'
        encrypted_log = self._encrypt_message(lst)
        encoded_log = base64.b64encode(encrypted_log.encode())
        if os.path.exists(fileToCheck):
            with open(fileToCheck, 'ab') as file:
                file.write(encoded_log + b'\n')

        else:
            with open(fileToCheck, 'wb') as file:
                file.write(encoded_log + b'\n')

    def read_from_log(self):
        t = Table()
        data = list[list]()
        with open(f'{datetime.now().strftime("%Y-%m-%d")}.log', 'rb') as file:
            encoded_lines = file.readlines()
            for line in encoded_lines:
                decoded_log = base64.b64decode(line)
                decrypted_log = self._decrypt_message(decoded_log.decode())
                data.append(decrypted_log.split(self.delimiter))
        for line in data:
            t.add_row(line)
        t.print_table()

    def get_log_length(self) -> int:
        try:
            with open(f'{datetime.now().strftime("%Y-%m-%d")}.log', 'r') as file:
                return len(file.readlines())
        except:
            return 0
            pass


class Table:
    def __init__(self, border=' | ', bot_char='-'):
        self.headers = ["No.", "Date", "Time", "Username", "Description of activity", "Additional Information", "Suspicious"]
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
