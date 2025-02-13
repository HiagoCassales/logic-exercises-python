# Logic exercise (Sequential Structure - PythonBrasil)
'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, 
que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

import math

# Entrada do usuário
metro_quadrado = float(input("Metros quadrados: "))

# Adiciona 10% de folga
cobertura = (metro_quadrado / 6) * 1.1  

# Estratégia 1: Apenas latas de 18L
latas_18 = math.ceil(cobertura / 18)
preco_latas = latas_18 * 80

# Estratégia 2: Apenas galões de 3.6L
galoes_3_6 = math.ceil(cobertura / 3.6)
preco_galoes = galoes_3_6 * 25

# Estratégia 3: Misturar latas e galões para menor desperdício
latas_mistura = cobertura // 18  # Máximo de latas inteiras
resto_tinta = cobertura % 18  # O que sobra depois de usar as latas

galoes_mistura = math.ceil(resto_tinta / 3.6)  # Completar com galões
preco_mistura = (latas_mistura * 80) + (galoes_mistura * 25)

print(f"Litros necessários (com 10% de folga): {cobertura:.2f}")
print(f"Comprar apenas latas de 18 litros: {latas_18} latas, preço: R$ {preco_latas:.2f}")
print(f"Comprar apenas galões de 3,6 litros: {galoes_3_6} galões, preço: R$ {preco_galoes:.2f}")
print(f"Comprar misturando latas e galões: {int(latas_mistura)} latas e {galoes_mistura} galões, preço: R$ {preco_mistura:.2f}")


