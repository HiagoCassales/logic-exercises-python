# Logic exercise (Repetition Structure - PythonBrasil)
'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos 
e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). 
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, 
portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. 
A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
'''

while True:
    nome = input("Nome do atleta: ").strip()
    if not nome:  # Se o nome for vazio, encerra o programa
        print("Programa encerrado.")
        break

    saltos = []
    for i in range(1, 6):
        salto = float(input(f"Distância do {i}º salto (em metros): "))
        saltos.append(salto)

    # Exibe os saltos
    print(f"\nAtleta: {nome}\n")
    for i, salto in enumerate(saltos, start=1):
        print(f"{i}º salto: {salto} m")

    # Encontra o melhor e o pior salto
    melhor_salto = max(saltos)
    pior_salto = min(saltos)

    # Exibe o melhor e o pior salto
    print(f"\nMelhor salto: {melhor_salto} m")
    print(f"Pior salto: {pior_salto} m")

    # Remove o melhor e o pior salto
    saltos.remove(melhor_salto)
    saltos.remove(pior_salto)

    # Calcula a média dos saltos restantes
    media = sum(saltos) / len(saltos)

    # Exibe o resultado final
    print(f"\nMédia dos demais saltos: {media:.1f} m")
    print(f"\nResultado final:")
    print(f"{nome}: {media:.1f} m\n")