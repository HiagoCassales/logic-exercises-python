# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
'''

numero = int(input("Número: "))
conjunto = []
fatorial = 1


for n in range(1, numero +1):
    conjunto.append(n)
    fatorial *= n

conjunto.reverse()
print(f"{numero}! = {' . '.join(map(str, conjunto))} = {fatorial}")