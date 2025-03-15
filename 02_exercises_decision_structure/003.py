# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

opcao = input("Selecione o sexo [F] ou [M]: ").upper()

if opcao not in "F" "M":
    print("Sexo Inválido")

if opcao == "F":
    print("Escolheu F - Feminino")
if opcao == "M":
    print("Escolheu M - Masculino")