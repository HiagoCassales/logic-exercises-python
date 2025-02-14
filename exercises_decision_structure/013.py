# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''

numero_dia = input("Descubra o dia da semana digite um número de 1-7: ")

if numero_dia not in "1234567":
    print("Digite um número entre 1 a 7")
else:
    if numero_dia == "1":
        print("Domingo")
    if numero_dia == "2":
        print("Segunda")
    if numero_dia == "3":
        print("Terça")
    if numero_dia == "4":
        print("Quarta")
    if numero_dia == "5":
        print("Quinta")
    if numero_dia == "6":
        print("Sexta")
    if numero_dia == "7":
        print("Sabado")