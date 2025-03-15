# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''

par = 0
impar = 0
for n in range(10):
    numeros = int(input('Digite os números: '))
    
    if numeros % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Quantidade de números par: {par}")
print(f"Quantidade de números ímpar: {impar}")
