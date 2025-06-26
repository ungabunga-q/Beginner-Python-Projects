"""
Mad Libs Generator
-------------------
This program creates a funny story by filling in blanks with user input.

Steps for Beginners:
1. Define a function for the Mad Libs game.
2. Use input() to get a noun, verb, and adjective from the user.
3. Use an f-string to insert the words into a story template.
4. Print the completed story.
"""

# 1. Define the Mad Libs function
def mad_libs():
    # 2. Get words from the user
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adj = input("Enter an adjective: ")
    # 3. Insert words into the story
    print(f"The {adj} {noun} decided to {verb} today!")

# 4. Main program
if __name__ == "__main__":
    mad_libs()
