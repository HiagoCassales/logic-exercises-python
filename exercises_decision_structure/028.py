# Logic exercise (Decision Structure - PythonBrasil)
'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

import sys, os

print("Lista de produtos:")
print("1)File Duplo ")
print("2)Alcatra ")
print("3)Picanha ")
produto = input("Digite o número do produto desejado: ")
if produto not in ["1", "2", "3"]:
    print("Digite o código correto do produto!")
    sys.exit()  # Interrompe a execução do programa
else:
    os.system("cls")


quantidade_kg = input("Quantidade em Kg: ")
try:
    quantidade_kg = float(quantidade_kg)
    os.system("cls")
except ValueError:
    print("Erro! Por favor, digite apenas números.")
    sys.exit()

print("Tipo pagamento:")
print("1)Dinheiro")
print("2)Cartão tabajara")
tipo_pagamento = input("Tipo pagamento: ")
if tipo_pagamento not in ["1", "2"]:
    print("Digite o código correto do tipo de pagamento!")
    sys.exit()  # Interrompe a execução do programa
else:
    os.system("cls")

preco = 0
desconto = 0
total = 0
total_pagar = 0
tipo_pagamento_name = ''

if produto == "1":
    produto_name = "File Duplo"
    if quantidade_kg <= 5:
        tipo_pagamento_name = "Dinheiro"
        preco = 4.90
        total = quantidade_kg * preco
        total_pagar += total
        if tipo_pagamento == "2":
            tipo_pagamento_name = "Crtão Tabajara"
            desconto = total * 0.05
            total_pagar = total - desconto
    elif quantidade_kg > 5:
        tipo_pagamento_name = "Dinheiro"
        preco = 5.80
        total = quantidade_kg * preco
        total_pagar += total
        if tipo_pagamento == "2":
            tipo_pagamento_name = "Crtão Tabajara"
            desconto = total * 0.05
            total_pagar = total - desconto

if produto == "2":
    produto_name = "Alcatra"
    if quantidade_kg <= 5:
        tipo_pagamento_name = "Dinheiro"
        preco = 5.90
        total = quantidade_kg * preco
        total_pagar += total
        if tipo_pagamento == "2":
            tipo_pagamento_name = "Crtão Tabajara"
            desconto = total * 0.05
            total_pagar = total - desconto
    elif quantidade_kg > 5:
        tipo_pagamento_name = "Dinheiro"
        preco = 6.80
        total = quantidade_kg * preco
        total_pagar += total
        if tipo_pagamento == "2":
            tipo_pagamento_name = "Crtão Tabajara"
            desconto = total * 0.05
            total_pagar = total - desconto

if produto == "3":
    produto_name = "Picanha"
    if quantidade_kg <= 5:
        tipo_pagamento_name = "Dinheiro"
        preco = 6.90
        total = quantidade_kg * preco
        total_pagar += total
        if tipo_pagamento == "2":
            tipo_pagamento_name = "Crtão Tabajara"
            desconto = total * 0.05
            total_pagar = total - desconto
    elif quantidade_kg > 5:
        tipo_pagamento_name = "Dinheiro"
        preco = 7.80
        total = quantidade_kg * preco
        total_pagar += total
        if tipo_pagamento == "2":
            tipo_pagamento_name = "Crtão Tabajara"
            desconto = total * 0.05
            total_pagar = total - desconto

print(f"Produto: {produto_name}\nQuantidade Kg: {quantidade_kg}Kg\nPreço Total: R$ {total:.2f}\nTipo Pagamento: {tipo_pagamento_name}\nDesconto: R$ {desconto:.2f}\nValor a pagar: R$ {total_pagar:.2f}")