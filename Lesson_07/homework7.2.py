# Create a function called make_country, which takes in a country’s name
# and capital as parameters. Then create a dictionary from those parameters, 
# with ‘name’ and ‘capital’ as keys. Make the function print out the values of
# the dictionary to make sure that it works as intended.

def make_country (name, capital):
    return {'name': name, 'capital': capital}

print(make_country("Slovakia", "Bratislava"))
print (make_country ("Austria", "Vienna"))
