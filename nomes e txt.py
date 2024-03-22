import os

# Diretório que você deseja analisar
diretorio = r'C:\Users\adcp church\Desktop\marcenaria'

# Lista para armazenar os nomes dos arquivos
nomes_arquivos = []

# Listar arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    if os.path.isfile(os.path.join(diretorio, nome_arquivo)):
        nomes_arquivos.append(nome_arquivo)

# Nome do arquivo de texto onde os nomes serão armazenados
arquivo_saida = 'nomes_arquivos.txt'

# Escrever os nomes dos arquivos no arquivo de texto
with open(arquivo_saida, 'w') as arquivo:
    for nome_arquivo in nomes_arquivos:
        arquivo.write(nome_arquivo + '\n')

print(f'Nomes dos arquivos foram salvos em {arquivo_saida}')
