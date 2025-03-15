# Logic exercise (Sequential Structure - PythonBrasil)
'''
Create a program that asks how much you earn per hour and the number of hours worked in the month. Calculate and display the total of your salary for that month.
'''

earn_per_hour = float(input("Enter how much you earn per hour: "))
worked_hours = float(input("Enter how many hours you worked: "))

salary_month = earn_per_hour * worked_hours

print(f"Total of your salary for that month {salary_month:.2f}")