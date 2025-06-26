"""
Palindrome Checker
Checks if a string is a palindrome.
"""
def is_palindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    s = input("Enter a string: ")
    if is_palindrome(s):
        print("Palindrome!")
    else:
        print("Not a palindrome.")
