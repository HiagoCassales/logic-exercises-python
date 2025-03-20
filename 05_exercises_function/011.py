'''
Data com mês por extenso. 
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''

def validar_data(data):
    partes = data.split("/")
    if len(partes) != 3:
        return False

    dia, mes, ano = partes

    if not (dia.isdigit() and mes.isdigit() and ano.isdigit() and len(ano) == 4):
        return False

    int_dia, int_mes, int_ano = int(dia), int(mes), int(ano)

    if int_mes < 1 or int_mes > 12:
        return False

    if int_mes in [4, 6, 9, 11]:  # Meses com 30 dias
        max_dias = 30
    elif int_mes == 2:  # Fevereiro
        if (int_ano % 4 == 0 and int_ano % 100 != 0) or (int_ano % 400 == 0):  
            max_dias = 29  # Ano bissexto
        else:
            max_dias = 28  # Ano normal de fevereiro
    else:  # Meses com 31 dias
        max_dias = 31

    if int_dia < 1 or int_dia > max_dias:
        return False

    return True

def mes_por_extenso(data):
    if not validar_data(data):
        return None
    else:
        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        partes = data.split("/")
        dia, mes, ano = partes
        int_mes = int(mes)
        return f"{dia} de {meses[int_mes - 1]} de {ano}"

print(mes_por_extenso("29/02/2020"))
