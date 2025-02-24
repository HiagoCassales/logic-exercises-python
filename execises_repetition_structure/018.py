# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

numeros = 5, 6, 3, 1, 8, 2, 4, 9

maior = 0
menor = numeros[0]
soma = 0

for n in numeros:
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f"Maior {maior}")
print(f"Menor {menor}")
print(f"Soma {soma}")