# Logic exercise (Sequential Structure - PythonBrasil)
'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

import math

tamanho_area = float(input("Digite o tamanho da área em metros quadrados: "))

litros_necessarios = tamanho_area / 3
latas_necessarias = math.ceil(litros_necessarios / 18)
preco = latas_necessarias * 80

print(f"Você precisará de {latas_necessarias} latas de tinta.")
print(f"O custo total será de R$ {preco:.2f}")


