# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

import math

# Entrada do usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Verifica se é realmente uma equação do segundo grau
if a == 0:
    print("Isso não é uma equação do segundo grau!")
else:
    # Calcula o delta
    delta = b**2 - 4*a*c

    if delta > 0:
        # Duas raízes reais diferentes
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"As raízes da equação são: x1 = {x1:.2f}, x2 = {x2:.2f}")

    elif delta == 0:
        # Uma raiz real
        x = -b / (2 * a)
        print(f"A equação tem uma raiz real: x = {x:.2f}")

    else:
        # Nenhuma raiz real
        print("A equação não possui raízes reais.")
