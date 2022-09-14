# task 1 for lesson 3
input_string = input("Enter: ")
if len(input_string) < 2:
    print ("Empty String")
else: 
    print(input_string[:2] + input_string[-2:])

#task 2 for lesson 3
phone_number = input ("Enter your phone number: ")
if len(phone_number) != 10:
    print("Invalid length of numbers please try again")
elif not (phone_number.isnumeric()):
    print ("Invalid format, please try again")
else:
    print ("Your number is valid")

#task #3 for lesson 3
my_name = "ana"
your_name = input ("Enter your name: ")
if your_name.lower() == my_name:
    print ("your name is correct")
else:
    print ("your name is not correct")