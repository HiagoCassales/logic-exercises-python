'''
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. 
Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. 
Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. 
Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. 
Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, 
mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. 
O programa deve fazer uso de arrays. 
O programa deverá executar o cálculo do percentual de cada jogador através de uma função. 
Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. 
Abaixo segue uma tela de exemplo. 
O disposição das informações deve ser o mais próxima possível ao exemplo. 
Os dados são fictícios e podem mudar a cada execução do programa. 
Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

'''

votos = [0] * 23
total_votos = 0
indice = 0
melhor_jogador = 0
votos_melhor_jogador = 0
porcentagem_melhor_jogador = 0

while True:
    try:
        voto = int(input("Número do jogador (0=fim): "))
        if voto == 0:
            break
        elif voto < 0 or voto > 23:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")
            continue
        else:
            total_votos += 1
            votos[voto - 1] += 1

    except ValueError:
        print("Digite apenas números inteiros.")
        continue

def percentual(voto, total):
    return (voto / total) * 100

print(f"Resultado da votação:")
print(f"Foram computados {total_votos} votos.")
print(f"Jogador{' '*10}Votos{' '*10}%")
for n in  range(len(votos)):
    if votos[n] != 0:
        print(f"{n + 1}{' '*16 if len(str(n)) < 2 else ' '*15}{votos[n]}{' '*14 if len(str(votos[n])) < 2 else ' '*13}{percentual(votos[n], total_votos):.2f}%")

        if votos[n] > votos_melhor_jogador:
            melhor_jogador = n + 1
            votos_melhor_jogador = votos[n]
            porcentagem_melhor_jogador = percentual(votos[n], total_votos)

print(f"O melhor jogador foi o número {melhor_jogador}, com {votos_melhor_jogador} votos, correspondendo a {porcentagem_melhor_jogador:.2f}% do total de votos.")

with open("04_exercises_list/resultado_votacao.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Resultado da votação:\n")
    arquivo.write(f"Foram computados {total_votos} votos.\n")
    arquivo.write(f"Jogador{' '*10}Votos{' '*10}%\n")

    for n in range(len(votos)):
        if votos[n] != 0:
            arquivo.write(f"{n + 1}{' '*16 if len(str(n)) < 2 else ' '*15}{votos[n]}{' '*14 if len(str(votos[n])) < 2 else ' '*13}{percentual(votos[n], total_votos):.2f}%\n")
    
    arquivo.write(f"\nO melhor jogador foi o número {melhor_jogador}, com {votos_melhor_jogador} votos, correspondendo a {porcentagem_melhor_jogador:.2f}% do total de votos.\n")