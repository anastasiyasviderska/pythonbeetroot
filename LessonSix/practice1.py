list_of_bombs = [
    [0, 1, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]
[x, y] = [int(i) for i in input('Enter your values here: ').split(',')]
counter = 0
while True:
    if list_of_bombs [x- 1] [y - 1]:
        print ("You loose")
        break
    elif counter == 1:
        print ("You win")
        break
    else:
        counter += 1
    [x, y] = [int(i) for i in input('Enter your values here: ').split(',')]