# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

notas = 10, 10, 10
media = (notas[0] + notas[1] + notas[2]) / 3

if media == 10:
    print(f"Média {media:.2f}, Aprovado com Distinção")
elif media >= 7:
    print(f"Média {media:.2f}, Aprovado")
elif media < 7:
    print(f"Média {media:.2f}, Reprovado")
