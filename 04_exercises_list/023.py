'''
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. 
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. 
Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. 
A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. 
O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
'''


with open("04_exercises_list/usuarios.txt", "r", encoding='UTF-8') as arquivo:
    usuarios = arquivo.readlines()

def conversao_byte_megabyte(item):
    return item / 1024 ** 2

def percentual_de_uso(uso_usuario):
    total_uso = 0
    for n in usuarios:
        formatado = n.split()
        total_uso += int(formatado[1])
    return (uso_usuario / total_uso) * 100



print(f"{'ACME Inc.':<25}{'Uso do espaço em disco pelos usuários':<10}")
print(f"{'-'*70}")
print(f"{'Nr.':<5}{'Usuário':<15}{'Espaço utilizado':<25}% do uso")
id = 0
total = 0
for n in usuarios:
    formatado = n.split()
    uso_por_usuario = conversao_byte_megabyte(int(formatado[1]))
    total += uso_por_usuario
    porcentagem_uso_usuario = percentual_de_uso(int(formatado[1]))
    print(f"{id + 1:<5}{formatado[0]:<15}{uso_por_usuario:<25.2f}{porcentagem_uso_usuario:.2f}%")
    id += 1

media = total / id
print(f"Espaço total ocupado: {total:.2f} MB")
print(f"Espaço médio ocupado: {media:.2f} MB")
