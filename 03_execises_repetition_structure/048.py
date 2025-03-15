# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
'''

numero = int(input("Digite um número inteiro positivo: "))
if numero < 0:
    print("Por favor, insira um número positivo.")
else:
    numero_invertido = 0
    while numero > 0:
        ultimo_digito = numero % 10
        numero_invertido = (numero_invertido * 10) + ultimo_digito
        numero = numero // 10
    print("Número invertido:", numero_invertido)