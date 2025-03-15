'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''
vetor = ['d', 'b', 'g', 'a', 'e', 'i', 'c', 'h', 'f', 'j']

contador = 0
consoantes = []
for n in vetor:
    if n not in ["a", "e", "i", "o", "u"]:
        consoantes.append(n)
        contador += 1

print(f"Total de {contador} consoantes, as consoantes foram {consoantes}")