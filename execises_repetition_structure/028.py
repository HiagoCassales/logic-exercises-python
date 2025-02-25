# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
'''

qtd_cd = int(input("Quantos CD's foram comprados: "))

total = 0
media = 0

for n in range(1, qtd_cd +1 ):
    valor_unit = float(input("Digite o valor: "))
    total += valor_unit

media = total / qtd_cd

print(f"O valor total foi R$ {total:.2f}")
print(f"A média gasta em cada um foi R$ {media:.2f}")