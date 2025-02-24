# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

while True:
    nome = input("Nome: ")
    if len(nome) < 3:
        print("Nome precisa ter mais que 3 caracteres")
        continue
    
    try:
        idade = input("Idade: ")
        idade = int(idade)
        if idade < 0 or idade > 150:
            print("Digite uma idade entre 0 e 150")
            continue
    except ValueError:
        print("Idade precisa ser um número")
        continue
    
    try:
        salario = input("Salário: ")
        salario = float(salario)
        if salario < 0:
            print("Salário deve ser maior que 0")
            continue
    except ValueError:
        print("Salário deve ser um número")
        continue

    sexo = input("Sexo [m-masculino - f-feminino]: ").upper()

    if sexo not in "M" "F":
        print("Digite os valores [m ou f]")
        continue
    
    estado_civil = input("Estado Civil [s - c - v - d]: ").upper()

    if estado_civil not in ["S","C", "V", "D"]:
        print("Digite uma das opções válidas [s - c - v - d]")
        continue
    else:
        break

print(f"Nome: {nome}\nIdade: {idade}\nSalário: {salario:.2f}\nSexo: {sexo}\nEstado Civil: {estado_civil}")