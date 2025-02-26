# Logic exercise (Repetition Structure - PythonBrasil)
'''
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser 
informados também pelo usuário, conforme exemplo abaixo:

Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
'''

tabuada = int(input("Montar a tabuada de: "))
comeca = int(input("Começar por: "))
termina = int(input("Terminar em: "))

if comeca < termina:
    print(f"Vou montar a tabuada de {tabuada} começando em {comeca} e terminando em {termina}")
    for n in range(comeca, termina +1):
        divisao = tabuada * n
        print(f"{tabuada} X {n} = {divisao}")
else:
    print("O valor do começo precisa ser menor do que o valor final")