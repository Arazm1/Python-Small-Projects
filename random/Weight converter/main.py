class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit

    def convert(self):
        if self.unit == 'k':
            return self._kg_to_lbs()
        elif self.unit == 'l':
            return self._lbs_to_kg()
        else:
            raise ValueError(f"'{self.unit}' is not a valid unit. Please use 'k' for kilograms or 'l' for pounds.")

    def _kg_to_lbs(self):
        converted_weight = self.weight * 2.20462262185
        return f"{self.weight} kg is {converted_weight:.2f} lbs."

    def _lbs_to_kg(self):
        converted_weight = self.weight * 0.45359237
        return f"{self.weight} lbs is {converted_weight:.2f} kg."


try:
    weight = float(input("Enter a weight: "))
    unit = input("Kilograms (k) or Pounds (l)? ").lower()
    
    converter = WeightConverter(weight, unit)
    print(converter.convert())
except ValueError as e:
    print(e)
