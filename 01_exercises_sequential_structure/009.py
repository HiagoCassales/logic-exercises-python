# Logic exercise (Sequential Structure - PythonBrasil)
'''
Create a program that asks for the temperature in degrees Fahrenheit, converts it, and shows the temperature in degrees Celsius.
C = 5 * ((F - 32) / 9).
'''

temperature_fahrenheit = int(input("Enter the temperature in fahrenheit: "))

celsius = 5 * ((temperature_fahrenheit - 32) / 9)

print(f"Temperature in degrees Celsius is {celsius:.2f}")