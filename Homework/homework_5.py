import random

def first_roll():
    one = random.randint(1,6)
    two = random.randint(1,6)
    dice = one + two
    print("\nFirst Roll:")
    print(f"You rolled a {dice}. Die faces were {one} and {two}")
    point.append(dice)
    if dice == 7 or dice == 11:
        print("You Win!")
    elif dice == 2 or dice == 3 or dice == 12:
        print("You Lose!")


def next_roll():
    one = random.randint(1,6)
    two = random.randint(1,6)
    dice = one + two
    print(f"You rolled a {dice}. Die faces were {one} and {two}")
    if dice != point[0]:
        print(input("Press enter to roll again"))
        next_roll()
    elif dice == 7:
        print("You Lose")
    else:
        print("You Win!")
        play_again2 = input("\nYou won! Do you want to play again: (y/n)")
        if play_again2 == 'y':
            point.pop()
            first_roll()
        else:
            exit()

#-------------------------------------------------------------------------------

point = []
dice = 0


print("\nLet's Play Craps!")
print(input("Press enter to roll the dice!"))

first_roll()

while dice != point[0]:
    if point[0] == 2 or point[0] == 3 or point[0] == 12:
        play_again = input("\nYou lost! But you can always play again: (y/n)")
        if play_again == 'n':
            exit()
        else:
            point.pop()
            first_roll()
    elif point[0] == 7 or point[0] == 11:
        play_again2 = input("\nYou won! Do you want to play again: (y/n)")
        if play_again2 == 'n':
            exit()
        else:
            point.pop()
            first_roll()
    else:
        print(f"\nOn the next turn, you'll need to roll a {point[0]} to win.")
        print(input("Press enter for next roll"))
        next_roll()





# Play by rolling two six-sided dice. 
# If you get a 7 or 11 on the first roll you win! 
# If you get a 2, 3, or 12 on the first roll then you lose. 
# Otherwise, what ever you roll becomes your "point". 
# You'll keep rolling the dice until you roll either a 7 or your point. 
# If you roll a 7, you lose. If you roll your point, you win the game