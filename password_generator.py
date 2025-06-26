"""
Password Generator
Generates a random password of given length.
"""
import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    print("Generated password:", generate_password(length))
