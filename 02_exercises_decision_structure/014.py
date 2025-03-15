# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 9:
    conceito = "A"
    status = "APROVADO"
elif media >= 7.5:
    conceito = "B"
    status = "APROVADO"
elif media >= 6:
    conceito = "C"
    status = "APROVADO"
elif media >= 4:
    conceito = "D"
    status = "REPROVADO"
else:
    conceito = "E"
    status = "REPROVADO"

print(f"Primeira nota: {nota1:.2f}")
print(f"Segunda nota: {nota2:.2f}")
print(f"Média das notas: {media:.2f}")
print(f"Conceito: {conceito}")
print(f"Status: {status}")

