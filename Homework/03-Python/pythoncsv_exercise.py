# import the random library
import random

print("Lets play rock paper scissors" )

# specify three options
options = ["r", "p", "s"]

# computer choice
computer_choice = random.choice(options)

# user choice
user_choice = input("Make your Choice: (r)ock, (p)aper,(s)cissors? ")
