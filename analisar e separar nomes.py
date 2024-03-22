import openpyxl

# Abrir o arquivo de texto
arquivo_texto = 'nomes_arquivos.txt'

# Lista para armazenar os nomes de arquivo processados
nomes_processados = []

# Abrir o arquivo de texto e processar os nomes
with open(arquivo_texto, 'r') as arquivo:
    for linha in arquivo:
        # Dividir a linha em palavras
        palavras = linha.strip().split()
        
        # Verificar se há números nas palavras
        for i, palavra in enumerate(palavras):
            if any(c.isdigit() for c in palavra):
                # Se encontrou um número, remover todas as palavras a partir daqui
                palavras = palavras[:i]
                break
        
        # Juntar as palavras processadas de volta em uma única string
        nome_processado = ' '.join(palavras)
        
        # Adicionar o nome processado à lista
        nomes_processados.append(nome_processado)

# Criar um arquivo do Excel
arquivo_excel = 'nomes_arquivos.xlsx'
workbook = openpyxl.Workbook()
sheet = workbook.active

# Preencher as células do arquivo Excel com os nomes processados
for i, nome in enumerate(nomes_processados, start=1):
    sheet.cell(row=i, column=1, value=nome)

# Salvar o arquivo Excel
workbook.save(arquivo_excel)

print(f'Nomes processados foram salvos em {arquivo_excel}')
