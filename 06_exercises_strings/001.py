'''
Tamanho de strings. 
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
'''

string_um = input("Primeira string: ")
string_dois = input("Segunda string: ")

print("Compara duas strings")
print(f"String 1: {string_um}")
print(f"String 2: {string_dois}")
print(f"Tamanho de \"{string_um}\": {len(string_um)} caracteres")
print(f"Tamanho de \"{string_dois}\": {len(string_dois)} caracteres")
if len(string_um) == len(string_dois):
    print("As duas strings são de tamanhos iguais.")
else:
    print("As duas strings são de tamanhos diferentes.")

if string_um == string_dois:
    print("As duas strings possuem conteúdos iguais.")
else:
    print("As duas strings possuem conteúdo diferente.")