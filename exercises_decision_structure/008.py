# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''

produto1 = float(input("Digite o preço do produto [Feijão]: "))
produto2 = float(input("Digite o preço do produto [Arroz]: "))
produto3 = float(input("Digite o preço do produto [Macarrão]: "))


if produto1 < produto2 and produto1 < produto3:
    print("Feijão foi o produto mais barato")
elif produto2 < produto1 and produto2 < produto3:
    print("Arroz foi o produto mais barato")
elif produto3 < produto1 and produto3 < produto2:
    print("Macarrão foi o produto mais barato")
elif produto1 == produto2 == produto3:
    print("Todos os produtos possuem o mesmo preço")
elif produto1 == produto2:
    print("Feijão e Arroz Possuem o mesmo valor")
elif produto1 == produto3:
    print("Feijão e Macarrão Possuem o mesmo valor")
elif produto2 == produto3:
    print("Arroz e Macarrão Possuem o mesmo valor")
