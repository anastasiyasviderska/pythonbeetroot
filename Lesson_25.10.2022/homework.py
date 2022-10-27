# Password Generator
# #     1.    Password length should be from 4 to 16 symbols
# #     2.    The following options should be available for the user:
# # -  latin alphabet, upper case letters, lower case letters, punctuation symbols
# the response can be Y/N (possible usage y/n and Y/N)
#        3. Based on the given bass the password is generated randomly and given to the user

from random import choices
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

def question_generator(input_str: str, generator_values: str) -> str:
    while True:
        use_lowercase = input(input_str)
        if use_lowercase == 'y':
            return generator_values
        elif use_lowercase == 'n':
            return ''
        else:
            print('Please type y or n! :(')

def password_generator() -> str:
    length = 0
    while length < 4 or length > 16:
        length = input('How long do you want the password to be? (4 - 16 characters): ')
        if length.isdigit():
            length = int(length)
        else:
            length = 0

    password_alphabet = ''
    while True:
        password_alphabet += question_generator('Do you want to use lowercase letters?(y/n): ', ascii_lowercase)
        password_alphabet += question_generator('Do you want to use uppercase letters?(y/n): ', ascii_uppercase)
        password_alphabet += question_generator('Do you want to use digits?(y/n): ', digits)
        password_alphabet += question_generator('Do you want to use symbols?(y/n): ', punctuation)

        if password_alphabet == '':
            print("Please select something")
        else:
            password = ''.join(choices(password_alphabet, k=length))
            return password


print (password_generator())

