# Logic exercise (Sequential Structure - PythonBrasil)
'''
Create a program that asks for the radius of a circle, calculates, and shows its area.
'''
import math
radius = float(input("Enter the radius of a circle: "))

area = math.pi * radius ** 2

print(f"The area is {area:.2f}")