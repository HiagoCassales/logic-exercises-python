'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.
'''

vetor = []
vetor_par = []
vetor_impar = []

for count in range(1, 21):
    try:
        numero = int(input(f"{count}º número: "))
        vetor.append(numero)
        if numero % 2 == 0:
            vetor_par.append(numero)
        else:
            vetor_impar.append(numero)
    except ValueError:
        print("Digite apenas números!")
        break

if vetor != [] and vetor_par != [] and vetor_impar != []:
    print(f"Todos os números {vetor}")
    print(f"Números pares {vetor_par}")
    print(f"Números ímpares {vetor_impar}")