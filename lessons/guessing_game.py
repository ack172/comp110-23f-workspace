"""Program that loops until correct number is guessed."""

from random import randint

secret: int = randint(1,10)
guess: int = int(input("Guess a number between 1 and 10: "))

while guess != secret: 
    print("Wrong! ")
    if guess < secret:
        print("too low!")
    else:
        print("Too high!")
    # Ask for a different guess
    guess : int(input("Try again: "))
print("You guessed correctly!")