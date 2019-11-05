from timer import timed
from logger import logged


def fib_recursive(n):
    if n <= 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


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


fib(100)
