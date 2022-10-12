def local_variable(function_1):
    return function_1.__code__.co_nlocals

def function_01():
    a = 2
    b, c, d = 12, 24, 45

def function_02():
    pass

def function_03():
    pass

print(local_variable(function_01))

print(local_variable(function_02))

print(local_variable(function_03))
