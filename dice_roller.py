def roll_dice():

"""
Dice Roller
-------------------
This program simulates rolling a dice and shows the result.

Steps for Beginners:
1. Import the random module to generate random numbers.
2. Define a function roll_dice() that returns a random number between 1 and 6.
3. Use input() to wait for the user to press Enter before rolling the dice.
4. Print the result using an f-string.
"""

# 1. Import the random module
import random

# 2. Define a function to roll the dice
def roll_dice():
    # random.randint(1, 6) returns a random integer from 1 to 6 (inclusive)
    return random.randint(1, 6)


# 3. Main program starts here
if __name__ == "__main__":
    # Wait for user input before rolling
    input("Press Enter to roll the dice...")
    # 4. Print the result
    print(f"You rolled: {roll_dice()}")
