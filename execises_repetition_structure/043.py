# Logic exercise (Repetition Structure - PythonBrasil)
'''
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

cardapio = {
    100:{"nome": "Cachorro Quente", "preco": 1.20, "quantidade": 0},
    101:{"nome": "Bauru Simples", "preco": 1.30, "quantidade": 0},
    102:{"nome": "Bauru com ovo", "preco": 1.50, "quantidade": 0},
    103:{"nome": "Hambúrguer", "preco": 1.20, "quantidade": 0},
    104:{"nome": "Cheeseburguer", "preco": 1.30, "quantidade": 0},
    105:{"nome": "Refrigerante", "preco": 1.00, "quantidade": 0},
}
total_item = 0
valor_total = 0

print("Opções")
print("1) Cardápio")
print("2) Adicionar item")
print("3) Finalizar pedido")
print("4) Sair")

while True:
    opcao = input("Opção: ")

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida")

    if opcao == "1":
        print("\nCardápio\n")
        print(f"| {"Especificação":<20} | {"Código":<10} | {"Preço":<13} |")
        print(f"{"_"*50}")
        for n in cardapio:
            print(f"| {cardapio[n]["nome"]:<20} | {n:>10} | R$ {cardapio[n]["preco"]:>10} |")
        print(f"{"_"*50}")
    
    if opcao == "2":
        while True:
            codigo = int(input("Código do pedido: "))

            if codigo < 0:
                break

            if codigo not in cardapio:
                print("Código inválido")

            quantidade = int(input("Quantos items deseja: "))

            cardapio[codigo]["quantidade"] += quantidade
    
    if opcao == "3":
        print("\nPedidos\n")
        print(f"| {"Especificação":<20} | {"Código":<10} | {"Preço":<13} | {"Quantidades":<10} | {"Total por item":10} |")
        print(f"{"_"*84}")
        for n in cardapio:
            if cardapio[n]["quantidade"] > 0:
                valor_item = cardapio[n]["preco"] * cardapio[n]["quantidade"]
                valor_total += valor_item
                total_item += cardapio[n]["quantidade"]
                print(f"| {cardapio[n]["nome"]:<20} | {n:>10} | R$ {cardapio[n]["preco"]:>10.2f} | Qtd. {cardapio[n]["quantidade"]:>6} | R$ {valor_item:>11.2f} |")
        

        print(f"{"_"*84}")
        print(f"{"":>51} | Qtd. {total_item:>6} | R$ {valor_total:>11.2f} |")


    if opcao == "4":
        print("Saindo!!")
        break