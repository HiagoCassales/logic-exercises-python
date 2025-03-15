# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida    Valor dos Juros     Quantidade de Parcelas          Valor da Parcela
R$ 1.000,00         0                   1                              R$  1.000,00
R$ 1.100,00         100                 3                               R$    366,00
R$ 1.150,00         150                  6                              R$    191,67
'''

divida = float(input("Divida: "))

print(f"{'|Valor da Dívida|':<10} {'|Valor dos Juros|':<10} {'|Parcelas|':<10} {'|Valor da Parcela|':<10}")
for n in range(1, 13):
    if n == 1:
        print(f"|R$ {divida:12.2f}| |{"0":>15}| |{"1":>8}| |R$ {divida:13.2f}|")
    if n == 3:
        valor_juros = divida * 0.1
        nova_divida = valor_juros + divida
        parcela = nova_divida / n

        print(f"|R$ {nova_divida:12.2f}| |{valor_juros:>15}| |{n:>8}| |R$ {parcela:13.2f}|")

    if n == 6:
        valor_juros = divida * 0.15
        nova_divida = valor_juros + divida
        parcela = nova_divida / n

        print(f"|R$ {nova_divida:12.2f}| |{valor_juros:>15}| |{n:>8}| |R$ {parcela:13.2f}|")
    
    if n == 9:
        valor_juros = divida * 0.2
        nova_divida = valor_juros + divida
        parcela = nova_divida / n

        print(f"|R$ {nova_divida:12.2f}| |{valor_juros:>15}| |{n:>8}| |R$ {parcela:13.2f}|")

    if n == 12:
        valor_juros = divida * 0.25
        nova_divida = valor_juros + divida
        parcela = nova_divida / n

        print(f"|R$ {nova_divida:12.2f}| |{valor_juros:>15}| |{n:>8}| |R$ {parcela:13.2f}|")