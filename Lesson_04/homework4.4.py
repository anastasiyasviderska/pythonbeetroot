from random import randint
number1 = randint(1, 20) 
number2 = randint(1, 20) 
math_expression = number1 + number2
user_guess = input(f"Enter your answer {number1} + {number2}: ")
if user_guess == str(math_expression):
    print ("Your answer is correct")
else:
    print("Your answer is wrong")
