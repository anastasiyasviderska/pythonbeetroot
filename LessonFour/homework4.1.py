#task 1 for lesson 4
from random import randint
generated_number = str(randint(1, 10))
user_number = input("Guess the number: ")
if generated_number == user_number:
    print ("Your guess is correct")
else:
    print(f"You are wrong the number is {generated_number}")


