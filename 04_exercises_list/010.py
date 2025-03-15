'''
Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
'''
vetor_a = []
vetor_b = []
vetor_c = []

for a in range(10):
    vetor_a.append(int(input(f"{a+1}º número, vetor A: ")))

for b in range(10):
    vetor_b.append(int(input(f"{b+1}º número, vetor B: ")))

for n in range(10):
    vetor_c.append(vetor_a[n])
    vetor_c.append(vetor_b[n])

print(vetor_c)