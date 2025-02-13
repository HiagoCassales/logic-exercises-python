# Logic exercise (Sequential Structure - PythonBrasil)
'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

print("1) Mulher")
print("2) Homem")
opcao = int(input("Selecione uma opção: "))

h = float(input("Digite a sua altura: "))

if opcao == 1:
    peso_ideal_mulher = (62.1 * h) - 44.7
    print(f"Seu peso ideal é {peso_ideal_mulher}")
else:
    peso_ideal_homem = (72.7 * h) - 58
    print(f"Seu peso ideal é {peso_ideal_homem}")