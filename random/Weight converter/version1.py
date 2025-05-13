#Weight converter

weight = float(input("Enter a weight: "))
unit = input("Kilograms (k) or pounds (l)? ").lower()

if unit == 'k':
    weight_converted = weight * 2.20462262185
    print(f"{weight} kg is {weight_converted:.2f} lbs")
elif unit == 'l':
    weight_converted = weight * 0.45359237
    print(f"{weight} Lbs is {weight_converted:.2f} kg")
else:
    print(f"{unit} is not a valid unit.")
