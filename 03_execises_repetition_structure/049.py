# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
'''

termo = int(input("Termo: "))
soma_serie = 0

for n in range(1, termo + 1):
    m = 2 * n -1
    termo_atual = n / m
    soma_serie += termo_atual
    print(f"{n}/{m}", end=" + " if n < termo else " ")

print(f"\nSoma da série: {soma_serie:.2f}")