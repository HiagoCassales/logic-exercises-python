'''
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''

vetor_a = []
vetor_b = []
vetor_c = []
vetor_resultante = []

for i in range(10):
    vetor_a.append(int(input(f"{i+1}º número, vetor A: ")))
    vetor_b.append(int(input(f"{i+1}º número, vetor B: ")))
    vetor_c.append(int(input(f"{i+1}º número, vetor C: ")))

for n in range(10):
    vetor_resultante.append(vetor_a[n])
    vetor_resultante.append(vetor_b[n])
    vetor_resultante.append(vetor_c[n])

# Exibe o vetor resultante
print(vetor_resultante)