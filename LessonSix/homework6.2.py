#Create a function which takes as input two dicts with structure mentioned above, 
# then computes and returns the total price of stock.
from collections import Counter
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total = 0.0

for product in stock:
    total += prices [product] * stock [product]
    
print (total)

