#task 2 for lesson 4
name = input ("Please enter your name: ")
age = input ("Please enter your age: ")
if age.isdigit():
    print (f"Hello {name}, on your next birthday you’ll be {int(age)+1} years")
else:
    print ("Your age should have numeric value")
    
