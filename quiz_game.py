"""
Quiz Game
Simple multiple-choice quiz.
"""
questions = [
    ("What is the capital of Italy?", "Rome"),
    ("What is 5 * 6?", "30"),
    ("What is the color of grass?", "Green")
]

def quiz():
    score = 0
    for q, a in questions:
        ans = input(q + " ")
        if ans.strip().lower() == a.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer is {a}.")
    print(f"Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz()
