# Logic exercise (Repetition Structure - PythonBrasil)
'''
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
'''

numero = int(input("Número: "))
primo = True

if numero > 1:
    for n in range(2, numero):
        if numero % n == 0:
            primo = False
    if primo:
        print("Esse número e primo")
    else:
        print("Esse número não e primo")