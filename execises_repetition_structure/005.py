# Logic exercise (Repetition Structure - PythonBrasil)
'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''

while True:
    print("1) Iniciar")
    print("2) Sair")
    opcao = input("Digite uma opção: ")

    if opcao not in "1" "2":
        print("Digite uma opção válida!!")

    if opcao == "2":
        print("Encerrando, volte sempre!")
        break

    if opcao == "1":
        try:
            input_a = input("Digite o válor da população A: ")
            int_a = int(input_a)

            input_b = input("Digite o válor da população B: ")
            int_b = int(input_b)

            input_taxa_a = input("Digite o valor da taxa A: ")
            float_taxa_a = float(input_taxa_a)

            input_taxa_b = input("Digite o valor da taxa B: ")
            float_taxa_b = float(input_taxa_b)

            contador = 0
        except ValueError:
            print("Digite um número inteiro válido!!")

        while int_a < int_b:
            calculo_taxa_a = float_taxa_a / 100
            taxa_a = int_a * calculo_taxa_a

            int_a += taxa_a

            calculo_taxa_b = float_taxa_b / 100
            taxa_b = int_b * calculo_taxa_b

            int_b += taxa_b

            contador += 1
        
        break

print(f"Levará {contador} anos para a população de A ultrapassar ou igualar a de B.")
print(f"População final de A: {int_a:.0f}")
print(f"População final de B: {int_b:.0f}")