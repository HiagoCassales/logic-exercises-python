'''
Verificação de CPF. 
Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx 
e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.
'''
import re

def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    if len(cpf) != 11:
        return False

    nove_digitos = cpf[:9]
    i = 0
    lista_multiplicacao_cpf = []
    soma = 0

    for n in range(10, 1, -1):
        multiplicar = int(nove_digitos[i]) * n
        lista_multiplicacao_cpf.append(multiplicar)
        i += 1
    
    for numero in lista_multiplicacao_cpf:
        soma += numero
    
    resto = (soma * 10) % 11
    primeiro_digito_valido = resto if resto <= 9 else 0

    i_dois = 0
    lista_multiplicacao_cpf_dois = []
    dez_digitos = nove_digitos + str(primeiro_digito_valido)
    soma_dois = 0

    for n in range(11, 1, -1):
        multiplicar = int(dez_digitos[i_dois]) * n
        lista_multiplicacao_cpf_dois.append(multiplicar)
        i_dois += 1

    for numero in lista_multiplicacao_cpf_dois:
        soma_dois += numero

    resto_dois = (soma_dois * 10) % 11
    segundo_digito_valido = resto_dois if resto_dois <= 9 else 0

    cpf_calculado = nove_digitos + str(primeiro_digito_valido) + str(segundo_digito_valido)
    
    if cpf == cpf_calculado:
        return True
    else:
        return False

cpf = input("Insira o CPF no formato xxx.xxx.xxx-xx: ")

if validar_cpf(cpf):
    print(f'{cpf} é válido')
else:
    print(f'{cpf} é inválido')
