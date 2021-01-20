# Using a while loop with lists and dictionaries

# A for loop is effective for looping through a list, but you shouldn’t modify a list inside a for loop because Python will have trouble keeping track of the items in the list. To modify a list as you work through it, use a while loop. Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and report on later.

# Moving items from one list to another:

# Start with users that need to be verified
# and an empty list to hold confirmed users.
unconfirmedUsers = ["alice", "brian", "candace"]
confirmedUsers = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
# The while loop will run for as long as there are users in the unconfirmedUsers list
while unconfirmedUsers:
    # pop() takes the user off at the end, removing them from the list
    # We store that user in a new variable so we can manipulate them
    currentUser = unconfirmedUsers.pop()
    
    # Printing a statement for the user we took from the unconfirmed list
    print(f"Verifying user: {currentUser.title()}")
    # Once 'confirmed' we append, or add that user to the confirmed list
    confirmedUsers.append(currentUser)
    
# Display all confirmed users.
print("\nThe following users have been confirmed:")
# We loop over the confirmed users list and print them out
for confirmedUser in confirmedUsers:
    print(confirmedUser.title())