# Logic exercise (Sequential Structure - PythonBrasil)
'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
1 - o produto do dobro do primeiro com metade do segundo .
2 - a soma do triplo do primeiro com o terceiro.
3 - o terceiro elevado ao cubo.
'''

numero_int1 = int(input("Digite o primeiro número inteiro: "))
numero_int2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite um número real: "))

dobro_primeiro, metade_segundo = numero_int1 * 2, numero_int2 / 2
produto_a = dobro_primeiro * metade_segundo

triplo_primeiro = numero_int1 * 3 + numero_int2

elevado_cubo = numero_real ** 3

print(produto_a, triplo_primeiro, elevado_cubo )