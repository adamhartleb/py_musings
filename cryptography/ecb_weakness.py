from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import sys
import os

secret_key = os.urandom(16)

aes_cipher = Cipher(algorithms.AES(secret_key), modes.ECB(), default_backend())

aes_encryptor = aes_cipher.encryptor()
aes_decryptor = aes_cipher.decryptor()

try:
    with open('image.bmp', 'rb') as image:
        with open('output.bmp', 'wb+') as output:
            # Skip first 54 bytes
            image_data = image.read()
            header, body = image_data[:54], image_data[54:]
            # Pad message
            body += (b'\x00' * (16-len(body) % 16))
            ciphertext = aes_encryptor.update(body)
            output.write(header + ciphertext)
except IOError as err:
    print(err, file=sys.stderr)
    sys.exit(1)
