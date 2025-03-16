'''
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''

temperatura_mes = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
soma = 0

for i in range(0, 12):
    mes = (float(input(f"Informe a temperatura do mês de {meses[i]}: ")))
    temperatura_mes.append(mes)
    soma += mes

media = soma / 12

mes_ano = 1
print(f"Meses acima da média anual")
print(f"Média {media:.1f}°C")
for n in temperatura_mes:
    if n > media:
        print(f"{mes_ano} - {meses[mes_ano - 1]}: média do mês {n:.1f}°C")
    mes_ano += 1