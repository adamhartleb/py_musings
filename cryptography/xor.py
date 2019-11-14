from os import urandom
random_string = b"abcefghijklmnopq"
random_data = urandom(16)

for idx, letter in enumerate(random_string):
    xord = letter ^ random_data[idx]
    print(chr(xord), end='')

print(' ')

for idx, letter in enumerate(random_string):
    xord = letter ^ random_data[idx]
    print(chr(xord ^ random_data[idx]), end='')
