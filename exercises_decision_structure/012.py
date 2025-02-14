# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

hora_valor = float(input("Digite o valor da hora: "))
hora_trabalho = float(input("Digite a quantidade de horas trabalhadas: "))

salario_bruto = hora_valor * hora_trabalho

if salario_bruto <= 900:
    ir_texto = "Isento"
    ir = 0
elif salario_bruto <= 1500:
    ir_texto = "5%"
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir_texto = "10%"
    ir = salario_bruto * 0.10
else:
    ir_texto = "20%"
    ir = salario_bruto * 0.20

inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11
total_desconto = ir + inss
salario_liquido = salario_bruto - total_desconto

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"(-) IR ({ir_texto}): R$ {ir:.2f}")
print(f"(-) INSS (10%): R$ {inss:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f}")
print(f"Total de descontos: R$ {total_desconto:.2f}")
print(f"Salário Liquido: R$ {salario_liquido:.2f}")