import requests

input_name = input("Enter a name: ").capitalize()

response = f"https://api.nationalize.io/?name={input_name}"

data = requests.get(response).json()

name = data['name']
#country = ['country']
countries = data['country']
country_ids = [country['country_id'] for country in countries]
probabilities = [country["probability"] for country in countries]

print(f"Based on the name {input_name}, ")
for country_id, probability in zip(country_ids, probabilities):
    print(f"{probability:.2%} of individuals with this name are likely from {country_id}.")