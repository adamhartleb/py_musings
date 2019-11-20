from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

key = os.urandom(32)
iv = os.urandom(16)

aes_cipher = Cipher(algorithms.AES(key), modes.CBC(iv),
                    backend=default_backend())
aes_encryptor = aes_cipher.encryptor()
aes_decryptor = aes_cipher.decryptor()

padder = padding.PKCS7(128).padder()
unpadder = padding.PKCS7(128).unpadder()

plaintexts = [
    b"SHORT",
    b"MEDIUM MEDIUM MEDIUM",
    b"LONG LONG LONG LONG LONG LONG",
]

print(padder.update(
    plaintexts[0] + plaintexts[1] + plaintexts[2]) + padder.finalize())

ciphertexts = []

for p in plaintexts:
    padded = padder.update(p)
    ciphertexts.append(aes_encryptor.update(padded))

print(ciphertexts)
ciphertexts.append(aes_encryptor.update(padder.finalize()))
print(ciphertexts)

for c in ciphertexts:
    padded_message = aes_decryptor.update(c)
    print(unpadder.update(padded_message))

print(unpadder.finalize())
