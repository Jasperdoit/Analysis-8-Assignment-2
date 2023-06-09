import hashlib
class passwordmanager:
    def encrypt(password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password
