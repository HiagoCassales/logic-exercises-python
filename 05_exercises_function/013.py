'''
Desenha moldura. 
Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. 
Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. 
Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
'''

def retangulo(linha, coluna):
    linha = max(1, min(linha, 20))
    coluna = max(1, min(coluna, 20))

    print(f"+{'-' * (coluna - 2)}+")
    for _ in range(linha - 2):
        print(f"|{' ' * (coluna - 2)}|")
    print(f"+{'-' * (coluna - 2)}+")

retangulo(3, 10) 