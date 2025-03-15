# Logic exercise (Repetition Structure - PythonBrasil)
'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while True:
    usuario = input("Digite o nome de usuário: ").upper()
    senha = input("Digite a senha: ").upper()

    if senha == usuario:
        print("A senha não pode ser igual o nome de usuário!")
    else:
        print("Dados válidos")
        break