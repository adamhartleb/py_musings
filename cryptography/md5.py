from hashlib import md5

with open('test.txt', 'rb') as file:
    contents = file.read()
    md5hasher = md5()
    md5hasher.update(contents)
    print(md5hasher.hexdigest())
