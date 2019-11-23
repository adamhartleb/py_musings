from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os


class EncryptionManager():
    def __init__(self):
        iv = os.urandom(16)
        key = os.urandom(32)
        aes_context = Cipher(algorithms.AES(
            key), modes.CBC(iv), default_backend())
        self.encryptor = aes_context.encryptor()
        self.decryptor = aes_context.decryptor()
        self.padder = padding.PKCS7(128).padder()
        self.unpadder = padding.PKCS7(128).unpadder()

    def update_encryptor(self, message):
        return self.encryptor.update(self.padder.update(message))

    def finalize_encryptor(self):
        return self.encryptor.update(self.padder.finalize()) + self.encryptor.finalize()

    def update_decryptor(self, message):
        return self.unpadder.update(self.decryptor.update(message))

    def finalize_decryptor(self):
        return self.unpadder.update(self.decryptor.finalize()) + self.unpadder.finalize()


manager = EncryptionManager()

plaintexts = [
    b"SHORT",
    b"MEDIUM MEDIUM MEDIUM",
    b"LONG LONG LONG LONG LONG LONG"
]

ciphertexts = []

for m in plaintexts:
    ciphertexts.append(manager.update_encryptor(m))

ciphertexts.append(manager.finalize_encryptor())

print(ciphertexts)

res = []

for c in ciphertexts:
    res.append(manager.update_decryptor(c))

res.append(manager.finalize_decryptor())

print(res)
