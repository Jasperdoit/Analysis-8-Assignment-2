import os
class display:
    def clearConsole():
        os.system('cls' if os.name == 'nt' else 'clear')