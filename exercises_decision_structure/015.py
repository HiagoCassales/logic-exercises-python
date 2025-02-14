# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas: Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;

Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

lado1 = int(input("Informe o primeiro lado do triângulo: "))
lado2 = int(input("Informe o segundo lado do triângulo: "))
lado3 = int(input("Informe o terceiro lado do triângulo: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero: três lados iguais")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles: quaisquer dois lados iguais")
    else:
        print("Triângulo Escaleno: três lados diferentes")
else:
    print("Os valores informados não formam um triângulo.")