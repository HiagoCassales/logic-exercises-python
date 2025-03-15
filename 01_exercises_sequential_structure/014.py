# Logic exercise (Sequential Structure - PythonBrasil)
'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
'''

peso_peixe = float(input("Digite o peso do peixe: "))

peso_estabelecido = 50
multa = 4

if peso_peixe > peso_estabelecido:
    peso_excesso = peso_peixe - peso_estabelecido
    multa_apos = peso_excesso * 4
else:
    multa_apos = 0
    peso_excesso = 0

print(f"Seu peixe pesa {peso_peixe}Kg")
print(f"Teve um excesso de {peso_excesso}Kg")
print(f"Multa de R${multa_apos}")