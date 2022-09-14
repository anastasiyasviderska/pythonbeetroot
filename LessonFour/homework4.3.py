from random import shuffle
user_word = list(input ("Please enter the word: "))
for i in range (5):
    print(f"init {user_word}")
    shuffle(user_word)
    print (''.join(user_word))