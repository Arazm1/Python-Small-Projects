import json
import requests


Your_Api_Key = ""

input_currency = input("Enter the currency you want to convert from: ").upper()
original_amount_currency = float(input(f"Enter the amount of {input_currency} you wish to convert: "))
converted_currency = input("Enter the currency you want to convert to: ").upper()


response = f"https://v6.exchangerate-api.com/v6/{Your_Api_Key}/latest/{input_currency}"
data = requests.get(response).json()


conversion_rate = data['conversion_rates'][converted_currency]
converted_amount = original_amount_currency * conversion_rate
print(f"{original_amount_currency} {input_currency} is {converted_amount:.3f} {converted_currency}")
