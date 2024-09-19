# Simple Currency Converter in Python

# Predefined exchange rates (as an example)
exchange_rates = {
    'USD': {'INR': 74.85, 'EUR': 0.85, 'GBP': 0.75},
    'INR': {'USD': 0.013, 'EUR': 0.011, 'GBP': 0.010},
    'EUR': {'USD': 1.18, 'INR': 88.34, 'GBP': 0.88},
    'GBP': {'USD': 1.33, 'INR': 100.50, 'EUR': 1.14}
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        return amount * exchange_rates[from_currency][to_currency]
    else:
        return None

if __name__ == "__main__":
    amount = float(input("Enter the amount: "))
    from_currency = input("From currency (e.g., USD): ").upper()
    to_currency = input("To currency (e.g., INR): ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Conversion rate not available for the given currencies.")