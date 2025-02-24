# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
'''

base = int(input("Número base: "))
expoente = int(input("Número expoente: "))
resultado = 1

for x in range(expoente):
    resultado *= base

print(resultado)

#função de potência do python
potencia = base ** expoente
print(potencia)