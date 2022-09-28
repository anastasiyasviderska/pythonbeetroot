user_input = input("Enter your value: ")

def some_function (argument):
    try:
        user_input_int = int(user_input)
        return 1/user_input_int
    except ValueError:
        print("Your input is incorrect, use an int")
    except ZeroDivisionError:
        print("You cannot divide on zero, try another number")

print(some_function(user_input))

    

