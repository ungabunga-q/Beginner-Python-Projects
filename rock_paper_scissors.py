def play():
"""
Rock Paper Scissors Game
-------------------
Play the classic game against the computer.

Steps for Beginners:
1. Import the random module to let the computer choose.
2. Define a function to play the game.
3. Get the user's choice with input().
4. Use random.choice to pick for the computer.
5. Compare choices and print the result.
"""

# 1. Import random
import random

# 2. Define the game function
def play():
    choices = ['rock', 'paper', 'scissors']
    # 3. Get user input
    user = input("Choose rock, paper, or scissors: ").lower()
    # 4. Computer randomly chooses
    comp = random.choice(choices)
    print(f"Computer chose: {comp}")
    # 5. Decide winner
    if user == comp:
        print("It's a tie!")
    elif (user == 'rock' and comp == 'scissors') or (user == 'paper' and comp == 'rock') or (user == 'scissors' and comp == 'paper'):
        print("You win!")
    else:
        print("You lose!")

# 3. Main program
if __name__ == "__main__":
    play()
