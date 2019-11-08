from load_file import load

dictionary = load('2of4brif.txt')


def find_palindromes(word_list):
    return [word for word in word_list if word == word[::-1]]


print(find_palindromes(dictionary))
