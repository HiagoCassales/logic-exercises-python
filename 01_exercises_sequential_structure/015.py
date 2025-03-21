# Logic exercise (Sequential Structure - PythonBrasil)
'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

valor_hora = float(input("Digite quanto ganha por hora: "))
hora_trabalhada = float(input("Digite quantas horas trabalhou no mês atual: "))

salario_bruto = valor_hora * hora_trabalhada

imposto_renda = (11 * salario_bruto) / 100
inss = (8 * salario_bruto) / 100
sindicato = (5 * salario_bruto) / 100
salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

print(f"Salário Bruto : R$ {salario_bruto:.2f}")
print(f"IR (11%) : R$ {imposto_renda:.2f}")
print(f"INSS (8%) : R$ {inss:.2f}")
print(f"Sindicato (5%) : R$ {sindicato:.2f}")
print(f"Salário Líquido : R$ {salario_liquido:.2f}")
