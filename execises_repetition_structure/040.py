# Logic exercise (Repetition Structure - PythonBrasil)
'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:

Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''

dados_cidades = {
    "São Paulo": {"veiculos": 1500, "acidentes": 112},
    "Rio de Janeiro": {"veiculos": 2800, "acidentes": 240},
    "Salvador": {"veiculos": 1200, "acidentes": 98},
    "Belo Horizonte": {"veiculos": 3100, "acidentes": 310},
    "Fortaleza": {"veiculos": 1800, "acidentes": 153}
}

maior, cidade_maior = float("-inf"), 0
menor, cidade_menor = float("inf"), 0

soma_veiculos = 0
media_veiculos = 0

soma_acidentes = 0
media_acidentes = 0
count_cidade_menor_2000 = 0

for n in dados_cidades:
    if dados_cidades[n]["acidentes"] > maior:
        maior = dados_cidades[n]["acidentes"]
        cidade_maior = n
    if dados_cidades[n]["acidentes"] < menor:
        menor = dados_cidades[n]["acidentes"]
        cidade_menor = n

    soma_veiculos += dados_cidades[n]["veiculos"]

    if dados_cidades[n]["veiculos"] < 2000:
        soma_acidentes += dados_cidades[n]["acidentes"]
        count_cidade_menor_2000 += 1

media_veiculos = soma_veiculos / len(dados_cidades)
media_acidentes = soma_acidentes / count_cidade_menor_2000

print(f"Maior cidade com índice de acidentes: {cidade_maior} - {maior}")
print(f"Menor cidade com índice de acidentes: {cidade_menor} - {menor}")
print(f"A média de veiculos nas {len(dados_cidades)} cidades juntas são: {media_veiculos:.2f}")
print(f"A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: {media_acidentes}")
