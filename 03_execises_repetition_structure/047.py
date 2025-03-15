# Logic exercise (Repetition Structure - PythonBrasil)
'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. 
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, 
conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. 
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04

'''

while True:
    notas = []
    count_nota = 0
    maior_nota, menor_nota = float("-inf"), float("inf")
    nome = input("Nome: ")


    for nota in range(1, 8):
        nota_jurado = float(input("Nota: "))
        if maior_nota < nota_jurado:
            maior_nota = nota_jurado
        if menor_nota > nota_jurado:
            menor_nota = nota_jurado
        notas.append(nota_jurado)
    
    print(f"Atleta: {nome}")
    for exibir_nota in notas:
        count_nota += 1
        print(f"{count_nota}º nota: {exibir_nota}")
    
    print("Resultado final: ")
    print(f"Atleta: {nome}")
    print(f"Melhor nota: {maior_nota}")
    print(f"Pior nota: {menor_nota}")

    notas.remove(maior_nota)
    notas.remove(menor_nota)
    media = sum(notas) / len(notas)

    print(f"Média: {media}")
