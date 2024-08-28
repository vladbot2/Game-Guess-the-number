import random

def guessTheNumber():
    lowerBound = 1
    upperBound = 100

    numberToGuess = random.randint(lowerBound, upperBound)
    
    attempts = 10

    print(f"I've picked a number between {lowerBound} and {upperBound}. Try to guess it within {attempts} attempts")

    for attempt in range(1, attempts + 1):
        userGuess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if userGuess < numberToGuess:
            print("The number is higher.")
        elif userGuess > numberToGuess:
            print("The number is lower.")
        else:
            print(f" You guessed the number {numberToGuess} in {attempt} attempts")
            break
    else:
        print(f" you didn't guess it. The number was {numberToGuess}.")

guessTheNumber()
