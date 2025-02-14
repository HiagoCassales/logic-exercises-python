# Logic exercise (Sequential Structure - PythonBrasil)
'''
Create a program that asks for the 4 bimonthly grades and shows the average.
'''

bimonthly_grades1 = int(input("Enter the first grade: "))
bimonthly_grades2 = int(input("Enter the second grade: "))
bimonthly_grades3 = int(input("Enter the third grade: "))
bimonthly_grades4 = int(input("Enter the fourth grade: "))

average_grade = int((bimonthly_grades1 + bimonthly_grades2 + bimonthly_grades3 + bimonthly_grades4) / 4)

print(f"The average of the grades is {average_grade}")