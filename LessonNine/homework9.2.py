from sys import argv
import json

def menu():
    print("1. Add new entries\n2. Search by first name\n3. Search by last name\n4. Search by full name\n5. Search by telephone number\n6. Search by city or state\n7. Delete a record for a given telephone number\n8. Update a record for a given telephone number\n9. An option to exit the program")

def read_phonebook(pb_path):
    try:
        with open (pb_path) as file_object:
            pb = json.load(file_object)
        return pb
    except FileNotFoundError:
        with open (pb_path, 'w') as file_object:
            json.dump([], file_object)
            file_object.close()
        return []

def operation_add(pb_path):
    card = {}
    card ['first_name'] = input("First Name: ")
    card ['last_name'] = input("Last Name: ")
    card ['phone_num'] = input("Phone Number: ")
    card ['city'] = input ("City: ")
    card ['state'] = input ("State: ")
    my_list = read_phonebook(pb_path)
    my_list.append(card)
    with open (pb_path, 'w') as file_object:
        json.dump(my_list, file_object)
        file_object.close()
    return my_list

def operation_search_by_firstname(pb_path):
    my_list = read_phonebook(pb_path)
    first_name = input("First Name: ")
    return list(filter(lambda card: card['first_name'] == first_name, my_list))

def operation_search_by_lastname(pb_path):
    my_list = read_phonebook(pb_path)
    last_name = input("Last Name: ")
    return list(filter(lambda card: card['last_name'] == last_name, my_list))

def operation_search_by_fullname(pb_path):
    my_list = read_phonebook(pb_path)
    full_name = input("Full Name: ")
    return list(filter(lambda card: card['first_name'] + " " + card['last_name'] == full_name, my_list))    

def operation_search_by_phone(pb_path):
    my_list = read_phonebook(pb_path)
    phone_number = input("Phone Number: ")
    return list(filter(lambda card: card['phone_num'] == phone_number, my_list))

def operation_search_by_city_state(pb_path):
    my_list = read_phonebook(pb_path)
    city_or_state = input("Enter City or State: ")
    return list(filter(lambda card: card['city'] == city_or_state or card['state'] == city_or_state, my_list))

def operation_delete_by_phone(pb_path):
    my_list = read_phonebook(pb_path)
    phone = input("Enter a Phone to delete an Entry: ")
    filtered_phonebook = list(filter(lambda card: card['phone_num'] != phone, my_list))
    with open (pb_path, 'w') as file_object:
        json.dump(filtered_phonebook, file_object)
        file_object.close()
    return filtered_phonebook

def operation_update_by_phone(pb_path):
    my_list = read_phonebook(pb_path)
    phone = input("Enter a Phone to update an Entry: ")
    for card in my_list:
        if card['phone_num'] == phone:

            first_name = input(f"Update First Name ({card ['first_name']}): ")
            if first_name != "":
                card ['first_name'] = first_name

            last_name = input(f"Update Last Name ({card ['last_name']}): ")
            if last_name != "":
                card ['last_name'] = last_name

            phone_num = input(f"Update Phone Number ({card ['phone_num']}): ")
            if phone_num != "":
                card ['phone_num'] = phone_num

            city = input(f"Update City ({card ['city']}): ")
            if city != "":
                card ['city'] = city

            state = input(f"Update State ({card ['state']}): ")
            if state != "":
                card ['state'] = state

    with open (pb_path, 'w') as file_object:
        json.dump(my_list, file_object)
        file_object.close()
    return my_list         

def operation_exit():
    print ("The phonebook is closing now")
    exit()

def print_cards(my_list):
    print("------------------------------------------------------------------------------")
    for card in my_list:
        str = "| " + '{0: <33}'.format(card['first_name'] + " " + card['last_name'])
        str += '{0: <19}'.format(" : " +card['phone_num'])
        str += " : " + card['city'] + ", " + card['state']
        print(str)
    print("------------------------------------------------------------------------------")

try:
    phonebook_path = argv[1]
    print_cards(read_phonebook(phonebook_path))
    menu()
except IndexError:
    print ("Using: python3 homework9.1.2 <Phonebook.json>")
    exit


while True:
    try:
        selected_menu = int(input("Enter your number from 1 to 9: "))
        match selected_menu:
            case 1:
                print_cards(operation_add(phonebook_path))
            case 2:
                print_cards(operation_search_by_firstname(phonebook_path))
            case 3:
                print_cards(operation_search_by_lastname(phonebook_path))
            case 4:
                print_cards(operation_search_by_fullname(phonebook_path))
            case 5:
                print_cards(operation_search_by_phone(phonebook_path))
            case 6:
                print_cards(operation_search_by_city_state(phonebook_path))
            case 7:
                print_cards(operation_delete_by_phone(phonebook_path))
            case 8:
                print_cards(operation_update_by_phone(phonebook_path))
            case 9:
                operation_exit()
    except ValueError:
        menu()

