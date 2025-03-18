'''
Faça um programa que simule um lançamento de dados. 
Lance o dado 100 vezes e armazene os resultados em um vetor . 
Depois, mostre quantas vezes cada valor foi conseguido. Dica: 
use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
'''
import random
contagem_dados = [0] * 6

def simular_lancamentos(numero_lancamentos, min, max):
    for n in range(1, numero_lancamentos + 1):
        numero_gerado = random.randint(min, max)
        contagem_dados[numero_gerado - 1] += 1

simular_lancamentos(100, 1, 6)
i = 0
for n in contagem_dados:
    print(f"Dado N {i + 1} = {contagem_dados[i]}")
    i += 1