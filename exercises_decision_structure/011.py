# Logic exercise (Decision Structure - PythonBrasil)
'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

salario = float(input("Digite o salário do colaborador: "))

if salario <= 280:
    percentual = 1.20
    texto_percentual = '20%'
elif salario <= 700:
    percentual = 1.15
    texto_percentual = '15%'
elif salario <= 1500:
    percentual = 1.10
    texto_percentual = '10%'
else:
    percentual = 1.05
    texto_percentual = '5%'

novo_salario = salario * percentual  # Novo salário após o reajuste
aumento = novo_salario - salario  # Valor do aumento

print(f"o salário antes do reajuste R$ {salario:.2f}")
print(f"o percentual de aumento aplicado {texto_percentual}")
print(f"o valor do aumento R$ {aumento:.2f}")
print(f"o novo salário, após o aumento R$ {novo_salario:.2f}")
