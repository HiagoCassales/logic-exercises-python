# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

valor_saque = int(input("Digite o valor a sacar entre R$10 e R$600: "))
valor_pedido = valor_saque

resto100 = valor_saque // 100
valor_saque = valor_saque % 100
resto50 = valor_saque // 50
valor_saque = valor_saque % 50
resto10 = valor_saque // 10
valor_saque = valor_saque % 10
resto5 = valor_saque // 5
valor_saque = valor_saque % 5
resto1 = valor_saque // 1
valor_saque = valor_saque % 1

print(f"Para sacar a quantia de {valor_pedido} reais, o programa fornece {resto100} nota de 100, {resto50} nota de 50, {resto10} nota de 10, {resto5} nota de 5 e {resto1} nota de 1")