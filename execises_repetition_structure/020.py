# Logic exercise (Repetition Structure - PythonBrasil)
'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
'''

while True:
    fatorial = 1
    print("1)Iniciar")
    print("2)Sair")
    opcao1 = input("Digite o número da opcão: ")

    if opcao1 not in ["1", "2"]:
        print("Selecione a opção correta")
    
    if opcao1 == "1":
        numero_fatorial = int(input("Digite um número entre 0 a 16: "))

        if numero_fatorial > 16 or numero_fatorial < 0:
            print("Número inválido!!")
        else:
            for n in range(1, numero_fatorial + 1):
                fatorial = fatorial * n
    
            print(fatorial)
    
    if opcao1 == "2":
        print("Encerrando!!")
        break