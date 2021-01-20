# The modulo operator (%)
# The operator divides one number by another and returns the remainder
# 4 % 3 = 1
# 5 % 3 = 2

# The operator doesn't tell you how many times one number fits into another, it's just the remainder
# When the 2 numbers are divisible, the remainder is 0. We can use this fact to determine in a number is even or odd.
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

# The modulo here says that if the remainder of our number, when divided by 2 is 0, it's even, else odd ( 10 / 2 has no remainder, 9 / 2 does).
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
    
# 7-1. Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”

rentalCar = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {rentalCar.title()}")

# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

dinners = input("Hello, how many people are in your group? ")
dinners = int(dinners)

if dinners > 8:
    print("\nMy apologies, there will be a bit of a wait")
else:
    print("\nYour table is right this way")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

multiple = int(input("Please enter a number "))

if multiple % 10 == 0:
    print("That is a multiple of 10")
else:
    print("That is not a multiple of 10")

