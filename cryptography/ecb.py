from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

test_key = bytes.fromhex('00112233445566778899AABBCCDDEEFF')

aes_cipher = Cipher(algorithms.AES(test_key), modes.ECB(), default_backend())
aes_encryptor = aes_cipher.encryptor()
aes_decryptor = aes_cipher.decryptor()

message = b"""
FROM: FIELD AGENT ALICE
TO: FIELD AGENT BOB
RE: Meeting
DATE: 2001-1-1

Meet me today at the docks at 2300."""

# Padding the message. If it isn't padded, the plaintext message will be incomplete.
message += (b'E' * (-len(message) % 16))
ciphertext = aes_encryptor.update(message)
print(ciphertext)
plaintext = aes_decryptor.update(ciphertext)
print(plaintext)
