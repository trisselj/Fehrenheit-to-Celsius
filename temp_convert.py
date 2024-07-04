# Author: Jake Trissel
# Github Username: trisselj
# Date: 06/26/2024
# Description: Converts from Celsius to Fahrenheit

# Entering of temperature
Celsius = input("Please enter the temperature in Celsius")
# Str to float
CelsiusFloat = float(Celsius)
# Conversion
FahrenheitFloat = (9/5) * CelsiusFloat + 32
# Printing of answer
print("The temperature you entered in Fahrenheit is " + str(FahrenheitFloat))