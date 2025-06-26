"""
Tip Calculator
Calculates tip based on bill and percentage.
"""
def calculate_tip(bill, percent):
    return bill * percent / 100

if __name__ == "__main__":
    bill = float(input("Enter bill amount: "))
    percent = float(input("Enter tip percentage: "))
    print(f"Tip: {calculate_tip(bill, percent):.2f}")
