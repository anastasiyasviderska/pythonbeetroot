def function_main(function_name):
    def function_a():
        return 'a'

    def function_b():
        return 'b'

    def function_c():
        return 'c'

    def function_fail():
        return 'fail'
        
    if function_name == 'a':
        return function_a
    elif function_name == 'b':
        return function_b
    elif function_name == 'c':
        return function_c
    else:
        return function_fail

print(function_main('c')())
print(function_main('b')())
print(function_main('a')())
print(function_main('f')())