# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
'''

conjuntos = {
    1: 179, 
    2: 160, 
    3: 164, 
    4: 161, 
    5: 180, 
    6: 172, 
    7: 186, 
    8: 162, 
    9: 176, 
    10: 170
}
alto = float("-inf")
codigo_alto = 0
baixo = float("inf")
codigo_baixo = 0

for n in conjuntos:
    if conjuntos[n] > alto:
        alto = conjuntos[n]
        codigo_alto = n
    if conjuntos[n] < baixo:
        baixo = conjuntos[n]
        codigo_baixo = n

print(f"O mais alto é código: {codigo_alto} - Altura: {alto}")
print(f"O mais baixo é código: {codigo_baixo} - Altura: {baixo}")