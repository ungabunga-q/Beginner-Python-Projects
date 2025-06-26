def hangman():
"""
Hangman Game
-------------------
Guess the word before you run out of tries.

Steps for Beginners:
1. Import random to pick a word.
2. Define a function for the game logic.
3. Use a list to track guessed letters.
4. Use a while loop for the game turns.
5. Check if the guessed letter is in the word and update the display.
6. Print win/lose message at the end.
"""

# 1. Import random
import random

# 2. Define the game function
def hangman():
    words = ['python', 'hangman', 'challenge', 'program']
    # 3. Pick a random word
    word = random.choice(words)
    guessed = ['_'] * len(word)
    tries = 6
    print(' '.join(guessed))
    # 4. Game loop
    while tries > 0 and '_' in guessed:
        guess = input('Guess a letter: ').lower()
        # 5. Check guess
        if guess in word:
            for i, c in enumerate(word):
                if c == guess:
                    guessed[i] = guess
        else:
            tries -= 1
            print(f'Wrong! Tries left: {tries}')
        print(' '.join(guessed))
    # 6. Print result
    if '_' not in guessed:
        print('You win!')
    else:
        print(f'You lose! The word was {word}.')

# 3. Main program
if __name__ == '__main__':
    hangman()
