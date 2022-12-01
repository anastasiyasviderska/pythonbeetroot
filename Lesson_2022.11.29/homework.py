test_list = [3, 4, [5, 2, 1, [23, 9], 8], [4, 87], 17, 16, [3, 5, [[34]]]]


def normal_max(list_parameter):
    max_num = list_parameter[0]
    for elem in list_parameter[1:]:
        if elem > max_num:
            max_num = elem
    return max_num


def recursive_max(list_parameter):
    max_num = 0
    for elem in list_parameter:
        if type(elem) is int:
            if elem > max_num:
                max_num = elem
        elif type(elem) is list:
            function_value = recursive_max(elem)
            if function_value > max_num:
                max_num = function_value
    return max_num

def print_hierarchy(list_parameter: list, prefix: str):
    for item in list_parameter:
        if type(item) is int:
            print(f"{prefix}{item}")
        elif type(item) is list:
            print_hierarchy(item, prefix + ' |  ')




print(recursive_max(test_list))
print_hierarchy(test_list," |  ")