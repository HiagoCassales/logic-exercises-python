'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
'''
notas = []
soma = 0

while True:
    nota = float(input("Informe a nota: "))

    if nota < 0:
        break

    soma += nota
    notas.append(nota)

media = soma / len(notas)
print(f"Quantidade de notas inseridas {len(notas)}")
print(f"Notas: {notas}")
print("Notas invertidas: ")
for n in notas[::-1]:
    print(f"{n}")
print(f"A soma das notas: {soma}")
print(f"A médias das notas: {media}")

valores_acima_media = 0
for i in notas:
    if i > media:
        valores_acima_media += 1

print(f"Quantidade de notas acima do valor da média: {valores_acima_media}")

valores_abaixo_sete = 0
for i in notas:
    if i < 7:
        valores_abaixo_sete += 1

print(f"Quantidade de notas abaixo de 7.0: {valores_abaixo_sete}")

print("Obrigado por ultilizar nosso serviço!")