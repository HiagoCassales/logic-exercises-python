# Logic exercise (Repetition Structure - PythonBrasil)
'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n-ésimo termo.
'''

termo = int(input("Digite o n-ésimo termo: "))

anterior = 0
proximo = 1

for n in range(termo):
    print(proximo)
    soma = proximo + anterior
    anterior = proximo
    proximo = soma
