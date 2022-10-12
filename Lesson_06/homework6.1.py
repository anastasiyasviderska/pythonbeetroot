#Make a program that has some sentence (a string) on input and returns a dict containing 
# all unique words as keys and the number of occurrences as values. 

input_string = "Jan Feb March Feb Jan Jan April May Jan"

def word_count(str):
    counts = dict()
    words = str.split(" ")

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_count(input_string))

