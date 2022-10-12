# Make a list that contains all integers from 1 to 100, then find 
# all integers from the list that are divisible by 7 but not a 
# multiple of 5, and store them in a separate list. Finally, print the list.

# Constraint: use only while loop for iteration.

general_list = []
x = 1

while x <= 100:
    general_list.append(x)
    x = x + 1
print (general_list)
result_list = []
y = 0
while y < len(general_list):
    if y % 7 == 0 and y % 5 != 0:
        result_list.append(y)
    y = y + 1

print (result_list)