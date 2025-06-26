"""
Text-Based Adventure Game
A simple interactive story game.
"""
def start_game():
    print("Welcome to the Adventure Game!")
    print("You are in a dark forest. There is a path to the left and right.")
    choice = input("Which way do you go? (left/right): ")
    if choice == "left":
        print("You find a treasure chest! You win!")
    elif choice == "right":
        print("You meet a dragon and run away! Game over.")
    else:
        print("Invalid choice. The adventure ends.")

if __name__ == "__main__":
    start_game()
