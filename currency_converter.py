"""
Currency Converter
Converts USD to EUR (static rate for beginners).
"""
def convert_usd_to_eur(usd):
    rate = 0.92  # Example static rate
    return usd * rate

if __name__ == "__main__":
    usd = float(input("Enter amount in USD: "))
    eur = convert_usd_to_eur(usd)
    print(f"{usd} USD is approximately {eur:.2f} EUR.")
