import re
import random
from datetime import datetime

class security:
    def is_valid_username(username):
        """Validates the username for the following criteria:
        1. The username must start with an alphabet or underscore."""
        # Regex pattern to validate username
        pattern = r'^[a-zA-Z_][a-zA-Z0-9_]{7,11}$'
        return re.match(pattern, username) is not None

    def is_valid_password(password):
        # Regex pattern to validate password
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%&_\-=\\`|\(\){}\[\]:;\'<>,\.\?/])[a-zA-Z\d~!@#$%&_\-=\\`|\(\){}\[\]:;\'<>,\.\?/]{12,30}$"
        return re.match(pattern, password) is not None
    
    def is_valid_gender(gender):
        # List of valid gender options
        valid_genders = ['M', 'F', 'O']
        return gender.upper() in valid_genders

    def is_valid_number(value):
        try:
            float(value)
            if value < 0:
                return False
            return True
        except ValueError:
            return False
        
    def get_valid_input(prompt, validation_func):
        while True:
            value = input(prompt)
            if validation_func(value):
                return value
            else:
                input("[!] Invalid input. Please try again.")

    def is_valid_email(email):
        # Regular expression pattern to validate email address
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
    
    def is_valid_zipcode(zipcode):
        pattern = r'^\d{4}[A-Z]{2}$'
        return re.match(pattern, zipcode) is not None

    def is_valid_phone_number(phone):
        # Regular expression pattern to validate phone number
        pattern = r'^\d{8}$'
        return re.match(pattern, phone) is not None
    
    def valid_cities():
        return ["Tokyo", "Jakarta", "New Dehli", "Mexico City", "Cairo", "Amsterdam", "Paris", "London", "New York", "Moscow"]
    
    def choose_city():
        cities = security.valid_cities()
        print("Choose a city:")
        for i, city in enumerate(cities, start=1):
            print(f"[{i}] {city}")

        while True:
            choice = input("Enter the number corresponding to the city: ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(cities):
                    return cities[choice - 1]
            print("Invalid input. Please choose a valid number.")

    def make_memberid():
        # Get the last two digits of the current year
        current_year = datetime.now().year % 100

        # Generate the first 7 digits randomly
        digits = [current_year // 10, current_year % 10]

        # Append the year digits and calculate the checksum digit
        digits.extend([random.randint(0, 9) for _ in range(7)])

        checksum = sum(digits) % 10
        digits.append(checksum)

        # Convert the digits to a string
        member_id = ''.join(str(digit) for digit in digits)

        return member_id
    

