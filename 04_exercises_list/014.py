'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
'''

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
classificacao = 0

for i in perguntas:
    pergunta = input(f"Responda com (S/N - Sim/Não){i}: ")[0].upper()
    if pergunta in ["S"]:
        classificacao += 1

if classificacao < 2:
    print("Inocente")
elif classificacao == 2:
    print(f"Suspeita")
elif classificacao <= 4:
    print("Cúmplice")
else:
    print("Assassino")