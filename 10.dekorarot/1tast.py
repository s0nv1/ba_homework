import functools


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwgs):
        s = ', '.join(list(map(str, args)))
        return f'{func.__name__} called with {s}'
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

assert add(4, 5) == "add called with 4, 5"
assert square_all(1, 2, 3, 4) == 'square_all called with 1, 2, 3, 4'
