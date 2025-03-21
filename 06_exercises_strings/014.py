'''
Leet spek generator. 
Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. 
A própria palavra leet admite muitas variações, como l33t ou 1337. 
O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. 
Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.
'''

leetspeak = {
    "a": "4", "b": "|3", "c": "(", "d": "|)", "e": "3", "f": "|=", "g": "9", "h": "|-|", "i": "!", "j": "_|", "k": "|<", "l": "|_", 
    "m": "/\\/\\", "n": "/\\/", "o": "0", "p": "|D", "q": "q", "r": "|2", "s": "5", "t": "7", "u": "(_)", "v": "\\/", "w": "\\/\\/", 
    "x": "><", "y": "`/", "z": "2", " ": " ",
}

texto = input("Digite: ").lower()
novo_texto = ""
for t in texto:
    novo_texto += leetspeak.get(t, t)

print(novo_texto)
