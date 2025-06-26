"""
Age Calculator
Calculates age from birth year.
"""
from datetime import date

def calculate_age(birth_year):
    current_year = date.today().year
    return current_year - birth_year

if __name__ == "__main__":
    year = int(input("Enter your birth year: "))
    print(f"Your age: {calculate_age(year)}")
