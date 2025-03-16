'''
Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
'''

alunos = []
total_alunos = 30
soma = 0

for i in range(1, total_alunos + 1):
    aluno = []
    aluno.append(int(input(f"Informe a idade do {i}º aluno: ")))
    aluno.append(float(input(f"Informe a altura do {i}º aluno: ")))
    alunos.append(aluno)
    soma += aluno[1]

media_altura = soma / total_alunos

alunos_altura_baixa = 0
for aluno in alunos:
    if aluno[0] > 13 and aluno[1] < media_altura:
        alunos_altura_baixa += 1

print(f"Existe {alunos_altura_baixa} alunos acima dos 13 anos com a altura abaixo da media de todos alunos")