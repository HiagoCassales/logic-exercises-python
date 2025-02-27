# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: 
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
'''

contador = {
    "0-25": 0,
    "26-50": 0,
    "51-75": 0,
    "76-100": 0,
}

while True:
    numeros = int(input("Número 0 a 100: "))

    if numeros < 0:
        print("Encerrando!!")
        break

    if numeros >= 0 and numeros <= 25:
        contador["0-25"] += 1
    elif numeros >= 26 and numeros <= 50:
        contador["26-50"] += 1
    elif numeros >= 51 and numeros <= 75:
        contador["51-75"] += 1
    elif numeros >= 76 and numeros <= 100:
        contador["76-100"] += 1
    else:
        print("Número ultrapassou 100, não permitido")

print(f"Números de 0 a 25: {contador['0-25']}")
print(f"Números de 26 a 50: {contador['26-50']}")
print(f"Números de 51 a 75: {contador['51-75']}")
print(f"Números de 76 a 100: {contador['76-100']}")