"""
Random Joke Generator
Prints a random joke from a list.
"""
import random

def tell_joke():
    jokes = [
        "Why did the chicken cross the road? To get to the other side!",
        "I told my computer I needed a break, and it said 'No problem, I'll go to sleep.'",
        "Why do programmers prefer dark mode? Because light attracts bugs!"
    ]
    print(random.choice(jokes))

if __name__ == "__main__":
    tell_joke()
