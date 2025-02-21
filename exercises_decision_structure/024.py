# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("\nSelecione um operador")
print("\nOperadores")
print("1) valor")
print("2) Subtração")
print("3) Divisão")
print("4) Multiplicação")
operador = input("Digite o valor do operador: ")


if operador == "1":
    operacao = "Soma"
    valor = numero1 + numero2
    if valor % 2 == 0:
        par_impar = "par"
    else:
        par_impar = "ímpar"
    
    if valor < 0:
        negativo_positivo = "negativo"
    else:
        negativo_positivo = "positivo"
    
    if valor % 1 == 0:
        inteiro_decimal = "inteiro"
    else:
        inteiro_decimal = "decimal"

if operador == "2":
    operacao = "Subtração"
    valor = numero1 - numero2
    if valor % 2 == 0:
        par_impar = "par"
    else:
        par_impar = "ímpar"
    
    if valor < 0:
        negativo_positivo = "negativo"
    else:
        negativo_positivo = "positivo"
    
    if valor % 1 == 0:
        inteiro_decimal = "inteiro"
    else:
        inteiro_decimal = "decimal"

if operador == "3":
    operacao = "Divisão"
    valor = numero1 / numero2
    if valor % 2 == 0:
        par_impar = "par"
    else:
        par_impar = "ímpar"
    
    if valor < 0:
        negativo_positivo = "negativo"
    else:
        negativo_positivo = "positivo"
    
    if valor % 1 == 0:
        inteiro_decimal = "inteiro"
    else:
        inteiro_decimal = "decimal"

if operador == "4":
    operacao = "Multiplicação"
    valor = numero1 * numero2
    if valor % 2 == 0:
        par_impar = "par"
    else:
        par_impar = "ímpar"
    
    if valor < 0:
        negativo_positivo = "negativo"
    else:
        negativo_positivo = "positivo"
    
    if valor % 1 == 0:
        inteiro_decimal = "inteiro"
    else:
        inteiro_decimal = "decimal"

print(f"O resultado da {operacao} é {valor}")
print(f"O número {valor} é {par_impar}")
print(f"O número {valor} é {negativo_positivo}")
print(f"O número {valor} é {inteiro_decimal}")

'''
# Solicita os números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Mostra as opções de operação
print("\nSelecione um operador")
print("\nOperadores")
print("1) Soma")
print("2) Subtração")
print("3) Divisão")
print("4) Multiplicação")

operador = input("Digite o valor do operador: ")

# Variáveis para armazenar os resultados
operacao = None
valor = None

# Verifica se a operação é válida antes de calcular
if operador == "1":
    operacao = "Soma"
    valor = numero1 + numero2
elif operador == "2":
    operacao = "Subtração"
    valor = numero1 - numero2
elif operador == "3":
    if numero2 == 0:  # Impede divisão por zero
        print("Erro: Não é possível dividir por zero.")
    else:
        operacao = "Divisão"
        valor = numero1 / numero2
elif operador == "4":
    operacao = "Multiplicação"
    valor = numero1 * numero2
else:
    print("Erro: Operador inválido.")

# Se a operação foi bem-sucedida, verifica as características do resultado
if operacao is not None and valor is not None:
    par_impar = "par" if valor % 2 == 0 else "ímpar"
    negativo_positivo = "negativo" if valor < 0 else "positivo"
    inteiro_decimal = "inteiro" if valor % 1 == 0 else "decimal"

    # Exibe os resultados finais
    print(f"\nO resultado da {operacao} é {valor}")
    print(f"O número {valor} é {par_impar}")
    print(f"O número {valor} é {negativo_positivo}")
    print(f"O número {valor} é {inteiro_decimal}")

'''