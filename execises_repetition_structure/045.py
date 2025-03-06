# Logic exercise (Repetition Structure - PythonBrasil)
'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota 
(atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
'''

gabarito = {}
index_pergunta = 0

codigo_aluno, nota_aluno = 0, 0
maior, maior_codigo = float("-inf"), 0
menor, menor_codigo = float("inf"), 0
soma = 0

while True:
    print("\nOpções:")
    print("1) Fazer prova")
    print("2) Ver dados")
    print("3) Adicionar perguntas ao gabarito")
    print("4) Sair")

    opcao = input("Escolha uma opção: ")

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida. Tente novamente.")
        continue

    if opcao == "1":
        if not gabarito:
            print("O gabarito ainda não foi definido. Adicione perguntas primeiro.")
            continue

        codigo_aluno += 1
        nota_aluno = 0

        for pergunta in gabarito:
            print(f"\nPergunta {pergunta}: {gabarito[pergunta]['pergunta']}")
            print(f"A - {gabarito[pergunta]['opcao']['A']}")
            print(f"B - {gabarito[pergunta]['opcao']['B']}")
            print(f"C - {gabarito[pergunta]['opcao']['C']}")
            print(f"D - {gabarito[pergunta]['opcao']['D']}")
            print(f"E - {gabarito[pergunta]['opcao']['E']}")

            while True:
                usuario_resposta = input("Selecione a resposta correta (A/B/C/D/E): ").upper()
                if usuario_resposta in ["A", "B", "C", "D", "E"]:
                    break
                print("Resposta inválida. Tente novamente.")

            if usuario_resposta == gabarito[pergunta]["resposta"]:
                nota_aluno += 1

        # Atualiza maior e menor nota
        if nota_aluno > maior:
            maior = nota_aluno
            maior_codigo = codigo_aluno
        if nota_aluno < menor:
            menor = nota_aluno
            menor_codigo = codigo_aluno

        # Atualiza a soma das notas
        soma += nota_aluno

        print(f"\nAluno {codigo_aluno} terminou a prova com {nota_aluno} acertos.")

    elif opcao == "2":
        if codigo_aluno == 0:
            print("Nenhum aluno fez a prova ainda.")
            continue

        media = soma / codigo_aluno
        print(f"\nDados:")
        print(f"Aluno que mais acertou - Código: {maior_codigo} - Nota: {maior}")
        print(f"Aluno que menos acertou - Código: {menor_codigo} - Nota: {menor}")
        print(f"Total de alunos que utilizaram o sistema: {codigo_aluno}")
        print(f"Média das notas: {media:.2f}")

    elif opcao == "3":
        index_pergunta += 1
        pergunta = input("Digite a pergunta: ")
        opcaoA = input("Opção A: ")
        opcaoB = input("Opção B: ")
        opcaoC = input("Opção C: ")
        opcaoD = input("Opção D: ")
        opcaoE = input("Opção E: ")

        while True:
            resposta = input("Resposta correta (A/B/C/D/E): ").upper()
            if resposta in ["A", "B", "C", "D", "E"]:
                break
            print("Resposta inválida. Tente novamente.")

        gabarito[f"{index_pergunta}"] = {
            "pergunta": pergunta,
            "opcao": {"A": opcaoA, "B": opcaoB, "C": opcaoC, "D": opcaoD, "E": opcaoE},
            "resposta": resposta
        }
        print(f"Pergunta {index_pergunta} adicionada ao gabarito.")

    elif opcao == "4":
        print("Encerrando o programa...")
        break