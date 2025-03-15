'''
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''

vetor = []
soma = 0
multiplicacao = 1

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)
    soma += numero
    multiplicacao *= numero

print(f"Todos os números {vetor}")
print(f"A soma dos números {soma}")
print(f"A multiplicação dos números {multiplicacao}")
