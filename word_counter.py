"""
Word Counter
Counts words in a sentence.
"""
def word_count(sentence):
    return len(sentence.split())

if __name__ == "__main__":
    s = input("Enter a sentence: ")
    print(f"Word count: {word_count(s)}")
