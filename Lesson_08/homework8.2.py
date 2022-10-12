# Write a function that takes in two numbers from the user via input(), 
# call the numbers a and b, and then returns the value of squared a divided 
# by b, construct a try-except block which raises an exception if the two 
# values given by the input function were not numbers, and if value b was zero 
# (cannot divide by zero). 

def calculator():
    a = input("Please enter your number a: ")
    b = input("Please enter your number b: ")
    if a.isdigit() and b.isdigit():
        int_a = int(a)
        int_b = int(b)
        if int_b == 0:
            raise ZeroDivisionError
        else:
            return int_a**2/int_b
    else:
        raise ValueError

result = 0.0

while True:
    try:
        result = calculator()
        break
    except ValueError:
        print("Wrong type, your value should be a digit")
    except ZeroDivisionError: 
        print("You cannot divide on zero")

print(f"The result is: {result}")

