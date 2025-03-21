'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''

saltos = []

while True:
    nome = input("Informe o nome do atleta: ")
    if nome == "":
        break
    atleta = []
    atleta.append(nome)
    soma = 0
    for i in range(1, 6):
        salto = float(input(f"Informe o {i}º salto: "))
        atleta.append(salto)
        soma += salto
    
    media = soma / 5
    atleta.append(media)
    saltos.append(atleta)

count = 0
for atleta in saltos:
    print(f"Atleta: {atleta[0]}")
    print(f"Primeiro Salto: {atleta[1]} m")
    print(f"Segundo Salto: {atleta[2]} m")
    print(f"Terceiro Salto: {atleta[3]} m")
    print(f"Quarto Salto: {atleta[4]} m")
    print(f"Quinto Salto: {atleta[5]} m")
    print()
    print(f"Resultado final:")
    print(f"Atleta: {atleta[0]}")
    print("Saltos:", " - ".join(str(atleta[n]) for n in range(1, 6)))
    print(f"Média dos saltos: {atleta[6]:.2f}")




