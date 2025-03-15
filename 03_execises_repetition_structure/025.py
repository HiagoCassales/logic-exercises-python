# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar
se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''

idade = []
contador = 0


while True:
    soma = 0
    media = 0
    print("1) Adicionar idade")
    print("2) Media")
    print("3) Sair")
    opcao = input("Seleciona a opção: ")

    if opcao == "1":
        idade.append(int(input("Digite a idade: ")))
        contador += 1
    elif opcao == "2":
        if contador == 0:
            print("Divisão por 0 não e possivel")
            break
        else:
            for n in idade:
                soma += n
            
            media = soma / contador

        if media >= 0 and media <= 25:
            print(f"Média {media}, Jovem")
        elif media > 25 and media <= 60:
            print(f"Média {media}, Adulto")
        elif media > 60:
            print(f"Média {media}, idoso")
        else:
            print("Números negativos não são válidos")
        
        contador = 0
        idade = 0
    elif opcao == "3":
        print("Encerrando!!")
        break