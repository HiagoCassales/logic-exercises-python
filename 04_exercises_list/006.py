'''
Faça um Programa que peça as quatro notas de 10 alunos, 
calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
'''
vetor_media = []
aluno_media_sete = 0
id_media = 0

for aluno in range(1, 11):
    soma = 0
    vetor_media.append({})
    vetor_media[aluno - 1]["id_aluno"] = aluno

    for nota in range(1, 5):
        notas = int(input(f"{nota}º nota: "))
        soma += notas
    
    vetor_media[aluno - 1]["media_nota"] = soma / 4

for media_sete in vetor_media:
    if media_sete["media_nota"] >= 7:
        aluno_media_sete += 1
    
    id_media += 1

print(f"A quantidade de alunos com média 7.0+ é {aluno_media_sete}")