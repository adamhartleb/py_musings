from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os


class EncryptionManager():
    def __init__(self):
        key = os.urandom(32)
        aes_context = Cipher(algorithms.AES(
            key), modes.ECB(), default_backend())
        self.iv = os.urandom(16)
        self.encryptor = aes_context.encryptor()
        self.decryptor = aes_context.decryptor()
        self.padder = padding.PKCS7(128).padder()
        self.unpadder = padding.PKCS7(128).unpadder()
        self.intialized = False

    def bxor(self, b1, b2):
        parts = []
        for b1, b2 in zip(b1, b2):
            parts.append(bytes([b1 ^ b2]))
        return b''.join(parts)

    def initialize_encryptor(self, first_message):
        res = self.padder.update(first_message)
        if res:
            self.intialized = True
            xord_data = self.bxor(self.iv, res)
            return self.encryptor.update(xord_data)

    def update_encryptor(self, prev_message, message):
        if not self.intialized:
            return self.initialize_encryptor(message)
        message = self.padder.update(message)
        if message:
            xord_data = self.bxor(prev_message, message)
            return self.encryptor.update(xord_data)

    def finalize_encryptor(self, prev_message):
        return self.encryptor.update(self.bxor(prev_message, self.padder.finalize())) + self.encryptor.finalize()

    def initialize_decryptor(self, first_message):
        decrypted_message = self.unpadder.update(
            self.decryptor.update(first_message))
        if decrypted_message:
            return self.bxor(self.iv, decrypted_message)

    def update_decryptor(self, prev_message, message):
        decrypted_message = self.unpadder.update(
            self.decryptor.update(message))
        return self.bxor(prev_message, decrypted_message)

    def finalize_decryptor(self, prev_message):
        decrypted_message = self.unpadder.update(
            self.decryptor.finalize()) + self.unpadder.finalize()
        return self.bxor(prev_message, decrypted_message)


# def bxor(b1, b2):
#     parts = []
#     for b1, b2 in zip(b1, b2):
#         parts.append(bytes([b1 ^ b2]))
#     return b''.join(parts)


# rek = bxor(b'abc123', b'')
# print(bxor(rek, b''))

manager = EncryptionManager()

plaintexts = [
    b"SHORT",
    b"MEDIUM MEDIUM MEDIUM",
    b"LONG LONG LONG LONG LONG LONG"
]

ciphertexts = []

a = manager.initialize_encryptor(plaintexts[0])
b = manager.initialize_encryptor(plaintexts[1])
c = manager.initialize_encryptor(plaintexts[2])
d = manager.finalize_encryptor(c)
# print(a, b, c, d)

e = manager.initialize_decryptor(b)
f = manager.initialize_decryptor(c)
g = manager.initialize_decryptor(d)
# h = manager.finalize_decryptor(d)
print(f, g)
# res = []

# for i, c in enumerate(ciphertexts):
#     if i == 0:
#         manager.initialize_decryptor(c)
#         continue
#     res.append(manager.update_decryptor(ciphertexts[i - 1], c))

# res.append(manager.finalize_decryptor(ciphertexts[-1]))

# print(res)
