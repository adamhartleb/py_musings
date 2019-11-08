import sys


def load(file):
    try:
        with open(file) as input_file:
            content = input_file.read().strip().split('\n')
            content = [word.lower() for word in content]
            return content
    except IOError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
