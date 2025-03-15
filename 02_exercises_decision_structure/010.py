# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

print("Opções válidas")
print("M) matutino")
print("V) Vespertino")
print("N) Noturno")

opcao = input("Digite a opção: ").upper()

if opcao not in "MVN":
    print("Valor Inválido!")
else:
    if opcao == "M":
        print("Bom Dia!")
    elif opcao == "V":
        print("Boa Tarde")
    elif opcao == "N":
        print("Boa Noite!")