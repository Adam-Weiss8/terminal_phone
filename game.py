import random

def guessing_game():
    print("Hello Welcome to the guessing game")
    prompt = "y"
    while prompt is "y":

        print("I'm thinking of a number 1-10... what is it: ")

        num = random.randrange(1,11)
        guess = input()

        if guess is num:
            print("WOW you guessed the number")
        else:
            print(f"NOPE, I was thinking of {num}")

        print("Would you like to play again? (press 'y' to play again or anything else to quit)") 
        prompt = input()
    print("OK Bye lol")




