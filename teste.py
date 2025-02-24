# Define o número inicial e final dos arquivos
inicio = 27
fim = 51

# Loop para criar os arquivos
for i in range(inicio, fim + 1):
    nome_arquivo = f"{i:03}.py"  # Formata o nome do arquivo com 3 dígitos
    with open(nome_arquivo, "w") as f:
        # Conteúdo padrão que será escrito em cada arquivo
        f.write(f"# Logic exercise (Repetition Structure - PythonBrasil)\n")
        f.write(f"'''\n\n'''")
    
    print(f"Arquivo {nome_arquivo} criado com sucesso!")
