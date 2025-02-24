# Logic exercise (Repetition Structure - PythonBrasil)
'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
'''

anterior = 0
proximo = 1

while proximo <= 500:
    print(proximo)
    soma = proximo + anterior
    anterior = proximo
    proximo = soma
