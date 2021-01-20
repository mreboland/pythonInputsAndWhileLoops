# Using break to exit a loop
# To exist a while loop immediately without running any remaining code, regardless of results or condition tests, use break.
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

# A loop that starts with 'while True' will run forever unless it reaches a break statement.
while True:
    city = input(prompt)
    
    if city == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# As a note, we can use the break statement in any of Python’s loops. For example, we could use break to quit a for loop that’s working through a list or a dictionary.
