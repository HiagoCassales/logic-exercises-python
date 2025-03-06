# Logic exercise (Repetition Structure - PythonBrasil)
'''
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
'''

valor_n = int(input("Valor de N: "))
h = 0

for n in range(1, valor_n + 1):
    h += 1 / n

print(f"O valor de H com {valor_n} termos é: {h:.4f}")