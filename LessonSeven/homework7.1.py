#Create a simple function called favorite_movie, which takes a string 
# containing the name of your favorite movie. The function should then 
# print "My favorite movie is named {name}".
def favourite_movie (str):
    print(f"My favourite movie is named {str}")

name = input("Enter the name of your favourite movie: ")
favourite_movie(name)