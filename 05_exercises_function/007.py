'''
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, 
que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
O programa deverá então exibir o valor a ser pago na tela. 

Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
O cálculo do valor a ser pago é feito da seguinte forma. 
Para pagamentos sem atraso, cobrar o valor da prestação.
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''

relatorio_diario = []
def valor_pagamento(valor, atraso):
    if atraso == 0:
        return valor
    elif atraso != 0:
        multa_fixa = valor * 0.03
        dia_atraso = atraso * 0.01
        multa_total = multa_fixa + dia_atraso
        return valor + multa_total

def formatacao(valor, atraso):
    prestacao = valor_pagamento(valor, atraso)
    relatorio_diario.append(prestacao)
    print(f"Valor a ser pago R$ {prestacao:.2f}")

def relatorio_dia():
    total_prestacoes = 0
    print(f"Relatório diário")
    print(f"Quantidade de prestações {len(relatorio_diario)}")
    for n in relatorio_diario:
        print(f"Valor da prestação R$ {n:.2f}")
        total_prestacoes += n
    print(f"Valor total das prestações R$ {total_prestacoes:.2f}")

while True:
    valor = float(input("Valor da prestação (0 para encerrar o programa): "))
    if valor <= 0:
        relatorio_dia()
        break
    dias = int(input("Dias de atraso: "))
    
    formatacao(valor, dias)