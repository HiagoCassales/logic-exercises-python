'''
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

'''

def n_esima(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f"{j}", end=" ")
        print()

n_esima(6)