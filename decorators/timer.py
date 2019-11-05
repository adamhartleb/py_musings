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
