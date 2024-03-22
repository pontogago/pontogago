import os

# Função para listar arquivos em um diretório e suas subpastas
def listar_arquivos(diretorio):
    lista_arquivos = []
    for pasta_raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            caminho_completo = os.path.join(pasta_raiz, arquivo)
            lista_arquivos.append(caminho_completo)
    return lista_arquivos

# Diretório que você deseja analisar
diretorio_base =r'C:\Users\adcp church\Desktop\marcenaria'

# Obtém a lista de arquivos
arquivos = listar_arquivos(diretorio_base)

# Nome do arquivo de saída
arquivo_saida = 'nomes_arquivos.txt'

# Escreve os nomes dos arquivos no arquivo de saída
with open(arquivo_saida, 'w') as arquivo_txt:
    for arquivo in arquivos:
        arquivo_txt.write(arquivo + '\n')

print(f'Os nomes dos arquivos foram salvos em {arquivo_saida}')
