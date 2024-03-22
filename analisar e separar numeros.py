import openpyxl
import re

# Função para extrair números de uma linha e convertê-los em uma data
def extrair_data(line):
    # Procura por sequências de 8 dígitos na linha
    matches = re.findall(r'\d{8}', line)
    if matches:
        # Supomos que o primeiro conjunto de 8 dígitos representa uma data no formato "DDMMYYYY"
        data_str = matches[0]
        # Converte para o formato "DD/MM/YYYY"
        data_formatada = f"{data_str[0:2]}/{data_str[2:4]}/{data_str[4:]}"
        return data_formatada
    else:
        return None

# Nome do arquivo de texto de entrada
arquivo_entrada = 'nomes_arquivos.txt'

# Nome do arquivo Excel de saída
arquivo_excel = 'dados.xlsx'

# Carregar o conteúdo do arquivo de texto
with open(arquivo_entrada, 'r') as arquivo_txt:
    linhas = arquivo_txt.readlines()

# Criar um novo arquivo Excel
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = 'Dados'

# Escrever os dados no arquivo Excel
for linha in linhas:
    data_formatada = extrair_data(linha)
    if data_formatada:
        sheet.append([data_formatada])

# Salvar o arquivo Excel
workbook.save(arquivo_excel)

print(f'Dados foram extraídos e salvos em {arquivo_excel}')
