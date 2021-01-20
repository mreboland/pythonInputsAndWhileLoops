# How input() function works
# The input function pauses your program and waits for the user to enter some text. Once received, the input is assigned to a variable which we can then use.

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# Letting the user choose when to quit a while loop
# We can make a program run as long as the user wants by putting our program in a while loop. We'll define a quit value so the program can be stopped

# Defining a prompt message to send to the user
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. "

# We define message here as an empty string so the while loop has something to compare to initially. If it wasn't there the while loop wouldn't have an initial message to verify so it wouldn't run. We can use an empty string because python allows it to be interpreted.
# message = ""
# while message != 'quit':
#     # As long as message isn't quit, the loop will run forever
#     message = input(prompt)
#     # I added an additional check here because without it, it'll print quit when inputted.
#     if message == 'quit':
#         break
#     else:
#         print(message)
    # There a simpler check as well which came up later in the lesson
    # if message != "quit":
        # print(message)
        
# Using a flag
# For a program that should run only as long as many conditions are true, we can define one variable that determines whether or not the entire program is active. This variable is called a flag, which acts as a signal to the program. The flag is set to true or false for on/off.
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# Here we set the variable active to True, so the program starts in an active state. The program will loop as long as the active variable remains True
active = True
while active:
    # Here we prompt the user and same there answer like before
    message = input(prompt)
    # Here we check to see if input value is quit
    if message == "quit":
        # if so, we change our variable active to False which aborts the program
        active = False
    else:
        # Otherwise print the message
        print(message)