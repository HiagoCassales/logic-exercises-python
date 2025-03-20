'''
Conta espaços e vogais. 
Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
'''

frase = input("Insira a palavra: ").lower()

vogais = ["a", "e", "i", "o", "u"]
contador_total = 0
contar_espacos = frase.count(" ")

for n in vogais:
    contador_total += frase.count(n)

print(f"Existe {contar_espacos} espaços em branco na frase.")
print(f"As vogais a, e, i, o, u, aparecem {contador_total} vezes.")