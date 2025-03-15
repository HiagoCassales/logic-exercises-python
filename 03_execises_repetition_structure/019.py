# Logic exercise (Repetition Structure - PythonBrasil)
'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''
numeros = [5, 6, 3, 1, 8, 2, 4, 9, -5, 2000]

# Filtrando os números entre 0 e 1000
numeros_validos = [n for n in numeros if 0 <= n <= 1000]

maior = 0
menor = numeros_validos[0]
soma = 0

for n in numeros_validos:
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f"Maior {maior}")
print(f"Menor {menor}")
print(f"Soma {soma}")
