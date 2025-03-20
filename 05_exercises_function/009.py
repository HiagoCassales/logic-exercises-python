'''
Reverso do número. 
Faça uma função que retorne o reverso de um número inteiro informado. 
Por exemplo: 127 -> 721.
'''

def reverso(numero):
    str_numero = str(numero)
    if numero < 0:
        str_numero = str_numero[1::]
        return int('-' + str_numero[::-1])
    else:
        return int(str_numero[::-1])

print(reverso(127))