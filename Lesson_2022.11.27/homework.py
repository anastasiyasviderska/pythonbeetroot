from random import randint
from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

def password_generator(length: int) -> int:
    min_pass = 0
    max_pass = 10 ** length - 1
    value = randint(min_pass, max_pass)
    print(f'min: {min_pass}, max: {max_pass}, value: {value}')
    return value
    

@timeit
def password_hacker(generated_password: int):
    temp_password = 0
    while generated_password != temp_password:
        temp_password += 1



password_hacker(password_generator(4))
password_hacker(password_generator(5))
password_hacker(password_generator(6))
password_hacker(password_generator(7))
password_hacker(password_generator(8))
