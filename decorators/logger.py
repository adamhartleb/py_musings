def logged(fn):
    from datetime import datetime, timezone

    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        print(f'{fn.__name__} called at {run_dt}')
        result = fn(*args, **kwargs)
        return result

    return inner
