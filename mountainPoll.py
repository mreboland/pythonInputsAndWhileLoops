# Filling a dictionary with user input

# First we define an empty dictionary for use to store values in later based on user input
responses = {}

# Set a flag to indicate that polling is active
pollingActive = False

while pollingActive:
    # Prompt for the users name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # Store the responses in the dictionary
    responses[name] = response
    
    # Find out if anyone else is going to take the poll.
    # If user enters 'yes' it maintains the True status for pollingActive so the loop runs again
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == "no":
        pollingActive = False
        
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
# Loop over the key and value pairs in the responses dictionary in order to print them out.
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")
    
# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of # various sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.

sandwichOrders = ["blt", "montreal", "cold cut"]
finishedSandwiches = []

while sandwichOrders:
    makingOrder = sandwichOrders.pop()
    
    print(f"We are currently making your {makingOrder} sandwich")
    finishedSandwiches.append(makingOrder)
    
for meal in finishedSandwiches:
    print(f"We've finish your {meal} sandwich")

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.
sandwichOrders = ["pastrami", "blt", "montreal",
                  "pastrami", "cold cut", "pastrami"]
finishedSandwiches = []

print("\nUnfortunately we have run out of pastrami sandwiches")
while sandwichOrders:
    while "pastrami" in sandwichOrders:
        sandwichOrders.remove("pastrami")
    
    makingOrder = sandwichOrders.pop()

    print(f"We are currently making your {makingOrder} sandwich")
    finishedSandwiches.append(makingOrder)

for meal in finishedSandwiches:
    print(f"We've finish your {meal} sandwich")


# 7-10. Dream Vacation: Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.

# Empty dict to save user data too
dreamVacation = {}

# To keep loop active
pollActive = True
# Looping
while pollActive:
    # Get user info
    userName = input("\nHello, what is your name? ")
    destination = input("Where would you like to travel to? ")
    
    # Saving user data to dictionary
    dreamVacation[userName] = destination
    
    # Prompt user if they want to let someone else poll or not
    nextUser = input("\nWould you like to let another user poll? (yes/no) ")
    if nextUser == "no":
        pollActive = False
        
for key, value in dreamVacation.items():
    print(f"{key.title()} would love to travel to {value.title()}")
    
