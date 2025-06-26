"""
BMI Calculator
Calculates Body Mass Index.
"""
def bmi(weight, height):
    return weight / (height ** 2)

if __name__ == "__main__":
    w = float(input("Enter weight (kg): "))
    h = float(input("Enter height (m): "))
    print(f"Your BMI: {bmi(w, h):.2f}")
