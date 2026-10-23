#!/usr/bin/python3
# Number guess game
# Computer generate a random number and stores it as secrete number
# The player guess the number
# If the guess equals secrete number, the user wins
# If the guess is less than secrete number, the computer give an int "TOO LOW"
# If the guess is greater than secrete number, prints - "TOO HIGH"
# The game take track of number of guesses

import random

MIN: int = 1
MAX: int = 10

trials: int = 0
secrete_number: int = random.randint(MIN, MAX)

while True:
    guess: int = int(input(f"Enter a guess between {MIN} - {MAX}: "))
    trials += 1

    if guess == secrete_number:
        print(f"Correct you guessed it in {trials} trials")
        break
    elif guess < secrete_number:
        print("TOO LOW, TRY AGAIN!")
    elif guess > secrete_number:
        print("TOO HIGH, TRY AGAIN")

