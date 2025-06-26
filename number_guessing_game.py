"""
Number Guessing Game
The computer randomly selects a number and you try to guess it.
"""

import random

def guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 and 100!")
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    guessing_game()
