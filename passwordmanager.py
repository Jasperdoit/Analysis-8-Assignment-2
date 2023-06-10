import hashlib
import random
import string
class passwordmanager:
    def encrypt(password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def generate_password() -> str:
        password_length = random.randint(12, 30)
        special_characters = " ~!@#$%&_-+=`|\\(){}[]:;'<>,.?/"
        allowed_characters = string.ascii_letters + string.digits + special_characters
        password = ""
        for i in range(password_length):
            password += random.choice(allowed_characters)
        return password
    
    
