# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
'''

try:
    numero = float(input("Digite um número: "))

    if numero % 1 == 0:
        print(f"O número {int(numero)} é inteiro")
    else:
        print(f"O número {numero} é decimal")
except ValueError:
    print("Digite um número correto")
