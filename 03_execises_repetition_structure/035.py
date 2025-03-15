# Logic exercise (Repetition Structure - PythonBrasil)
'''
Encontrar números primos é uma tarefa difícil. 
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
'''

numero = int(input("Número: "))
primos = []

if numero > 1:
    for n in range(2, numero + 1):
        e_primo = True

        for i in range(2, n):
            if n % i == 0:
                e_primo = False
                break

        if e_primo:
            primos.append(n)

    print(f"Os números primos entre 1 e {numero} são: {primos}")

else:
    print("Não há números primos menores que 2.")