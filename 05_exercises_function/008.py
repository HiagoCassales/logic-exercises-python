'''
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
'''

def contador(numero):
    return len(str(numero).replace("-", ""))

print(contador(45698))