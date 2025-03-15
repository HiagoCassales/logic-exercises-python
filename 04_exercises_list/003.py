'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

notas = [5, 6, 2, 8]
soma = 0
for n in notas:
    soma += n

media = soma / 4

print(f"A média calculada é {media:.2f}")