# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
'''
numeros = ""
numeros_list = []
for n in range(1, 21):
    str_n = str(n)
    numeros += str_n
    numeros_list.append(n)

print(numeros)
print(numeros_list)

