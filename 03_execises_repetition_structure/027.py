# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
'''

qtd_turmas = int(input("Quantidade de turmas: "))
turmas = {}
soma = 0
media = 0

for n in range(1, qtd_turmas + 1):
    numero_alunos = int(input("Número de alunos: "))
    if numero_alunos > 40:
        print("Não pode ter mais de 40 alunos por turma")
        break
    else:
        turmas[n] = numero_alunos
        soma += turmas[n]
    
    media = soma / qtd_turmas

if qtd_turmas <= 0:
    print("Números negativos ou 0 não e aceito! para a quantidade de turmas")
else:
    print(f"A quantidade de turmas são {qtd_turmas}")
    print(f"A média das turmas são {media:.2f}")