#!/usr/bin/python3
# Number guess game
# Computer generate a random number and stores it as secrete number
# The player guess the number
# If the guess equals secrete number, the user wins
# If the guess is less than secrete number, the computer give an int "TOO LOW"
# If the guess is greater than secrete number, prints - "TOO HIGH"
# The game take track of number of guesses

import random

MIN_BOUND: int = 1
MAX_BOUND: int = 10

wins_history: list[int] = []


def get_valid_guess(min_val: int, max_val: int) -> int:
    """Prompt user an integer within a specific range and validate it"""
    while True:
        try:
            guess = int(input(f"Enter a guess between {min_val} - {max_val}: "))

            if min_val <= guess <= max_val:
                return guess

            print(f"Out of Bound! Please Enter numbers between {min_val} and {max_val}")

        except ValueError:
            print("Please enter a valid Integer")


def evaluate_guess(guess: int, secret_number: int) -> bool:
    """Compare the guess and secret number and print the hint

    Return True if the guess is correct otherwise False
    """
    if guess == secret_number:
        return True

    if guess < secret_number:
        print("TOO LOW, TRY AGAIN!!")
    else:
        print("TOO HIGH, TRY AGAIN!!")

    return False


def record_wins_history(trials: int) -> None:
    wins_history.append(trials)


def play_game(min_val: int, max_val: int) -> None:
    """Manage the main game loop, tracking trials and running core mechanics"""
    trials: int = 0
    secret_number: int = random.randint(1, 10)

    while True:
        guess = get_valid_guess(min_val, max_val)
        trials += 1

        if evaluate_guess(guess, secret_number):
            print(f"Correct you guessed it in {trials} trials")
            record_wins_history(trials)
            break


if __name__ == "__main__":
    play_game(MIN_BOUND, MAX_BOUND)

