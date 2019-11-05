def memoize_fib(fib):
    cache = {1: 1, 2: 2}

    def inner(n):
        if n not in cache:
            cache[n] = fib(n-1) + fib(n - 2)
        return cache[n]

    return inner
