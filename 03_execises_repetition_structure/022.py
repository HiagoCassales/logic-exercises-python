# Logic exercise (Repetition Structure - PythonBrasil)
'''
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
'''

numero = int(input("Número: "))

divisiveis = []

if numero > 1:
    for n in range(2, numero):
        if numero % n == 0:
            divisiveis.append(n)
else:
    print(f"{numero} e menor ou igual a 1 não pode ser primo")

if len(divisiveis) == 0 and numero > 1:
    print(f"{numero} é primo")
else:
    if numero > 1:
        print(f"{numero} não é primo")
        print(f"Ele e divisivel por {divisiveis}")