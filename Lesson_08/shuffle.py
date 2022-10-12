from random import randint

my_list = [1,2,3,4,5,6,7]

def shuffle(my_list):
    index_list = []
    shuffled_list = []
    for i in range (len(my_list)):
        new_var = randint(0, len(my_list) - 1)

        while new_var in index_list:
            new_var = randint(0, len(my_list) - 1)
        index_list.append(new_var)
        shuffled_list.append(my_list[new_var])

    return shuffled_list

print(shuffle(my_list))

        
