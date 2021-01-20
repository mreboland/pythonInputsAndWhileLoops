# Everytime you use input() you should include a clear message so the user knows exactly what to provide
# name = input("Please enter your name: ")
# print(f"\nHellow, {name}!")

# Sometimes you'll want to write a prompt that's longer than one line. You can do this by assigning our prompt to a viable and pass that variable to the input function
prompt = "If you tell us who you are, we can personalize the mssages you see."
# the += takes the string that was assigned to prompt and adds the new string onto the end. Same as doing prompt = prompt + "\nWhat is your first name? "
prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"\nHello, {name}!")

# Using int() to accept numerical input
# While using input(), python interprets everything as a string. This becomes an issue when using numbers.
# age = input("How old are you? ")
# The value stored in age is a string "" and not a number
# print(age)
# As proof, if we input an age less than 18 it'll result in a type error saying there's no support between a 'str' and an 'int'
# print(age >= 18)

# To get around the issue we use int()
age = input("How old are you? ")
# Using int() here converts the number from a string to an integer
age = int(age)
# The below will print true or false now depending on age inputted
print(age >= 18)