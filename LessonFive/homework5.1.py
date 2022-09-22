# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

from random import randint
rand_list = []
x = 0

while x < 10:
    rand_list.append(randint(1,10))
    x = x + 1
    
print(rand_list)
print(max(rand_list))