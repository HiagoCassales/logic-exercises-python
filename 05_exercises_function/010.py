'''
Jogo de Craps. 
Faça um programa de implemente um jogo de Craps. 
O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. 
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". 
Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''
import random
def rolar_dados():
    soma_dados = 0
    for n in range(2):
        dado = random.randint(1, 6)
        soma_dados += dado
    return soma_dados

def primeira_jogada():
    soma_dados = rolar_dados()
    if soma_dados in [7, 11]:
        return "natural", soma_dados
    elif soma_dados in [2, 3, 12]:
        return "craps", soma_dados
    elif soma_dados in [4, 5, 6, 8, 9, 10]:
        return "ponto", soma_dados

def jogar_ate_vencedor():
    ponto = primeira_jogada()
    if ponto[0] == "natural":
        print(f"Você tirou {ponto[1]}, venceu!")
    elif ponto[0] == "craps":
        print(f"Você tirou {ponto[1]}, perdeu")
    else:
        print(ponto[0])
        print(f"Você tirou {ponto[1]}")
        while True:
            continuar = input("Para continuar (s/n)").strip().lower()

            if continuar != 's':
                print("você perdeu")
                break

            dados = rolar_dados()
            if dados == 7:
                print(f"Você tirou {dados} perdeu")
                break
            elif dados == ponto[1]:
                print(f"Você tirou {dados} ganhou!")
                break
            else:
                print(f"Você tirou {dados}, jogue novamente")


jogar_ate_vencedor()