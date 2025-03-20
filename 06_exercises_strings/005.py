'''
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
'''
nome = input("Insira o nome: ").upper()

for i in range(len(nome), 0, -1):
    print(nome[:i])