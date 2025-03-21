'''
Valida e corrige número de telefone. 
Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. 
O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
'''

numero = input("Número de telefone: ")
numero_sem_hifen = numero.replace("-", "")
numero_corrigido = ""

if len(numero_sem_hifen) < 7 or len(numero_sem_hifen) > 8:
    print("ERRO: telefone digitado menor que 7 ou maior que 8.")
else:
    print("Valida e corrige número de telefone")
    print(f"Telefone: {numero}")
    if len(numero_sem_hifen) == 7:
        numero_sem_hifen = "3" + numero_sem_hifen
        numero_corrigido = numero_sem_hifen[:4] + "-" + numero_sem_hifen[4:]
        print(f"Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
    elif len(numero_sem_hifen) == 8:
        numero_corrigido = numero_sem_hifen[:4] + "-" + numero_sem_hifen[4:]
        
    print(f"Telefone corrigido sem formatação: {numero_sem_hifen}")
    print(f"Telefone corrigido com formatação: {numero_corrigido}")