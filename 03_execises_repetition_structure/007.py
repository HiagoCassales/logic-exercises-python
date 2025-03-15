# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que leia 5 números e informe o maior número.
'''

numeros = 5, 2, 7, 6, 8, 3
maior = 0

for n in numeros:
    if n > maior:
        maior = n

print(maior)