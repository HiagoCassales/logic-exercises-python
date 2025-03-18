'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. 
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. 
O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''

votos = [[0, "Windows Server"], [0, "Unix"], [0, "Linux"], [0, "Netware"], [0, "Mac OS"], [0, "Outro"]]

while True:
    count_opcao = 0
    for n in votos:
        print(f"{count_opcao + 1}- {n[1]}")
        count_opcao += 1
    try:
        voto = int(input("Selecione a opção que deseja votar: "))
        if voto == 0:
            break
        if voto not in [1, 2, 3, 4, 5, 6]:
            print("Digite uma opção entre 1 a 6 ou 0 para encerrar")
            continue
    except ValueError:
        print("Insira um valor válido")
        continue

    votos[voto - 1][0] += 1


total_votos = 0
mais_votado = None
porcentagem_mais_votado = 0
for t in votos:
    total_votos += t[0]
def porcentagem(voto, total):
    return (voto / total) * 100

print(f"Sistema Operacional{' '*5}Votos{' '*3}%")
print(f"{'-'*19}{' '*5}{'-'*5}{' '*3}{'-'*3}")
for n in votos:
    print(f"{n[1].ljust(24)}{str(n[0]).ljust(8)}{porcentagem(n[0], total_votos):.0f}%")
    if mais_votado is None or n[0] > mais_votado[0]:
        mais_votado = n
        porcentagem_mais_votado = porcentagem(n[0], total_votos)

print(f"{'-'*19}{' '*5}{'-'*5}")
print(f"Total{' '*19}{total_votos}")
print(f"O Sistema Operacional mais votado foi o {mais_votado[1]}, com {mais_votado[0]} votos, correspondendo a {porcentagem_mais_votado:.0f}% dos votos.")
