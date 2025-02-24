# Logic exercise (Repetition Structure - PythonBrasil)
'''
Altere o programa anterior para mostrar no final a soma dos números.
'''

numero1 = 55
numero2 = 58
soma = 0

for n in range(numero1 +1, numero2):
    print(n)
    soma += n

print(soma)