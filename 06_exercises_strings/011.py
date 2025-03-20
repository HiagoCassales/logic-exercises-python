'''
Jogo de Forca. 
Desenvolva um jogo da forca. 
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
'''

import random

palavra_secreta = "PYTHON"
palavra_exibida = "_" * len(palavra_secreta)
tentativas_restantes = 6
letras_erradas = ""

print("Bem-vindo ao jogo da forca!")

while tentativas_restantes > 0:
    print(f"\nA palavra é: {' '.join(palavra_exibida)}")
    letra = input("Digite uma letra: ").strip().upper()
    
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite apenas uma letra válida!")
        continue
    
    if letra in palavra_exibida or letra in letras_erradas:
        print("Você já tentou essa letra. Tente outra.")
        continue
    
    if letra in palavra_secreta:
        nova_palavra = ""
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                nova_palavra += letra
            else:
                nova_palavra += palavra_exibida[i]
        palavra_exibida = nova_palavra
    else:
        letras_erradas += letra
        tentativas_restantes -= 1
        print(f"-> Você errou pela {len(letras_erradas)}ª vez. Tente de novo!")
    
    if "_" not in palavra_exibida:
        print(f"\nParabéns! Você acertou a palavra: {palavra_secreta}")
        break
else:
    print(f"\nVocê foi enforcado! A palavra era: {palavra_secreta}")