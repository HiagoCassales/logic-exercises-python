'''
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. 
A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. 
O programa deverá receber um número indeterminado de entradas, cada uma contendo: 
um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; 
a.necessita troca do cabo ou conector; 
a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. 
Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
'''

produtos = []
defeitos = [[0, "Necessita da esfera"], [0, "Necessita de limpeza"], [0, "Necessita troca do cabo ou conector"], [0, "Quebrado ou inutilizado"]]
total_defeitos = 0

while True:
    item = []
    try:
        id = int(input("ID do produto: "))
        if id == 0:
            break

        item.append(id)
    except ValueError:
        print("Digite o ID corretamente, somente números")
        break

    try:
        print(f"1- necessita da esfera")
        print(f"2- necessita de limpeza")
        print(f"3- necessita troca do cabo ou conector")
        print(f"4- quebrado ou inutilizado")

        defeito = int(input("Código do defeito: "))
        if defeito not in [1, 2, 3, 4]:
            print("Digite uma opção válida, 1 a 4")
            item.pop()
            continue

        item.append(defeitos[defeito - 1][1])
        defeitos[defeito - 1][0] += 1
        total_defeitos += 1
        

    except ValueError:
        print("Digite o código do defeito corretamente, 1 a 4")
        continue

    produtos.append(item)

total_mouses = 0
anterior = 0
for n in produtos:
    if n[0] != anterior:
        total_mouses += 1
    anterior = n[0]

print(f"Quantidade de mouses: {total_mouses}")

print(f"{'Situação':<45}{'Quantidade':<20}{'Percentual'}")
indice = 1
for i in defeitos:
    print(f"{indice}- {i[1]:<42}{i[0]:<20}{(i[0] / total_defeitos * 100):.2f}")
    indice += 1