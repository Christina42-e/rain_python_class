"""Currency Conversion (Using Exchange Rates)
exchange_rates = {"USD": 1.0, "EUR": 0.85, "GBP": 0.75, "INR": 82.75}
"""
amount = float(input("Enter amount: "))
from_currency = input("From currency (USD, EUR, GBP, INR): ").upper()
to_currency = input("To currency (USD, EUR, GBP, INR): ").upper()

exchange_rates = {"USD": 1.0, "EUR": 0.85, "GBP": 0.75, "INR": 82.75}

if from_currency in exchange_rates and to_currency in exchange_rates:
    base_amount = amount / exchange_rates[from_currency]
    converted_amount = base_amount * exchange_rates[to_currency]
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
else:
    print("Invalid currency!")