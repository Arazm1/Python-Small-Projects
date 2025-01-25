import json
import requests


Your_Api_Key = ""    #Your API Key: Get it from https://www.exchangerate-api.com/
Url = "https://v6.exchangerate-api.com/v6"

input_currency = input("Enter the currency you want to convert from: ").upper()
while True:
    try:
        original_amount_currency = float(input(f"Enter the amount of {input_currency} you wish to convert: "))
        if original_amount_currency > 0:
            break
        else:
            print("The amount must be greater than 0!")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

converted_currency = input("Enter the currency you want to convert to: ").upper()


response = f"{Url}/{Your_Api_Key}/latest/{input_currency}"
data = requests.get(response).json()


conversion_rate = data['conversion_rates'][converted_currency]
converted_amount = original_amount_currency * conversion_rate
print(f"{original_amount_currency} {input_currency} is {converted_amount:.3f} {converted_currency}")
