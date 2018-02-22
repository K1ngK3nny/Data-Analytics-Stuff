# import the random library
from random import randint

print("Lets play rock paper scissors")

# set list of play options
t = ["Rock", "Paper", "Scissors"]

# assign random play to the computer with options lining up with the above list of options
computer = t[randint(0, 2)]

# set player to false bc when we pass a value to the player, that will make the player True and the value will dictacte what happens next
player = False

# we do a while loop. there is a better way to do this
while player == False:
    player == input("Rock, Paper, Scissors?")
    If player == computer:
        print("Tie")
    elif player == "Rock":
        IF computer == "Paper"
            print("You Lose")
        else:
            print("You Win")
    elif player == "Paper":
        If computer == "Scissors"
            print("You Lose")
        else:
            print("You Win")
    elif player == "Scissors":
        If computer == "Rock"
            print("You Lose")
        else:
            print("You Win")
    else:
        print("Not a valid play, check spelling")

        # set player back to false to continue the game
    player = False
    computer = t[randint(0, 2)]
