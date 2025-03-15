# Logic exercise (Repetition Structure - PythonBrasil)
'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, 
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, 
sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 

Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, 
além da média das alturas e dos pesos dos clientes
'''


maior_altura = float("-inf")
codigo_maior_altura = 0
menor_altura = float("inf")
codigo_menor_altura = 0

maior_peso = float("-inf")
codigo_maior_peso = 0
menor_peso = float("inf")
codigo_menor_peso = 0

soma_altura = 0
media_altura = 0

soma_peso = 0
media_peso = 0

contador = 0

while True:
    codigo = input("Código: ")
    if codigo == "0":
        break
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))
    
    if altura > maior_altura:
        maior_altura = altura
        codigo_maior_altura = codigo
    if altura < menor_altura:
        menor_altura = altura
        codigo_menor_altura = codigo
    if peso > maior_peso:
        maior_peso = peso
        codigo_maior_peso = codigo
    if peso < menor_peso:
        menor_peso = peso
        codigo_menor_peso = codigo
    
    contador += 1
    soma_altura += altura
    soma_peso += peso

try:
    media_altura = soma_altura / contador
    media_peso = soma_peso / contador

    print(f"Cliente mais alto: Código: {codigo_maior_altura} - Altura: {maior_altura}")
    print(f"Cliente mais baixo: Código: {codigo_menor_altura} - Altura: {menor_altura}")
    print(f"Média das alturas dos clientes: {media_altura:.2f}")
    print()
    print(f"Cliente mais gordo: Código: {codigo_maior_peso} - Peso: {maior_peso}")
    print(f"Cliente mais magro: Código: {codigo_menor_peso} - Peso: {menor_peso}")
    print(f"Média dos pessos dos clientes: {media_peso:.2f}")
except ZeroDivisionError:
    print("Não e possivel dividir por 0")