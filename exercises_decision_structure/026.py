# Logic exercise (Decision Structure - PythonBrasil)
'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a 
ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

print("A-álcool")
print("G-gasolina")
combustivel = input("Escolha as opções: ").upper()
quantidade = int(input("Quantos litros: "))

preco_alcool = quantidade * 1.90
preco_gasolina = quantidade * 2.50
desconto = 0
total = 0

if combustivel not in "A" "G":
    print("Opção ínvalida, escolha entre [A-álcool & G-gasolina]")
if quantidade <= 0:
    print("Adicione um valor acima do negativo ou zero")

if combustivel == "A":
    if quantidade <= 20:
        tipo = "Alcool - 3% Desconto"
        desconto = preco_alcool * 0.03
        total = preco_alcool - desconto
    elif quantidade > 20:
        tipo = "Alcool - 5% Desconto"
        desconto = preco_alcool * 0.05
        total = preco_alcool - desconto

elif combustivel == "G":
    if quantidade <= 20:
        tipo = "Gasolina - 4% Desconto"
        desconto = preco_gasolina * 0.04
        total = preco_gasolina - desconto
    elif quantidade > 20:
        tipo = "Gasolina - 6% Desconto"
        desconto = preco_gasolina * 0.06
        total = preco_gasolina - desconto



print(f"Combustivel: {tipo}\nTotal a pagar: R$ {total:.2f}")
