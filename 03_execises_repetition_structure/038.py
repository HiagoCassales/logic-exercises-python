# Logic exercise (Repetition Structure - PythonBrasil)
'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''

salario_inicial = float(input("Salario: "))
novo_salario = salario_inicial
ano_contratado = 1995
ano_atual = 2025
aumento_ano = 0.02

for ano in range(ano_contratado, ano_atual + 1):
    if ano == 1996:
        salario = salario_inicial * aumento_ano
        novo_salario += salario
    if ano >= 1997:
        novo_aumento = aumento_ano * 2
        salario = salario_inicial * novo_aumento
        novo_salario += salario

print(f"Salario inicial: R$ {salario_inicial:.2f}")
print(f"Salario Atual: R$ {novo_salario:.2f}")
