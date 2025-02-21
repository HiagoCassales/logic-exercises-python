# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

numero = 7
tamanho_numero = len(str(numero))
numero_str = str(numero)

centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 10)

if tamanho_numero == 3:
    print(f"{numero_str} = {numero_str[0]} centenas, {numero_str[1]} dezenas e {numero_str[2]} unidades")
elif tamanho_numero == 2:
    print(f"{numero_str} = {numero_str[0]} dezena e {numero_str[1]} unidades")
elif tamanho_numero == 1:
    print(f"{numero_str} = {numero_str[0]} unidades")

if tamanho_numero == 3:
    print(f'{numero} = {centena} centenas, {dezena} dezenas e {unidade} unidades')
elif tamanho_numero == 2:
    print(f'{numero} = {dezena} dezena e {unidade} unidade')
elif tamanho_numero == 1:
    print(f'{numero} = {unidade} unidade')