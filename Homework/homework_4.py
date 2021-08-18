import random
import math



games = []
guesses = []
playing = True
userChoice = 0

while playing:
    initChoice = int(input("\nChoose a MAXIMUM number: "))
    tries = math.floor(math.log2(initChoice))
    randomNum = random.randint(1,initChoice)
    print(f"Guess a number between 1 and {initChoice}. Try to guess it in {tries} tries!")

    while userChoice != randomNum:
        try:
            userChoice = input("Guess a number: ")
            userChoice = int(userChoice)

            guesses.append(userChoice)

            if userChoice < randomNum:
                print("\tToo Low. Guess Again")
            elif userChoice > randomNum:
                print("\tToo High. Guess Again")
            else:
                congrats = ("\tGood job. You win!")
                print(congrats)

                games.append(congrats.count('w'))
        except:
            print("Choose a valid number")

    print(f"The number was {userChoice}")
    print("It took you", len(guesses), "tries.")
    print("Your guesses were:", guesses)
    print("You've played", len(games), "game/s with an average of * guesses per game")

    playAgain = input("Play Again: (y/n)")
    if playAgain == 'n':
        print("Your best game took * guesses and your worst game needed * guesses")
        print("Thanks for playing")
        exit()
    else:
        continue