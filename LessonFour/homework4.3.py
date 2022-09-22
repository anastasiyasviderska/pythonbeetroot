from random import shuffle
user_word = list(input ("Please enter the word: "))
for i in range (5):
    shuffle(user_word)
    print (''.join(user_word))