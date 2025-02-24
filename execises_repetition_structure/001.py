# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

notas_validas = [1,2,3,4,5,6,7,8,9,10,0]
print("Informe uma nota entre 0 a 10")
# while True:
#     try:
#         nota = int(input("Digite a nota: "))

#         if nota not in notas_validas:
#             print(f"Nota: {nota} incorreta digite o valor entre 0 a 10")
#         else:
#             print(f"Nota: {nota} válida")
#             break
#     except ValueError:
#         print("Erro! Por favor, digite apenas números.")

while True:
    try:
        nota = float(input("Digite a nota: "))

        if nota >= 0 and nota <= 10:
            print(f"Nota: {nota} válida")
            break
        else:
            print(f"Nota: {nota} incorreta digite o valor entre 0 a 10")

    except ValueError:
        print("Erro! Por favor, digite apenas números.")