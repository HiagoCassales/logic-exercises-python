# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''

data = input("Informe a data dd/mm/aaaa: ")
mes = int(data[3:5])
dia = int(data[0:2])
ano = int((data[6:10]))
mes30 = 4, 6, 9, 11
mes31 = 1, 3, 5, 7, 8, 10, 12

if mes <= 12 and mes >= 1 and dia < 33 and len(str(ano)) == 4:
    if mes in mes30:
        if dia <= 30 and dia >= 1:
            print("Data válida")

    elif mes in mes31:
        if dia <= 31 and dia >= 1:
            print("Data válida")
    
    elif data[3:5] in "02":
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia >= 28 or dia <= 29:
                print("Data válida")
else:
    print("Data inválida")