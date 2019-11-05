def timed(fn):
    # Allows the decorator to be used in modules that don't
    # import these modules themselves.
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        print(f'{fn.__name__} took {elapsed} seconds to execute.')
        return result

    return inner


def fib_recursive(n):
    if n <= 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# This is necessary to prevent the decorator from being logged for every recursive call.
@timed
def call_fib_recursive(n):
    return fib_recursive(n)


@timed
def fib(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b


print(fib(1000))
