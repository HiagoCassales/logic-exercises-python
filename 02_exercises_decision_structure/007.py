# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

numeros = 8, 6, 15
maior = 0
menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    
    if n < menor:
        menor = n

print(f"O menor número foi {menor}")
print(f"O maior número foi {maior}")