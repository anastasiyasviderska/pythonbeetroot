to_do_list = input("To do list: ").split(",")
to_do_list = list(set(item.strip()for item in to_do_list))

user_input = input ("Check an item from your list: ")
while True:
    done_in_input = "- done" in user_input
    add_in_input = "- add" in user_input
    if done_in_input:
        clear_user_input = user_input.replace("- done", "")
        to_do_list.remove(clear_user_input)
    elif add_in_input:
        clear_user_input = user_input.replace("- add", "")
        to_do_list.append(clear_user_input)
        to_do_list = list(set(to_do_list))
    if len(to_do_list) < 1:
        break
    to_do_list.sort()
    print_thingy = ', '.join(to_do_list)
    print(f"Left for today: {print_thingy}")
    user_input = input("Check an item from your list: ")
print ("Good job!")

