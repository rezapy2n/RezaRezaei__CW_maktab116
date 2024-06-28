class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = cls(fahrenheit).to_celsius(fahrenheit)
        return cls(celsius)


celsius_temp = 25
fahrenheit_temp = 77


temp_instance = Temperature.from_fahrenheit(fahrenheit_temp)

print(f"{fahrenheit_temp}°F is approximately {temp_instance.celsius:.2f}°C")
