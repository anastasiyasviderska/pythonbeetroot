def recursion (my_index):
    if my_index >= 10:
        return 1
    return recursion(my_index + 1) + 1

print("results", recursion(0))
    