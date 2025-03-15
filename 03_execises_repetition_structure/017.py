# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''

numero = int(input("Digite um número: "))
# 5x4x3x2x1 = 120
fatorial = 1

for n in range(1, numero + 1):
    fatorial = fatorial * n

print(fatorial)