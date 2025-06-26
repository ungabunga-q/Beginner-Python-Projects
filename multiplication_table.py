"""
Multiplication Table
Prints the multiplication table for a number.
"""
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    multiplication_table(n)
