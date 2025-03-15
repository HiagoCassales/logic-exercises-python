# Logic exercise (Sequential Structure - PythonBrasil)
'''
Create a program that asks for the temperature in degrees Celsius, converts it, and shows it in degrees Fahrenheit.
'''

temperature_celsius = float(input("Enter the temperature in Celsius: "))

temperature_fahrenheit = (temperature_celsius * 9/5) + 32

print(f"Temperature in degrees Fahrenheit is {temperature_fahrenheit:.1f}")