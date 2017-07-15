
from random import *





#Create the list of words you want to choose from.

sides = ["salad", "soup", "fries"]
main = ["pasta", "burger", "pizza"]
dessert=["ice cream", "cake","brownie"]

#Generates a random integer.

x = randint(0, len(sides)-1)
y = randint(0, len(main)-1)
z = randint(0, len(dessert)-1)

print (sides[x])
print (main [y])
print (dessert[z])
