'''
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

vetor_a = []
soma = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor_a.append(numero)
    
for n in vetor_a:
    quadrado = n ** 2
    soma += quadrado

print(soma)