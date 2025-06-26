"""
Binary to Decimal Converter
Converts binary string to decimal number.
"""
def binary_to_decimal(b):
    return int(b, 2)

if __name__ == "__main__":
    b = input("Enter a binary number: ")
    print(f"Decimal: {binary_to_decimal(b)}")
