# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente"
'''

print("So responda com [Sim ou Não]")
pergunta_um = input("Telefonou para a vítima? ").upper()
pergunta_dois = input("Esteve no local do crime? ").upper()
pergunta_tres = input("Mora perto da vítima? ").upper()
pergunta_quatro = input("Devia para a vítima? ").upper()
pergunta_cinco = input("Já trabalhou com a vítima? ").upper()

resposta_sim = 0

if pergunta_um == "SIM":
    resposta_sim += 1
if pergunta_dois == "SIM":
    resposta_sim += 1
if pergunta_tres == "SIM":
    resposta_sim += 1
if pergunta_quatro == "SIM":
    resposta_sim += 1
if pergunta_cinco == "SIM":
    resposta_sim += 1

print(f"Respostas {resposta_sim}")
if resposta_sim == 2:
    print("Suspeita")
elif resposta_sim >= 3 and resposta_sim <=4:
    print("Cúmplice")
elif resposta_sim == 5:
    print("Assassino")
else:
    print("Inocente")