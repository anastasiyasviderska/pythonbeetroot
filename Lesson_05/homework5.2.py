# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers
from random import randint
rand_list1 = []
rand_list2 = []
x = 0

while x < 10:
    rand_list1.append(randint(1,10))
    rand_list2.append(randint(1,10))
    x = x + 1
print  (rand_list1, rand_list2)

rand_list1_set = set(rand_list1)
rand_list2_set = set(rand_list2)

result_list = list(rand_list1_set & rand_list2_set)
if (result_list):
    print (result_list)
else:
    print ("No common elements")