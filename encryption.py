import base64
import os
import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

class Encryption:
    private_key = None
    public_key = None
    def __init__(self):
        if not os.path.exists('private.pem') or not os.path.exists('public.pem'):
            self.create_initial()
        Encryption.private_key = self.load_private_key()
        Encryption.public_key = self.load_public_key()


    @staticmethod
    def load_private_key():
        if Encryption.private_key is not None:
            return Encryption.private_key
        while True:
            print("[!] Master password required")
            password = input("Please enter your master password: ")
            password_hash = hashlib.sha256(password.encode()).digest()
            with open('master_password', 'rb') as f:
                correct_hash = f.read()
                if correct_hash == password_hash:
                    break
                else:
                    print("Incorrect password.")
                    input("Press enter to try again.")
        return serialization.load_pem_private_key(
            open('private.pem', 'rb').read(),
            password=password.encode()
        )


    @staticmethod
    def load_public_key():
        if Encryption.public_key is not None:
            return Encryption.public_key
        with open('public.pem', 'rb') as f:
            public_key = serialization.load_pem_public_key(
                f.read()
            )
        return public_key
    def create_initial(self):
        print("[!] Generating keys...")
        print("To generate the key, we need you to make a master password.")
        print("This password needs to be used everytime the system starts up.")
        print("This password is not recoverable, so please remember it.")
        password = input("Please enter your master password: ")
        
        # Hash the password
        password_hash = hashlib.sha256(password.encode()).digest()
        # And store the hash in a file
        with open('master_password', 'wb') as f:
            f.write(password_hash)
        
        # Generate the keys. Make sure the private key is secured with the password.
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096,
        )
        public_key = private_key.public_key()
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(password.encode()),
        )
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        
        # store keys
        with open('private.pem', 'wb') as f:
            f.write(private_pem)
        with open('public.pem', 'wb') as f:
            f.write(public_pem)
    
    def encrypt(self, message: str):
        message_bytes = message.encode()
        encrypted = Encryption.public_key.encrypt(
            message_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA512(),
                label=None
            )
        )
        return base64.b64encode(encrypted)
    
    def decrypt(self, message: str):
        message = base64.b64decode(message)
        decrypted = Encryption.private_key.decrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA512(),
                label=None
            )
        )
        return decrypted.decode('utf-8')

