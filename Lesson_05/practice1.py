#You have a first list like values = [“one”, “two”, “three”, “four”, “five”] and a 
# second list indexes [1, 3, 5]. You need to remove elements from first list which have an 
# indexes from a second.

values = ['one', 'two', 'three', 'four', 'five', 'six']
my_list = [0, 5, 3, 1, 5]

print(list(enumerate(values)))

print([value for index, value in enumerate(values) if index not in my_list]) 
new_values = []

for index in range(len(values)):
    if  not index in my_list:
        new_values.append(values[index])

print(new_values)
