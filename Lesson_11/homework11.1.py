def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} called with {', '.join(map(str, args))}")
        return func(*args)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

assert add(5, 7) == 12
assert square_all(1, 2, 3, 4, 5) == [1, 4, 9, 16, 25]
