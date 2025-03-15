# Logic exercise (Repetition Structure - PythonBrasil)
'''
Em uma eleição presidencial existem quatro candidatos. 
Os votos são informados por meio de código. 
Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. 
Para finalizar o conjunto de votos tem-se o valor zero.
'''

candidatos = {
    1:{"nome": "Jose", "votos": 10},
    2:{"nome": "Jõao", "votos": 25},
    3:{"nome": "Marcos", "votos": 33},
    4:{"nome": "Arthur", "votos": 4},
    5:{"nome": "Voto Nulo", "votos": 102},
    6:{"nome": "Voto em Branco", "votos": 57},
}

total_votos = 0
while True:
    print("Opções")
    print("1) Votar")
    print("2) Estatisticas")
    print("3) Sair")
    opcao = input("Opção: ")

    if opcao not in ["1", "2", "3"]:
        print("Opção inválida")
    
    if opcao == "1":
        print("Opções")
        for n in candidatos:
            print(f"Nome: {candidatos[n]["nome"]:15} | Número: {n}")
        
        voto = int(input("Digite o Número: "))

        candidatos[voto]["votos"] += 1
    
    if opcao == "2":
        total_votos = 0
        for c in candidatos:
            print(f"Nome: {candidatos[c]["nome"]:15} | Votos: {candidatos[c]["votos"]}")
            total_votos += candidatos[c]["votos"]
            
        porcentagem_nulo = (candidatos[5]["votos"] / total_votos) * 100
        porcentagem_branco = (candidatos[6]["votos"] / total_votos) * 100
        print(f"A percentagem de votos nulos sobre o total de votos {porcentagem_nulo:.2f}%")
        print(f"A percentagem de votos em branco sobre o total de votos {porcentagem_branco:.2f}%")
    
    if opcao == "3":
        print("Encerrando")
        break