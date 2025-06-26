"""
Flashcard Quiz
Simple quiz app for learning.
"""
questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What color is the sky?": "Blue"
}

def quiz():
    score = 0
    for q, a in questions.items():
        answer = input(q + " ")
        if answer.strip().lower() == a.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer is {a}.")
    print(f"Quiz finished! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz()
