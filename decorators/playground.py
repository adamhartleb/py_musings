from timer import timed, timed_runs
from logger import logged
from memoizer import memoize_fib
from decorator_class import TimedRuns


@memoize_fib
def fib_recursive(n):
    if n <= 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_recursive_memo(n):
    cache = {1: 1, 2: 2}

    def calc_fib(n):
        if n not in cache:
            cache[n] = calc_fib(n-1) + calc_fib(n - 2)
        return cache[n]

    return calc_fib(n)


# This is necessary to prevent the decorator from being logged for every recursive call.
@timed
def call_fib_recursive(n):
    return fib_recursive(n)


# Decorator stacking
@logged
@timed
def fib(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b


# @timed
# def call_fib_recursive_memo(n):
#     return fib_recursive_memo(n)

# @timed_runs(10)
# def call_fib_recursive_memo(n):
#     return fib_recursive_memo(n)

@TimedRuns(10)
def call_fib_recursive_memo(n):
    return fib_recursive_memo(n)


call_fib_recursive_memo(600)
