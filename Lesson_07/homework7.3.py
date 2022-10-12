# Create a function called make_operation, which takes in a simple 
# arithmetic operator as a first parameter (to keep things simple let 
# it only be '+', '-' or '*') and an arbitrary number of arguments (only numbers) 
# as the second parameter. Then return the sum or product of all the numbers in 
# the arbitrary parameter.

def make_operation(operation, first_number, *numbers):
    total = first_number
    for number in numbers:
        if operation == '+':
            total += number
        elif operation == '-':
            total -= number
        elif operation == '*':
            total *= number
        else: 
            print("Wrong parameter")
    return total

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
