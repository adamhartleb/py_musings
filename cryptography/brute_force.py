def generate(alphabet, max_len):
    if max_len <= 0:
        return
    for c in alphabet:
        yield c
    for c in alphabet:
        for next in generate(alphabet, max_len-1):
            yield c + next


def timed(runs):
    from time import perf_counter
    elapsed_times = []

    def decorated(fn):
        def inner(arg, hash_fn):
            for i in range(runs):
                start = perf_counter()
                result = fn(arg, hash_fn)
                elapsed = perf_counter() - start
                elapsed_times.append(elapsed)
            print(
                f'Average execution time for {hash_fn} was {sum(elapsed_times) / len(elapsed_times)} seconds')
        return inner

    return decorated


@timed(10)
def find_hash(word: str, hash_fn: str):
    from string import ascii_lowercase
    from hashlib import md5, sha1, sha256
    word = word.lower()
    registry = {
        'md5': md5,
        'sha1': sha1,
        'sha256': sha256
    }

    if hash_fn not in registry:
        raise ValueError('Hash function options: md5, sha1, or sha256')

    hashed_word_to_find = registry[hash_fn](bytes(word, 'utf-8')).hexdigest()

    for permutation in generate(ascii_lowercase, len(word)):
        hashed_permutation = registry[hash_fn](
            bytes(permutation, 'utf-8')).hexdigest()
        if hashed_permutation == hashed_word_to_find:
            return True
    raise ValueError('Something went wrong.')


find_hash('zzzz', 'md5')
find_hash('zzzz', 'sha1')
find_hash('zzzz', 'sha256')
