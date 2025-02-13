# Logic exercise (Sequential Structure - PythonBrasil)
'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
tamanho_mb = float(input("Digite o tamanho do Download (MB): "))
velocidade_mbps = float(input("Digite a velocidade da internet (Mbps): "))

# Converte MB para GB
tamanho_gb = tamanho_mb / 1024  

# Converte MB para Megabits (Mb)
tamanho_megabits = tamanho_mb * 8  

# Calcula o tempo de download em segundos
tempo_segundos = tamanho_megabits / velocidade_mbps
tempo_minutos = tempo_segundos / 60

print(f"Tamanho do arquivo: {tamanho_gb:.2f} GB")
print(f"Tempo aproximado de download: {tempo_minutos:.2f} minutos")


