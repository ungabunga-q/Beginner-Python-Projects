"""
Anagram Checker
Checks if two words are anagrams.
"""
def is_anagram(w1, w2):
    return sorted(w1) == sorted(w2)

if __name__ == "__main__":
    w1 = input("Enter first word: ")
    w2 = input("Enter second word: ")
    if is_anagram(w1, w2):
        print("Anagrams!")
    else:
        print("Not anagrams.")
