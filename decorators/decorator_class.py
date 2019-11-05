class TimedRuns:
    def __init__(self, runs):
        self.runs = runs

    def __call__(self, fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            elapsed_times = []
            for i in range(self.runs):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                elapsed = end - start
                elapsed_times.append(elapsed)
                print(
                    f'Run #{i + 1} for {fn.__name__} took {elapsed} seconds to execute.')
            print(
                f'{fn.__name__} took on average {sum(elapsed_times) / self.runs} seconds to complete.')
        return inner
