'''
Faça um programa, com uma função que necessite de um argumento. 
A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
'''

def argumento_positivo(n):
    return "P" if n > 0 else "N"

resultado = argumento_positivo(5)
print(resultado)