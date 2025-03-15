# Logic exercise (Repetition Structure - PythonBrasil)
'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, 
e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
'''
maior = float('-inf')  # Menor valor possível
menor = float('inf')   # Maior valor possível
media = 0
soma = 0
contador = 0


while True:
    print("1) Adicionar temperatura")
    print("2) Ver dados")
    print("3) Sair")
    opcao = input("Opção: ")

    if opcao not in ["1", "2", "3"]:
        print("Digite uma opção válida")
        continue

    if opcao == "3":
        print("Encerrando!!")
        break
    elif opcao == "1":
        user_temperatura = float(input("Temperatura: "))
        soma += user_temperatura
        contador += 1
        if user_temperatura > maior:
            maior = user_temperatura
        if user_temperatura < menor:
            menor = user_temperatura
    elif opcao == "2":
        media = soma / contador

        print(f"A maior temperatura foi {maior}")
        print(f"A média das temperaturas foi {media:.2f}")
        print(f"A menor temperatura foi {menor}")