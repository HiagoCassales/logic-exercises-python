# Logic exercise (Decision Structure - PythonBrasil)
'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

letra = input("Digite uma letra: ")

if letra.isalpha():
    if letra in "aeiouAEIOU":
        print(f"A letra ({letra.upper()}) é uma vogal")
    else:
        print(f"A letra ({letra.upper()}) é uma consoante")
else:
    print("Digite uma letra")