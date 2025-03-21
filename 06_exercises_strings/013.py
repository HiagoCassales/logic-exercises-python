'''
Jogo da palavra embaralhada. 
Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. 
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
O jogador terá seis tentativas para adivinhar a palavra. 
Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
'''
import random

with open("06_exercises_strings/palavras.txt", "r", encoding="utf-8") as arquivo:
    palavras = arquivo.read().splitlines()

palavra = random.choice(palavras).lower()
lista_caracteres = list(palavra)
random.shuffle(lista_caracteres)
palavra_embaralhada = ''.join(lista_caracteres)

chances = 6
while chances > 0:
    print("Palavra: ",palavra_embaralhada)
    chute = input("Digite a palavra correta: ").lower().strip()
    if chute == palavra:
        print("Parabens você ganhou a palavra era:",palavra)
        break
    else:
        chances -= 1
        if chances == 0:
            print("Você perdeu, a palavra era:",palavra)
        else:
            print("Você errou tente novamente!")

