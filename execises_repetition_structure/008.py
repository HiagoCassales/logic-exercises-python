# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

numeros = 10, 11
soma = 0

for n in numeros:
    soma += n
    media = soma / len(numeros)

print(soma, media)