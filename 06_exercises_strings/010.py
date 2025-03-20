'''
Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
'''

numeros_1_a_20 = [
    "um", "dois", "três", "quatro", "cinco", "seis", 
    "sete", "oito", "nove", "dez", "onze", "doze", 
    "treze", "quatorze", "quinze", "dezesseis", 
    "dezessete", "dezoito", "dezenove", "vinte"
]

multiplos_de_10 = [
    "trinta", "quarenta", "cinquenta", "sessenta", 
    "setenta", "oitenta", "noventa"
]

numero = int(input("Número 1 a 99: "))
str_numero = str(numero)

if numero > 99:
    print("Apenas números entre 1 a 99")
elif numero >= 1 and numero <= 20:
    print(f"{numeros_1_a_20[numero - 1].capitalize()}")
elif numero >= 30 and numero % 10 == 0:
    print(f"{multiplos_de_10[int(str_numero[:1]) - 3].capitalize()}")
elif numero > 20 and numero % 10 != 0:
    if numero > 20 and numero < 30:
        print(f"{numeros_1_a_20[19].capitalize()} e {numeros_1_a_20[int(str_numero[1]) - 1].capitalize()}")
    elif numero > 30:
        print(f"{multiplos_de_10[int(str_numero[:1]) - 3].capitalize()} e {numeros_1_a_20[int(str_numero[1]) - 1].capitalize()}")
