# While loops
# The for loop takes a collection of items and executes a block of code once for each item in the collection. A while loop runs as long as, or while, a certain condition is true.
# An example of counting to 5:
# We set a counter, currentNumber to 1 to have a start for our count
# currentNumber = 1

# # While currentNumber is less than or equal to 5 this will loop until it hits 5
# while currentNumber <= 5:
#     # Print the number
#     print(currentNumber)
#     # Increase currentNumber by 1 to increase the count. It's the same as currentNumber = currentNumber + 1
#     currentNumber += 1
    
# Using continue in a loop
# Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of the loop based on the result of a conditional test.

# We set an initial variable so we can enter into the while loop
currentNumber = 0

# While our variable is less than 10, loop
while currentNumber < 10:
    # Increment our variable
    currentNumber += 1
    
    # If our variable is divisible by 2 with no remainder (2, 4, 6, 8...)
    if currentNumber % 2 == 0:
        # continue with the rest of the program
        continue
    
    # Print the numbers that aren't divisible by 2 (1, 3, 5...)
    print(currentNumber)
    
# Avoiding infinite loops
x = 1
while x <= 5:
    print(x)
    # If we omit the line below, it'll cause the program to loop for ever as the counter will never reach 5. In those cases we have to abort in the terminal by using ctrl + c or you can just close it. Test properly and frequently in order to avoid those kinds of issues.
    x += 1

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

prompt = "\nPlease enter a topping to add to your pizza"
prompt += "\nEnter quit when you are done. "

while True:
    message = input(prompt)
    
    if message == "quit":
        break
    
    message = f"\nAdding {message.title()}"
    print(message)


# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free if they are between 3 and 12, the ticket is $10 and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

prompt = "\nPlease enter your age."
prompt += "\nEnter quit to exit. "

while True:
    # Leaving age as string so we can quit the program
    age = input(prompt)
    
    if age == "quit":
        break
    
    # If input is no 'quit' then we convert it to an int so we can do comparisons
    age = int(age)
    # comparisons
    if age < 3:
        print("Your ticket is free")
    elif age >= 3 and age < 12:
        print("You're ticket is $10")
    elif age >= 12:
        print("Your ticket is $15")
        
# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.

# prompt = "\nPlease enter a topping to add to your pizza"
# prompt += "\nEnter quit when you are done. "

# message = ""
# while message != "quit":
#     message = input(prompt)
    
#     if message != "quit":
#         print(f"Adding: {message.title()}")

# • Use an active variable to control how long the loop runs.

# prompt = "\nPlease enter a topping to add to your pizza"
# prompt += "\nEnter quit when you are done. "

# active = True
# while active:
#     message = input(prompt)

#     if message == "quit":
#         active = False
#     else:
#         print(f"Adding: {message.title()}")       
    
# • Use a break statement to exit the loop when the user enters a 'quit' value.

prompt = "\nPlease enter a topping to add to your pizza"
prompt += "\nEnter quit when you are done. "


while True:
    message = input(prompt)

    if message == "quit":
        break
    else:
        print(f"Adding: {message.title()}")


# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)

# x = 0
# while x <= 100:
#     print(x)
