# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
'''

numero = int(input("Número: "))

primos = []
contagem_divisoes = 0  # Contador para o número total de divisões realizadas

if numero >= 2:
    for n in range(2, numero + 1):  # Percorre todos os números de 2 até N
        eh_primo = True  # Assume que o número é primo até provar o contrário

        for i in range(2, n):  # Testa se n é divisível por algum número menor que ele
            contagem_divisoes += 1  # Conta cada tentativa de divisão
            if n % i == 0:  # Se for divisível por qualquer número além de 1 e ele mesmo, não é primo
                eh_primo = False
                break  # Interrompe o loop para otimizar

        if eh_primo:
            primos.append(n)  # Se passou pelo teste, adiciona na lista de primos

    print(f"Os números primos entre 1 e {numero} são: {primos}")
    print(f"Total de divisões realizadas: {contagem_divisoes}")

else:
    print("Não há números primos menores que 2.")
