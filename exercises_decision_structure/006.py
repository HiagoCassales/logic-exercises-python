# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um Programa que leia três números e mostre o maior deles.
'''

numeros = 9, 7, 3
maior = 0

for n in numeros:
    if n > maior:
        maior = n
print(maior)