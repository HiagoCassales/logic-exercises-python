# Logic exercise (Repetition Structure - PythonBrasil)
'''
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''

canditado_a = 0
canditado_b = 0
canditado_c = 0

numero_eleitores = int(input("Digite a quantidade de eleitores: "))

for n in range(1, numero_eleitores + 1):
    voto = input("Escolha o candidato A - B - C: ").upper()
    if voto == 'A':
        canditado_a += 1
    elif voto == "B":
        canditado_b += 1
    elif voto == "C":
        canditado_c += 1
    else:
        print("Voto anulado, canditado não existe")
    
    numero_eleitores -= 1

print(f"Canditado A: {canditado_a} Votos")
print(f"Canditado B: {canditado_b} Votos")
print(f"Canditado C: {canditado_c} Votos")