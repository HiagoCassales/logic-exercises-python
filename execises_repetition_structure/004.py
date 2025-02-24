# Logic exercise (Repetition Structure - PythonBrasil)
'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule 
e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento.
'''

populacao_a = 80000
populacao_b = 200000
contador = 0

while populacao_a < populacao_b:
    # Calcula os crescimentos anuais
    taxa_a = populacao_a * 0.03
    taxa_b = populacao_b * 0.015

    # Atualiza as populações
    populacao_a += taxa_a
    populacao_b += taxa_b

    # Conta o ano
    contador += 1

print(f"Levará {contador} anos para a população de A ultrapassar ou igualar a de B.")
print(f"População final de A: {populacao_a:.0f}")
print(f"População final de B: {populacao_b:.0f}")