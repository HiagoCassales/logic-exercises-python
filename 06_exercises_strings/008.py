'''
Palíndromo. 
Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. 
Por exemplo: OSSO e OVO são palíndromos. 
Em textos mais complexos os espaços e pontuação são ignorados. 
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. 
Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
'''

palindromo = input("Insira uma frase ou palavra: ")
palindromo_sem_espaco = palindromo.replace(' ', '').upper()

if palindromo_sem_espaco == palindromo_sem_espaco[::-1]:
    print(f"A frase ou palavra: \"{palindromo}\" é um palíndromo")
else:
    print(f"A frase ou palavra: \"{palindromo}\" não é um palíndromo")
