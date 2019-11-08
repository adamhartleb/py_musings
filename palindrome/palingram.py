from load_file import load

dictionary = load('2of4brif.txt')


def find_palingrams(dictionary):
    palingrams = []
    for word_one in dictionary:
        for word_two in dictionary:
            combined = word_one + word_two
            if combined == combined[::-1]:
                palingrams.append(f'{word_one} {word_two}')
    return palingrams


print(find_palingrams(dictionary))
