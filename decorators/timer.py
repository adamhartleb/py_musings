def timed(fn):
    # Allows the decorator to be used in modules that don't
    # import these modules themselves.
    from time import perf_counter

    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        print(f'{fn.__name__} took {elapsed} seconds to execute.')
        return result

    return inner


def timed_runs(runs):
    from time import perf_counter

    def timed(fn):
        def inner(*args, **kwargs):
            elapsed_times = []
            for i in range(runs):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                elapsed = end - start
                elapsed_times.append(elapsed)
                print(
                    f'Run #{i + 1} for {fn.__name__} took {elapsed} seconds to execute.')
            print(
                f'{fn.__name__} took on average {sum(elapsed_times) / runs} seconds to complete.')
        return inner
    return timed
