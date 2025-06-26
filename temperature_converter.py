"""
Temperature Converter
Converts Celsius to Fahrenheit and vice versa.
"""
def c_to_f(c):
    return c * 9/5 + 32

def f_to_c(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    choice = input("Convert (C)elsius or (F)ahrenheit? ").lower()
    if choice == 'c':
        c = float(input("Enter Celsius: "))
        print(f"Fahrenheit: {c_to_f(c):.2f}")
    elif choice == 'f':
        f = float(input("Enter Fahrenheit: "))
        print(f"Celsius: {f_to_c(f):.2f}")
    else:
        print("Invalid choice.")
