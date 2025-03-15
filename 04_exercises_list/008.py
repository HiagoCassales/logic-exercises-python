'''
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
'''

idade = []
altura = []

for i in range(1, 6):
    idade.append(int(input(f"{i}º idade: ")))
    altura.append(float(input(f"{i}º altura: ")))

print(f"Idades: {idade[::-1]}")
print(f"Alturas: {altura[::-1]}")