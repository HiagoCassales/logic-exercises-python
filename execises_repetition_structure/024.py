# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que calcule o mostre a média aritmética de N notas.
'''
notas = []
soma = 0

while True:
    soma = 0
    print("1) Adicionar notas")
    print("2) Exibir media")
    print("3) Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        usuario = int(input("Digite a nota: "))
        notas.append(usuario)
    
    elif opcao == "2":
        for n in notas:
            soma += n    
        media = soma / len(notas)
        print(f"A media e {media}")
        notas = []
    
    elif opcao == "3":
        print("Saindo!!")
        break