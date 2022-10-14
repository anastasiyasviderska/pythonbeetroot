def arg_rules(type_: type, max_length: int, contains: list):
    def wrapped_function(func):
        def wrapper(arg):
            if not type(arg) is type_:
                print(f"Wrong type: {str(type(arg))} should be {type_}")
                return False
            if len(arg) > max_length:
                print(f"Wrong len: {len(arg)} > {max_length}")
                return False
            for string in contains:
                if not string in arg:
                    print(f"Argument must contain {string}")
                    return False
            return func(arg)
        return wrapper
    return wrapped_function



@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
assert create_slogan(5) is False
assert create_slogan ('aaaaaaaaaaaaaa') is False