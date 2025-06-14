# File: app/encryptor.py
import os
from cryptography.fernet import Fernet

class CulturalVault:
    def __init__(self, key_path='vault.key'):
        if not os.path.exists(key_path):
            self.key = Fernet.generate_key()
            with open(key_path, 'wb') as f:
                f.write(self.key)
        else:
            with open(key_path, 'rb') as f:
                self.key = f.read()
        self.cipher = Fernet(self.key)

    def encrypt_file(self, input_path, output_path):
        with open(input_path, 'rb') as file:
            encrypted = self.cipher.encrypt(file.read())
        with open(output_path, 'wb') as file:
            file.write(encrypted)

    def decrypt_file(self, input_path, output_path):
        with open(input_path, 'rb') as file:
            decrypted = self.cipher.decrypt(file.read())
        with open(output_path, 'wb') as file:
            file.write(decrypted)