import json
import requests


Your_Api_Key = ""

input_currency = input("Enter the currency you want to convert from: ").upper()
converted_currency = input("Enter the currency you want to convert to: ").upper()


response = f"https://v6.exchangerate-api.com/v6/{Your_Api_Key}/latest/{input_currency}"
data = requests.get(response).json()
print(f"1 {input_currency} is {data['conversion_rates'][converted_currency]} {converted_currency}")