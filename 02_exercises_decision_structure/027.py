# Logic exercise (Decision Structure - PythonBrasil)
'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de 
morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

print("Fruteira\nMorango[1]\nMaça[2]")
mercadoria = input("Selecione a mercadoria: ")
quantidade_kg = float(input("Digite a quantidade em Kg: "))

if mercadoria not in "1" "2":
    print("Digite uma das opções corretas.")

valor = 0
desconto = 0

if mercadoria == "1":
    if quantidade_kg <= 5:
        produto = "Morango"
        valor = quantidade_kg * 2.50
    elif quantidade_kg > 5:
        produto = "Morango"
        valor = quantidade_kg * 2.20
        if quantidade_kg > 8 or valor > 25:
            desconto = valor * 0.10
            valor = valor - desconto

if mercadoria == "2":
    if quantidade_kg <= 5:
        produto = "Maça"
        valor = quantidade_kg * 1.80
    elif quantidade_kg > 5:
        produto = "Maça"
        valor = quantidade_kg * 1.50
        if quantidade_kg > 8 or valor > 25:
            desconto = valor * 0.10
            valor = valor - desconto

print(f"Produto {produto}\nDesconto {desconto:.2f}\nPreço a pagar R$ {valor:.2f}")