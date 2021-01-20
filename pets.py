# Removing all instances of specific values from a list
# Using remove() only removes the first instance of the value we want removed. If we want to remove all of them, we can use a while loop to accomplish it
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# The while loop will keep running until all cats have been removed from the list.
while "cat" in pets:
    pets.remove("cat")
    
print(pets)